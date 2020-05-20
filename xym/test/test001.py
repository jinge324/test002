# # import TestCase.test_weather
# # import getcwd
# # import HTMLTestRunnerCN
# # import os
# #
# # import unittest
# # if __name__ == "__main__":
# #     suite = unittest.TestSuite()
# #     suite.addTest(TestCase.test_weather.weather('test_weather'))
# #     path = getcwd.get_cwd()
# #     file_path = os.path.join(path,'report_baogao/xxx接口自动化测试报告.html')
# #     fp = open(file_path,'wb')
# #     runner = HTMLTestRunnerCN.HTMLTestReportCN(
# #         stream = fp,
# #         title = 'xxx接口自动化测试报告',
# #         description = '报告中描述部分',
# #         tester = '测试者'
# #     )
# #     runner.run(suite)
# #     fp.close()
#
#
# # tim = datetime.datetime.now().date()
# # print(tim)
# #
# # # 先获得时间数组格式的日期
# # threeDayAgo = (datetime.datetime.now() + datetime.timedelta(days=1))
# # # 转换为时间戳
# # timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# # # 转换为其他字符串格式
# # otherStyleTime = threeDayAgo.strftime("%Y-%m-%d")
# # print(otherStyleTime)
#
#
#
# import xym.test_cases.test_fee_one
# import xym.test_cases.test_fee_data.fee_one_data
# import xym.test_cases.test_fee_data.fee_order_data
# import xym.test_cases.test_fee_electric
# import xym.test_cases.test_order_activity
# import xym.request.mybaiduTK
# import xym.request.obtainTK
# import HTMLTestRunner
# import unittest
# import datetime
# import time
#
# if __name__ == "__main__":
#     fee = xym.test_cases.test_order_activity.order()
#     # # 查询店铺ID
#     # test_cases.storeId('雪中')
#     # # 新建应付费用
#     # # EXPENSE（应付费用）   DEPOSIT（保证金）
#     # # feeAmount,  # 应缴金额
#     # # startDate,  # 费用单起始时间
#     # # endDate,  # 费用单终止时间
#     # # payDate,  # 应缴付时间
#     # # refundDate,  # 可退时间（保证金独有）
#     # test_cases.addfee('DEPOSIT', '500', '2020-04-08', '2020-04-08', '2020-04-08', '2020-04-08')
#     # # 审核费用单’YES‘审核通过！其它审核不同！
#     # test_cases.examinefee('NO')
#     # o = xym.request.mybaiduTK.mytk()
#     # # 撤销待审费用单
#     # test_cases.revoke()
#     # # 撤销审核通过费用单
#     # test_cases.revoke_tobesettled()
#     # # 撤销审核不通过费用单
#     # test_cases.revoke_fail()
#     # 结算新建费用单
#     # test_cases.fee_settlement()
#     # 开单
#     fee.order_user()
#     fee.order_address()
#     fee.order_card()
#     print(fee.activities())
#     print(fee.prequalification())
#
#     # # 预缴电费充值
#     # numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     # # test_cases.electric.pay(numbers[1])
#     # for cardId in numbers:
#     #     test_cases.electric.pay(cardId)
#
#     # 时间的获取
#
#
#
#
lst = []
if lst:
    print('c')
else:
    print('cc')