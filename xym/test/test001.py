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
import xym.request.mybaiduTK
import xym.request.obtainTK

if __name__ == "__main__":
    fee = xym.fee.fee_one.fee_test01()
    # 查询店铺ID
    fee.storeId('雪中')
    # 新建应付费用
    # EXPENSE（应付费用）   DEPOSIT（保证金）
    # feeAmount,  # 应缴金额
    # startDate,  # 费用单起始时间
    # endDate,  # 费用单终止时间
    # payDate,  # 应缴付时间
    # refundDate,  # 可退时间（保证金独有）
    fee.addfee('DEPOSIT', '500', '2020-04-08', '2020-04-08', '2020-04-08', '2020-04-08')
    # 审核费用单’YES‘审核通过！其它审核不同！
    fee.examinefee('YES')
    # o = xym.request.mybaiduTK.mytk()



