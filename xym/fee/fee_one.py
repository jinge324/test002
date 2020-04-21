import json
import xym.request.myrequests

class fee_test01:
    global run, headers
    # 先实例化，然后再去调用run_main
    run = xym.request.myrequests.RunMain()
    # 威石tk
    headers = {
        'x - application - context': 'component - gateway - server:8888',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'tk': 'MDNlYWIyMzItYmZkNy00MzRlLWIwMjYtYTk2ZjVlMDM5ODJmMTU4NzEyNTUyNTA=c3RhZmY=MTU4Njc2NDMyOA=='
    }
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
        print('查询店铺storeId:', res1)
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
            print('审核不通过费用单', examine)
        return examine
