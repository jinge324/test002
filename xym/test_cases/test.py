import unittest
from xym.test_cases.test_order_activity import order

suite = unittest.TestSuite()

suite.addTest(order('newuser'))


# ---
with open('test.txt', 'w+', encoding='utf-8') as f:
    runner = unittest.TextTestRunner(stream=f, descriptions='test', verbosity=1)
    runner.run(suite)