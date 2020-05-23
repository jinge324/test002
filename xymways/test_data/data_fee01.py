import datetime
from xymways.test_data.data_total import time_obtain
import xymways.test_case.test_fee_01


global fee, fee_time
fee = xymways.test_case.test_fee_01.Testfee()
fee_time = time_obtain()
class testfee():

    # 费用单的计算主体
    def settlement(self):
        entityName = 'K-结算主体'
        return entityName
    # 新增费用单的费用项
    def expenseitem(self):
        # 保证金
        depositName = '水费押金'
        # 应付费用
        expensename = '电费充值'
        return depositName, expensename
    # 新增保证金费用单
    def add_bond(self):
        # 不添加备注
        data_bond_01 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': fee.test_storeId()[1],
            'entityId': fee.test_feeitem(),
            'feeAmount': "12",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 不输入金额
        data_bond_02 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': fee.test_storeId()[1],
            'entityId': fee.test_feeitem(),
            'feeAmount': "",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 不传可退时间参数
        data_bond_03 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': fee.test_storeId()[1],
            'entityId': fee.test_feeitem(),
            'feeAmount': "13",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            # 'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 不传可退时间参数
        data_bond_04 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': fee.test_storeId()[1],
            'entityId': fee.test_feeitem(),
            'feeAmount': "13",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': '',
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 传入不相对应的entityId（关联的结算主体）
        data_bond_05 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': fee.test_storeId()[1],
            'entityId': '111111111111111',
            'feeAmount': "13",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 费用单金额小于0.01
        data_bond_06 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': fee.test_storeId()[1],
            'entityId': fee.test_feeitem(),
            'feeAmount': "0.0001",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 费用单storeId与merchantNo不相对应
        data_bond_07 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': fee.test_storeId()[0],
            'merchantNo': '',
            'entityId': fee.test_feeitem(),
            'feeAmount': "999",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 费用单storeId与merchantNo不相对应
        data_bond_08 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': '211313231',
            'merchantNo': fee.test_storeId()[1],
            'entityId': fee.test_feeitem(),
            'feeAmount': "999",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 费用单storeId与merchantNo不相对应
        data_bond_09 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "DEPOSIT",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': '21131323sd1',
            'merchantNo': '4564sda5645646546',
            'entityId': fee.test_feeitem(),
            'feeAmount': "999",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        # 费用单类型不一致新建
        data_bond_10 = {
            # 'itemType': 'DEPOSIT',  # EXPENSE（应付费用）   DEPOSIT（保证金）
            'itemType': "EXPENSE",
            'feeItemId': fee.test_expenseitem()[0],
            'payerType': "MERCHANT",
            'storeId': '21131323sd1',
            'merchantNo': '4564sda5645646546',
            'entityId': fee.test_feeitem(),
            'feeAmount': "999",
            'startDate': fee_time.time_YMD()[0],
            'endDate': fee_time.time_YMD()[1],
            'refundDate': fee_time.time_YMD()[1],
            'payDate': fee_time.time_YMD()[2],
            'payerName': "",
            'remark': "123"
        }
        return data_bond_01, data_bond_02, data_bond_03, data_bond_04, data_bond_05,\
               data_bond_06, data_bond_07, data_bond_08, data_bond_09, data_bond_10

