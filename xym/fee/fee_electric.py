import json
import unittest
import xym.request.myrequests
import xym.request.assertion
import xym.fee.fee_test_data.fee_one_data

# 预缴电费
class electric(unittest.TestCase):
    global run, headers, assertion
    # 先实例化，然后再去调用run_main
    run = xym.request.myrequests.RunMain()
    assertion = xym.request.assertion
    # 威石tk
    headers = xym.fee.fee_test_data.fee_one_data.headers
    # 预缴电费缴费
    def pay(number):
        """查询店铺ID"""
        payurl = 'https://api.imways.com/mall/electricity/fee/prepay?feePaymentMode=CASH&isCardCharged=1&storeId=8606&degree=&amount=1'
        paydata = {
            'entityId': 25,
            'rechargeInfo': {
                'assetRechargeMode': "CASH",
                'posInfo': {'enablePoundage': 'true'},
                'remark': xym.fee.fee_test_data.fee_one_data.remark[number]
            },
            'remark': xym.fee.fee_test_data.fee_one_data.remark[number]
        }
        payfee = run.run_main(payurl, 'POST', headers, json.dumps(paydata))
        print(payfee)
