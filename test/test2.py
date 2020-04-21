import json
import xym.request.myrequests
from io import StringIO

# 先实例化，然后再去调用run_main
if __name__ == "__main__":
    run = xym.request.myrequests.RunMain()
    #卡券查询
    url = 'https://api.imways.com/coupon/batch/issued/query/page'
    data = {
        # 'pageNo': '1',
        # 'pageSize': '10'
    }
    #威石tk
    headers = {
        'x - application - context': 'component - gateway - server:8888',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'tk': 'ODIyYWU3OTgtZjk1Ni00MzEzLWI1OWYtYzAwYWE3Nzg0YjFiMTU4NzEyNTUyNTA=c3RhZmY=MTU4NjMxMjYxOA=='
    }
    print('查询线上国际馆的卡券', run.run_main(url, 'GET', headers, data))
    # #人资员工管理查询
    # url1 = 'https://api.imways.com/hrm/employee/manage/paginate/list?pageNo=1&pageSize=20'
    # data1 = {
    #     'pageSize': '20'
    # }
    # # 人资tk
    # HRheaders = {
    #     'tk': 'ZTYyZmYwM2EtYjQ3OC00YWNlLThhMzUtZGM2Y2JkN2U2ZWI3MTU4NzEyNTUyNTA=c3RhZmY=MTU4NTU2MjUxMw=='
    # }
    # print(run.run_main(url, 'GET', headers, data))
    # print(run.run_main(url1, 'POST', HRheaders, data1))
    #查询店铺storeId
    u1 = 'https://api.imways.com/mall/merchant/store/manager/query/list/by/value/and/not/go/out/business?value='
    r1 = '雪中'
    url1 = u1 + r1
    data1 = {
        'value': '雪中'
    }
    print(url1)
    res1 = run.run_main(url1, 'GET', headers, data1)['data'][0]['storeId']
    print('查询店铺storeId:', res1)
    # res2 = res1['data'][0]['storeId']
    # print(res2)
    # 新建费用单
    url2 = 'https://api.imways.com/mall/fee/my/create/fee'
    data2 = {
        'itemType': 'EXPENSE', # EXPENSE（应付费用）   DEPOSIT（保证金）
        'feeItemId': 'kl0001', # kl0001（个人所得税[P]）   SFYJ001（水费押金[D]）
        'payerType': 'MERCHANT',
        'storeId': res1,
        'merchantNo': "1915108",
        'entityId': 25,
        'feeAmount': "500", # 应缴金额
        'startDate': "2020-04-03", # 费用单起始时间
        'endDate': "2020-04-03", # 费用单终止时间
        # 'refundDate': "2020-04-03", # 可退时间（保证金独有）
        'payDate': "2020-04-03", # 应缴付时间
        'payerName': "",
        'remark': "123" #备注
    }
    res = run.run_main(url2, 'POST', headers, json.dumps(data2))
    print('新建保证金费用单', res)
    # 打印返回新建费用单号
    print('返回新建费用单号', res['data'])
    # 审核费用单
    # 审核通过！
    u3 = 'https://api.imways.com/mall/fee/my/audit/approve?feeBillNo='
    r3 = res['data']
    url3 = u3 + r3
    data3 = {
    }
    print('审核通过费用单', run.run_main(url3, 'POST', headers, data3))
    # 审核不通过！费用单
    yaunyin = '123456test'
    u4 = 'https://api.imways.com/mall/fee/my/audit/reject?'
    r4 = 'feeBillNo=' + res['data']
    l4 = '&reason=' + '123456test'
    url4 = u4 + r4 + l4
    data4 = {
        'feeBillNo': res['data'],
        'reason': '123456测试test'
    }
    # print('审核不通过费用单', run.run_main(url4, 'POST', headers, json.dumps(data4)))

    # 查询新建费用单
    selectfeeurl = 'https://api.imways.com/mall/fee/finance/unsettled/fee/bill/paginate/list'
    selectfeedata = {
        'startDate': "2020-01-08",
        'endDate': "2020-07-06",
        'timeQueryBy': "CREATE_TIME",
        'typeQueryBy': "FEE_BILL_NO",
        'keyword': res['data'],
        'seeSystemFee': 'false'
    }
    res2 = run.run_main(selectfeeurl, 'POST', headers, json.dumps(selectfeedata))['data']['list'][0]['entityId']
    print('查询新建的费用单entityId:', res2)

    #支付费用单
    zhi = 'https://api.imways.com/mall/balance/manage/expense/fee/pay?feePaymentMode=CASH&'
    urlzhi = 'amount=' + data2['feeAmount']
    urlfu = '&feeBillNo=' + res['data']
    urlzhifu = zhi + urlzhi + urlfu
    datazhifu = {
        # 'rechargeInfo': {'assetRechargeMode':'CASH', 'bankInfo':{"dueBank":"","dueDate":"","transferPerson":""},"checkInfo":{"checkNumber":"","checkPayer":""},"posInfo":{"enablePoundage":true,"feePaymentPosType":"CREDITCARD","posSerialNumber":""},"remittanceInfo":{"remittanceNum":"","remittanceName":""},
        'remark': '',
        'subsidyNo': ''
    }
    # print(urlzhi)
    # print(urlfu)
    # print(urlzhifu)
    print('支付新建费用单：', run.run_main(urlzhifu, 'POST', headers, json.dumps(datazhifu)))

    # 新增卡券
    print('#新增卡券')
    # url5 = 'https://api.imways.com/mall/config/category/query/category/tree/level'
    # data5 = {
    # }
    # print(run.run_main(url5, 'GET', headers, data5))
    url6 = 'https://api.imways.com/mall/coupon/manage/center/coupon/add'
    data6 = {
        'category': '1003',
        'couponName': '商场优惠券-4-2',
        'shortCouponName': '商场优惠券-4-2',
        'denomination': 99,
        'useCondition': 100,
        'isLimit': '1',
        'totalNum': '',
        'isEach': 0,
        'couponCover': 'https://xym-ways-public.oss-cn-hangzhou.aliyuncs.com/coupon/image/66/1278/20200401/7c8b9091-35a6-2301-4de0-3bed73e7640d.jpg',
        'unitType': 1,
        # 'unitIds': 'null',
        'couponDesc': '商场优惠券-4-2',
        'noticeToOperation': '<p>商场优惠券-4-2</p><p><br></p>',
        'orderSource': '',
        'categoryId': '',
        'range': 'all',
        'canAccumulate': 0,
        'donationType': 'NOT_DONATION',
        'maxAccumulate': '',
        'maxAccumulate': '',
        # 'writeOffLimitCount': 'null',
        # 'writeOffIsLimit': 'null',
        # 'writeOffLimitUnit': 'null',
        # 'screenBgImage': 'null',
        # 'showFinishEffect': 'null',
        'isNextDay': 0
    }
    print(data6['couponName'])
    # print(run.run_main(url6, 'POST', headers, json.dumps(data6)))
    # 查询卡券新建优惠券  data6['couponName']
    print('#查询卡券:', data6['couponName'])
    # name = '商场优惠券-4-2'
    u7 = 'https://api.imways.com/mall/coupons/manage/page?pageNo=1&pageSize=20&couponName='
    r7 = data6['couponName']
    l7 = '&storeName=&category='
    url7 = u7 + r7 + l7
    data7 = {
        # 'pageNo': 1,
        # 'pageSize': 20,
        # 'couponName': data6['couponName']
    }
    print(run.run_main(url7, 'GET', headers, json.dumps(data7)))
    # 发布新建的卡券
    url8 = 'https://api.imways.com/mall/coupons/manage/publish'
    data8 = {
        'couponId': '12107'
    }
    print(run.run_main(url8, 'POST', headers, data8))
