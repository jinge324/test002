import json
import unittest
import xym.request.myrequests
import xym.request.assertion
import xym.fee.fee_test_data.fee_one_data

class fee_test01(unittest.TestCase):
    global run, headers, assertion
    # 先实例化，然后再去调用run_main
    run = xym.request.myrequests.RunMain()
    assertion = xym.request.assertion
    # 威石tk
    headers = xym.fee.fee_test_data.fee_one_data.headers
    # 查询店铺storeId
    def storeId(self, namestore):
        global res1
        u1 = 'https://api.imways.com/mall/merchant/store/manager/query/list/by/value/and/not/go/out/business?value='
        # '雪中'
        r1 = namestore
        url1 = u1 + r1
        data1 = {
            # '雪中'
            'value': namestore
        }
        res1 = run.run_main(url1, 'GET', headers, data1)['data'][0]['storeId']
        # 断言
        assertion.assertions(self, contrast=6268, passvalue=res1)
        # print(res1)
        return res1

    # 新建应付费用
    def addfee(self, itemType, feeAmount, startDate, endDate, payDate, refundDate):
        global res
        url2 = 'https://api.imways.com/mall/fee/my/create/fee'
        if itemType == 'EXPENSE':
            data2 = {
                'itemType': 'EXPENSE',  # EXPENSE（应付费用）   DEPOSIT（保证金）
                'feeItemId': 'kl0001',  # kl0001（个人所得税[P]）   SFYJ001（水费押金[D]）
                'payerType': 'MERCHANT',
                'storeId': res1,
                'merchantNo': "1915108",
                'entityId': 25,
                'feeAmount': feeAmount,  # 应缴金额
                'startDate': startDate,  # 费用单起始时间
                'endDate': endDate,  # 费用单终止时间
                # 'refundDate': "2020-04-03", # 可退时间（保证金独有）
                'payDate': payDate,  # 应缴付时间
                'payerName': "",
                'remark': ""  # 备注
            }
            res = run.run_main(url2, 'POST', headers, json.dumps(data2))
            # 断言
            assertion.assertions(self, contrast=200, passvalue=res['code'])
            print('新建应付费用', res)
        else:
            data2 = {
                'itemType': itemType,  # EXPENSE（应付费用）   DEPOSIT（保证金）
                'feeItemId': 'SFYJ001',  # kl0001（个人所得税[P]）   SFYJ001（水费押金[D]）
                'payerType': 'MERCHANT',
                'storeId': res1,
                'merchantNo': "1915108",
                'entityId': 25,
                'feeAmount': feeAmount,  # 应缴金额
                'startDate': startDate,  # 费用单起始时间
                'endDate': endDate,  # 费用单终止时间
                'refundDate': refundDate,  # 可退时间（保证金独有）
                'payDate': payDate,  # 应缴付时间
                'payerName': "",
                'remark': "123"  # 备注
            }
            res = run.run_main(url2, 'POST', headers, json.dumps(data2))
            # 断言
            assertion.assertions(self, contrast=200, passvalue=res['code'])
            print('新建保证金', res)
        return res

    # 审核新建的费用单
    def examinefee(self, bei):
        if bei == 'YES':
            u3 = 'https://api.imways.com/mall/fee/my/audit/approve?feeBillNo='
            r3 = res['data']
            url3 = u3 + r3
            data3 = {
            }
            examine = run.run_main(url3, 'POST', headers, data3)
            assertion.assertions(self, contrast=200, passvalue=examine['code'])
            print('审核通过费用单', examine)
        else:
            u4 = 'https://api.imways.com/mall/fee/my/audit/reject?'
            r4 = 'feeBillNo=' + res['data']
            l4 = '&reason=' + bei
            url4 = u4 + r4 + l4
            data4 = {
                'feeBillNo': res['data'],
                'reason': '123456测试test'
            }
            examine = run.run_main(url4, 'POST', headers, json.dumps(data4))
            assertion.assertions(self, contrast=200, passvalue=examine['code'])
            print('审核不通过费用单', examine)
        return examine

    # 撤销待审核费用单
    def revoke(self):
        revokeurl = 'https://api.imways.com/mall/fee/my/audit/revoke/pending/audit?feeBillNo=' + res['data']
        revokedata = {}
        idasd = run.run_main(revokeurl, 'POST', headers, revokedata)
        print('撤销成功：', idasd)
        # 断言
        assertion.assertions(self, contrast=200, passvalue=idasd['code'])

    # 撤销待结算费用单
    def revoke_tobesettled(self):
        tobesettledurl = 'https://api.imways.com/mall/fee/my/audit/revoke/unsettled?feeBillNo=' + res['data']
        tobesettled = run.run_main(tobesettledurl, 'POST', headers)
        print('撤销待审核费用单：',  tobesettled)
        # 断言
        assertion.assertions(self, contrast=200, passvalue=tobesettled['code'])

    # 撤销审核不通过费用单
    def revoke_fail(self):
        failurl = 'https://api.imways.com/mall/fee/my/audit/revoke/rejected?feeBillNo=' + res['data']
        auditfail = run.run_main(failurl, 'POST', headers)
        print('撤销审核不通过费用单：', auditfail)
        # 断言
        assertion.assertions(self, contrast=200, passvalue=auditfail['code'])

    # 结算新建费用单
    def fee_settlement(self):
        settlementurl = 'https://api.imways.com/mall/balance/manage/deposit/fee/pay?feeBillNo=D2020031303677&amount=1&feePaymentMode=ASSET'
        ui = {'enablePoundage': 'true', 'feePaymentPosType': 'CREDITCARD'}
        settlementdata = {
            'rechargeInfo': {
                'posInfo': ui,
                'remark': '123'
            },
            'remark': '123'
        }

        settlement = run.run_main(settlementurl, 'POST', headers, settlementdata)
        print(settlement)

    # 开单老用户查询
    def order_user(self):
        global customid
        userurl = 'https://api.imways.com/merchant/store/order/manage/get/custom/info?mobile=17521279329'
        ueerdata = {
            'mobile': 17521279329
        }
        orderuser = run.run_main(userurl, 'GET', headers, ueerdata)
        assertion.assertions(self, contrast=200, passvalue=orderuser['code'])
        # print(orderuser['data'][0])
        customid = orderuser['data'][0]['custId']
        print(customid)

    # 查询到开单老用户的地址
    def order_address(self):
        addressurl = 'https://api.imways.com/merchant/store/order/open/distribution?customId=35521'
        addressdata = {
            "customId": customid
        }
        orderaddress = run.run_main(addressurl, 'POST', headers)
        assertion.assertions(self, contrast=200, passvalue=orderaddress['code'])

        print(orderaddress)

    # 查询开单用户会员卡
    def order_card(self):
        cardu = 'https://api.imways.com/merchant/custom/member/card/query/list?customId='
        cardr = json.dumps(customid)
        cardl = '&orderId='
        cardurl = cardu + cardr + cardl
        ordercard = run.run_main(cardurl, 'GET', headers)
        # 根据需要的联名卡来进行返回参数
        membershipcard = ordercard['data']
        print(membershipcard)
        print(len(membershipcard))
        for cardId in membershipcard:
           if cardId['cardName'] == xym.fee.fee_test_data.fee_one_data.card:
                print('cardId:', cardId['cardId'])
                break





        return membershipcard

    print(sjioejf
    '')