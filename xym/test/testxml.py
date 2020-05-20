# import time
# from HTMLTestRunner import HTMLTestRunner
# import unittest
#
# def allCase():
#     """定义一个函数，封装discover加载测试用例的方法"""
#     case_dir = 'E:/python/iop/xym/test_cases'  # 定义用例所在路径
#     suite = unittest.TestSuite()  # 定义一个测试套件
#     discover = unittest.defaultTestLoader.discover(case_dir,
#                                                    pattern='test_*.py',
#                                                    top_level_dir=None)
#     # discover 方法筛选出来的用例，循环添加到测试套件中
#     for test_suite in discover:
#         for test_case in test_suite:
#             suite.addTests(test_case)
#     return suite
#
#
# if __name__ == '__main__':
#     allsuite = allCase()
#     # runner = unittest.TextTestRunner()
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     filename = 'E:/python/iop/xym/' + now + '_result.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp,
#                             title='UnifiedReporting Test Report',
#                             description='Implementation Example with: ')
#     runner.run(allsuite)

#
# import unittest
# import time
# import HTMLTestRunner
# import unittest
# from xym.test_cases import test_order_activity
# from xym.test_cases import test_fee_electric
#
# # 存储用例
# suite = unittest.TestSuite()  # 实例化
# # 加载所有测试用例
# loader = unittest.TestLoader()
# # 加载模块
# suite.addTest(loader.loadTestsFromModule(test_order_activity.order))
#
#    # runner = unittest.TextTestRunner()
# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = 'E:/python/iop/xym/' + now + '_result.html'
# # 生成HTML测试报告
# with open(filename, 'wb') as f:
#     # runner = HTMLTestRunner(stream=f, verbosity=2, title='==威石项目测试报告==', description=None)
#     runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='==威石项目测试报告==', description=None)
#     runner.run(suite)

import unittest
from xym.test_cases.test_order_activity import order
import HTMLTestRunner
suite = unittest.TestSuite()

suite.addTest(order('newuser'))


# ---
with open('test.txt', 'w+', encoding='utf-8') as f:

    runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2, title='awe', description='alkme')
    runner.run(suite)








































