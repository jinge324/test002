import json
import xym.request.myrequests
import xym.fee.fee_test_data.fee_one_data

class order_qw():
    def iop(self):
        run = xym.request.myrequests.RunMain
        headers = xym.fee.fee_test_data.fee_one_data.headers
        payurl = 'https://api.imways.com/mall/electricity/fee/prepay?feePaymentMode=CASH&isCardCharged=1&storeId=8606&degree=&amount=1'
        paydata = {
            'entityId': 25,
            'rechargeInfo': {
                'assetRechargeMode': "CASH",
                'posInfo': {'enablePoundage': 'true'},
                'remark': 'iowefjio'
            },
            'remark': 'jieofjwaoi'
        }
        payfee = run.run_main(payurl, 'POST', headers, json.dumps(paydata))
        print(payfee)


if __name__ == "__main__":
    order_qw.iop()