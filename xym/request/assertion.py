# 断言
def assertions(self, contrast, passvalue):
    try:
        self.assertEqual(contrast, passvalue)
    except AssertionError:
        print('断言错误：提示为{0}'.format(passvalue))
