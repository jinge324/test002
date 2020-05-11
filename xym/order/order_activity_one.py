# import json
# import xym.request.myrequests
#
# class order:
#     global run, headers
#     # 先实例化，然后再去调用run_main
#     run = xym.request.myrequests.RunMain()
#     # 威石tk
#     headers = {
#         'x - application - context': 'component - gateway - server:8888',
#         'content-type': 'application/json;charset=UTF-8',
#         # 'accept': 'application/json, text/plain, */*',
#         'tk': 'OGYzOWYxNTEtMGUwOS00ZDIxLThhMGItYmNlYjRhNjE1ZjkwMTM3MDAwMDc3Nzc=Y2xlcms=MTU4NzcxNDUxNg=='
#     }
#     # 订单开具
#     def issue():
#         issurl = 'https://b.imways.com//merchant/store/order/open/create'
#         # 商品添加
#         orderGoods = [{'goodsId': "794670", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 1000, 'salePriceTotal': 1000, 'isSpecialPrice': 'false', 'remark': "", 'goodsClass': "COMMON"},
#                       {'goodsId': "840235", 'orderQty': "1", 'marketPrice': 15000, 'salePrice': 15000, 'salePriceTotal': 15000, 'isSpecialPrice': 'false', 'remark': "", 'goodsClass': "SET"}]
#         # 参加的活动
#         orderActivityRelList = [{'activityId': 1185, 'activityType': "fulfil_quota"}, {'activityId': 1209, 'activityType': "fulfil_quota"}, {'activityId': 1210, 'activityType': "fulfil_quota"}, {'activityId': 1208, 'activityType': "fulfil_quota"}, {'activityId': 1206, 'activityType': "fulfil_quota"}, {'activityId': 1199, 'activityType': "fulfil_quota"}]   #  , 'placeCode': null, 'freeOrderTypeEnums': null
#         #
#         orderExts = [{'key': "needDelivery", 'value': 0}, {'key': "expectedCompleteDate", 'value': 1587571200}, {'key': "customizedImage", 'value': ''}, {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}]
#         customDTO = {'realName': "赵金鸽"}
#         # https://api.imways.com/merchant/custom/member/card/query/list?customId=35521&orderId=    get
#         memberCardInfoDTO = {'cardId': "1980000016888", 'cardName': "喜盈门会员卡", 'cardType': "MEMBER_CARD", 'cardTypeName': "喜盈门会员卡", 'defaultFlag': 'true', 'memberCode': '1980000016888', 'addFriendsFlag': 'false'}
#
#         issdata = {
#             'orderType': '1003',
#             'customId': '35521',
#             'orderGoods': orderGoods,
#             'orderExts': orderExts,
#             'addressId': '12687',
#             'originalAmount': '25000',
#             'discountAmount': '0',
#             'realAmount': '25000',
#             'orderDesc': '智能橱柜 等',
#             'customDTO': customDTO,
#             'orderActivityRelList': orderActivityRelList,
#             'memberCardInfoDTO': memberCardInfoDTO
#         }
#         res = run.run_main(issurl, 'POST', headers, json.dumps(issdata))
#         print(res)
#         return res
#
#     # 订单开具--根据手机号查询顾客,返回用户custId
#     def issue_customer(phonenumber):
#         global custId
#         customer = 'https://api.imways.com/merchant/store/order/manage/get/custom/info?mobile='
#         customerurl = customer + '15871255250'
#         customerdata = {
#             'mobile': phonenumber
#         }
#         custId = run.run_main(customerurl, 'GET', headers, json.dumps(customerdata))['data'][0]['custId']
#         print(custId)
#         return custId
#     # 根据用户custId查找用户收货地址
#     def address():
#         addressurl = 'https://api.imways.com/merchant/store/order/open/distribution'
#         addressdata = {
#             'customId': custId
#         }
#         addrsss = run.run_main(addressurl, 'POST', headers, json.dumps(addressdata))
#         print(addrsss)
#         return addrsss
#
#
#
# if __name__ == "__main__":
#     # orderr = order.issue()
#     number = '15871255250'
#     uiwe = order.issue_customer('15871255250')
#     order.address()


