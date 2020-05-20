import json
import unittest
import xym.request.myrequests
import xym.request.assertion
import xym.test_cases.test_fee_data.fee_one_data
import datetime

class activitys(unittest.TestSuite):
    global run, headers, assertion
    # 先实例化，然后再去调用run_main
    run = xym.request.myrequests.RunMain()
    assertion = xym.request.assertion
    # 威石tk
    headers = xym.test_cases.test_fee_data.fee_one_data.headers

    # 新建免单活动
    def exemption(self):


