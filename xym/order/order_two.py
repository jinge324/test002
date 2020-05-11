import json
import xym.request.myrequests
import xym.request.assertion
import xym.order.order_test_data.order_one
import unittest


class order_test01(unittest.TestCase):
    global run, headers, asswerion
    run = xym.request.myrequests.RunMain
    headers = xym.order.order_test_data.order_one.headers
    asswerion = xym.request.assertion
    # 查询店铺storeId
    def sto(self):
        url = 'https://api.imways.com/merchant/store/clerk/manage/load/store/posts'
        res1 = run.run_main(url, 'POST', headers)
        print('查询店铺storeId:', res1)
        xym.request.assertion.assertions(set, contrast=200, passvalue=res1['data'])

    # 开单用户查询
    def order_user(self):
        userurl = 'https://api.imways.com/merchant/store/order/manage/get/custom/info?mobile=15871255250'
        ueerdata = {
            'mobile': 15871255250
        }
        orderuser = run.run_main(self, userurl, 'GET', headers, ueerdata)
        print(orderuser)

