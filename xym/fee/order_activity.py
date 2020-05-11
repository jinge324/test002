import json
import unittest
import xym.request.myrequests
import xym.request.assertion
import xym.fee.fee_test_data.fee_one_data

class order():
    global run, headers, assertion
    # 先实例化，然后再去调用run_main
    run = xym.request.myrequests.RunMain()
    assertion = xym.request.assertion
    # 威石tk
    headers = xym.fee.fee_test_data.fee_one_data.headers
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



    #
    def jsaof(self):
        run.run_main()
        v