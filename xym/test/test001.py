# import TestCase.test_weather
# import getcwd
# import HTMLTestRunnerCN
# import os
#
# import unittest
# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTest(TestCase.test_weather.weather('test_weather'))
#     path = getcwd.get_cwd()
#     file_path = os.path.join(path,'report_baogao/xxx接口自动化测试报告.html')
#     fp = open(file_path,'wb')
#     runner = HTMLTestRunnerCN.HTMLTestReportCN(
#         stream = fp,
#         title = 'xxx接口自动化测试报告',
#         description = '报告中描述部分',
#         tester = '测试者'
#     )
#     runner.run(suite)
#     fp.close()

import xym.fee.fee_one
import xym.fee.fee_test_data.fee_one_data
import xym.fee.fee_electric
import xym.request.mybaiduTK
import xym.request.obtainTK
import HTMLTestRunner
import unittest

if __name__ == "__main__":
    fee = xym.fee.fee_electric
    # # 查询店铺ID
    # fee.storeId('雪中')
    # # 新建应付费用
    # # EXPENSE（应付费用）   DEPOSIT（保证金）
    # # feeAmount,  # 应缴金额
    # # startDate,  # 费用单起始时间
    # # endDate,  # 费用单终止时间
    # # payDate,  # 应缴付时间
    # # refundDate,  # 可退时间（保证金独有）
    # fee.addfee('DEPOSIT', '500', '2020-04-08', '2020-04-08', '2020-04-08', '2020-04-08')
    # # 审核费用单’YES‘审核通过！其它审核不同！
    # fee.examinefee('NO')
    # o = xym.request.mybaiduTK.mytk()
    # # 撤销待审费用单
    # fee.revoke()
    # # 撤销审核通过费用单
    # fee.revoke_tobesettled()
    # # 撤销审核不通过费用单
    # fee.revoke_fail()
    # 结算新建费用单
    # fee.fee_settlement()
    # 开单
    # fee.order_user()
    # fee.order_address()
    # fee.order_card()
    # print(len(xym.fee.fee_test_data.fee_one_data.card))
    # orderer = xym.order.order_activity_one.order_test01
    # orderer.order_user()


    # # 预缴电费充值
    # numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # # fee.electric.pay(numbers[1])
    # for cardId in numbers:
    #     fee.electric.pay(cardId)


