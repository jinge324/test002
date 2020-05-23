import requests
import json
from xymways.test_method.reques_Interface import runmain
from xymways.test_data.data_total import headers_market
import xymways.test_data.data_fee01

class Testfee():
    global run
    run = runmain()
    # 查询店铺storeId
    def test_storeId(self):
        u1 = 'http://api.xymtest.com/mall/merchant/store/manager/query/list/by/value/and/not/go/out/business?value='
        # '雪中'
        r1 = '南阳全盘'
        url = u1 + r1
        res = run.run_main(url, 'GET', headers_market)
        assert res['code'] == 200
        res1 = res['data'][0]['storeId']
        res2 = res['data'][0]['merchantNo']
        # print(res)
        return res1, res2
    # 查询测试商场结算主体
    def test_settlement(self):
        global testdata
        testdata = xymways.test_data.data_fee01.testfee()
        url = 'http://api.xymtest.com/mall/config/balance/entity/query/list'
        res = run.run_main(url, 'GET', headers_market)
        assert res['code'] == 200
        # print(res)
        for zong in res['data']:
            if zong['entityName'] ==testdata.settlement():
                entityId = zong['entityId']
                # print(entityId)
                break
        return entityId
    # 查询测试商场费用项
    def test_expenseitem(self):
        testdata = xymways.test_data.data_fee01.testfee()
        url = 'http://api.xymtest.com/mall/config/fee/item/select/list/grouping/by/item/type'
        res = run.run_main(url, 'GET', headers_market)
        assert res['code'] == 200
        expense = res['data']['EXPENSE']
        deposit = res['data']['DEPOSIT']
        # print(res)
        # 应付费用
        for yingfu in expense:
            if yingfu['feeItemName'] == testdata.expenseitem()[1]:
                expense_code = yingfu['feeItemCode']
                # print(expense_code)
                break
        # 保证金
        for baozheng in deposit:
            if baozheng['feeItemName'] == testdata.expenseitem()[0]:
                deposit_code = baozheng['feeItemCode']
                # print(deposit_code)
                break
        return deposit_code, expense_code
    # 查询保证金所关联的结算主体
    def test_feeitem(self):
        ur = 'http://api.xymtest.com/mall/config/feeitem/get/info/by/code?feeItemCode='
        ul = Testfee().test_expenseitem()[0]
        url = ur + ul
        res = run.run_main(url, 'GET', headers_market)
        assert res['code'] == 200
        entityId = res['data']['entityId']
        # print(res)
        return entityId
    # 查询应付费用所关联的结算主体
    def test_feeiten(self):
        ur = 'http://api.xymtest.com/mall/config/feeitem/get/info/by/code?feeItemCode='
        ul = Testfee().test_expenseitem()[1]
        url = ur + ul
        res = run.run_main(url, 'GET', headers_market)
        assert res['code'] == 200
        entityId = res['data']['entityId']
        # print(res)
        return entityId
    # 新增保证金
    def test_add_bond_01(self):
        print('新增保证金不添加备注')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[0]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['code'] == 200
        print(res)
    def test_add_bond_02(self):
        print('新增保证金不输入金额')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[1]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['message'] == '请输入金额'
        print(res)
    def test_add_bond_03(self):
        print('新增保证金,不传可退时间参数')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[2]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['message'] == '请选择费用可退日期'
        print(res)
    def test_add_bond_04(self):
        print('新增保证金,不传可退时间参数')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[3]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['message'] == '请选择费用可退日期'
        print(res)
    def test_add_bond_05(self):
        print('新增保证金,传入不相对应的entityId（关联的结算主体）')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[4]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['code'] != 200
        print(res)    
    def test_add_bond_06(self):
        print('新增保证金,费用单金额小于0.01')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[5]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['code'] != 200
        print(res)
    def test_add_bond_07(self):
        print('新增保证金,费用单storeId与merchantNo不相对应')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[6]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['code'] != 200
        print(res)
    def test_add_bond_08(self):
        print('新增保证金,费用单storeId与merchantNo不相对应')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[7]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['message'] == '店铺不存在'
        print(res)
    def test_add_bond_09(self):
        print('新增保证金,费用单storeId与merchantNo不相对应')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[8]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['code'] != 200
        print(res)
    def test_add_bond_10(self):
        print('新增保证金,费用单类型不一致新建')
        url = 'http://api.xymtest.com/mall/fee/my/create/fee'
        data = testdata.add_bond()[9]
        res = run.run_main(url, 'POST', headers_market, json.dumps(data))
        assert res['code'] != 200
        print(res)
    # def test_lain(self):
    #     url = 'http://api.xymtest.com/mall/config/pos/separate/account/scheme/update/enable/flag?schemeId=41&enableFlag=1'
    #     res = run.run_main(url, 'POST', headers_market)
    #     print(res)