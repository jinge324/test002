import xym.test_cases.test_order_activity
import datetime
import time

global iop, timeStamp
iop = xym.test_cases.test_order_activity.order()
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() + datetime.timedelta(days=1))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 异常开单
def billings_01():
    # 开单不添加商品
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单送货，不添加地址
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [{'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': '',
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单不送货，添加地址
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [{'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 0}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单没有用户
    billing_four = {
        'orderType': "1003",
        'customId': '',
        'orderGoods': [{'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单用户没有会员卡
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [{'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': ''
    }
    # 开单用户没有顾客姓名
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': '',
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单不填预计完成时间
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [{'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': ''},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单预计完成时间填今天之前
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': 1557504000},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 开单商品是其它店铺的商品
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169348", 'orderQty': "1", 'marketPrice': 100, 'salePrice': 100, 'salePriceTotal': 100,
             'isSpecialPrice': 'false', 'goodsClass': "COM"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 100,
        'discountAmount': 100,
        'realAmount': 100,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 修改开单商品的类型
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': 1557504000},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }

    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 正常开单
def billings():
    # 不参加活动,不需送货，单个普通商品开单
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
        }
    # 不参加活动,需送货，单个普通商品开单
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "2", 'marketPrice': 1000, 'salePrice': 1000, 'salePriceTotal': 2000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 2000,
        'discountAmount': 0,
        'realAmount': 2000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
        }
    # 不参加活动,不需送货，单个套组品开单
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动,不需送货，单个服务费用商商品开单
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动,多个普通商品开单
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [{'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}, {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动,多个套组商品开单
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}, {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动,多个服务费商品开单
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}, {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品与套组开单
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品与服务费开单
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组与服务开单
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
             'isSpecialPrice': 'false', 'goodsClass': "SET"},
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "超好吃唱个歌炒个菜",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }

    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 普通商品特价
def billings_02():
    # 不参加活动， 普通商品特价（不打折）开单,不送货,开启预审
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 0,
        'realAmount': 1000,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品特价（不打折）开单,送货,关闭预审
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169350", 'orderQty': "1", 'marketPrice': 3333, 'salePrice': 3333, 'salePriceTotal': 3333,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}, {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2100, 'salePriceTotal': 2100,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 5433,
        'discountAmount': 0,
        'realAmount': 5433,
        'remark': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
        'orderDesc': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品特价（单品打折为0）开单,不送货,开启预审
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 1000,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品不特价（单品打折为0）开单,不送货,开启预审
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 1000,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品特价（单品打折为0）开单,不送货,关闭预审
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 1000,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品不特价（单品打折为0）开单,不送货,关闭预审
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 1000,
        'discountAmount': 1000,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品特价（单品打折为1.5）开单,不送货,开启预审
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 4898,
        'discountAmount': 4896.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品不特价（单品打折为1.5）开单,不送货,开启预审
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 4898,
        'discountAmount': 4896.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品特价（单品打折为1.5）开单,不送货,关闭预审
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 4898,
        'discountAmount': 4896.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品不特价（单品打折为1.5）开单,不送货,关闭预审
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 4898,
        'discountAmount': 4896.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }

    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 套组商品特价
def billings_03():
    # 不参加活动， 套组商品特价（不打折）开单,不送货,开启预审
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 99, 'salePriceTotal': 99,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 0,
        'realAmount': 99,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品特价（不打折）开单,送货,关闭预审
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 99, 'salePriceTotal': 99,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 0,
        'realAmount': 99,
        'remark': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
        'orderDesc': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品特价（单品打折为0）开单,不送货,开启预审
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 99,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品不特价（单品打折为0）开单,不送货,开启预审
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 99,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品特价（单品打折为0）开单,不送货,关闭预审
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 99,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘套组test00244444444套",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品不特价（单品打折为0）开单,不送货,关闭预审
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 99,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品特价（单品打折为1.5）开单,不送货,开启预审
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品不特价（单品打折为1.5）开单,不送货,开启预审
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品特价（单品打折为1.5）开单,不送货,关闭预审
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品不特价（单品打折为1.5）开单,不送货,关闭预审
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }

    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 服务费特价
def billings_04():
    # 不参加活动， 服务费特价（不打折）开单,不送货,开启预审
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 2120, 'salePriceTotal': 2120,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 0,
        'realAmount': 2120,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "测试代销",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费特价（不打折）开单,送货,关闭预审
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 2120, 'salePriceTotal': 2120,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 0,
        'realAmount': 2120,
        'remark': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
        'orderDesc': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费特价（单品打折为0）开单,不送货,开启预审
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2120,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费不特价（单品打折为0）开单,不送货,开启预审
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2120,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费特价（单品打折为0）开单,不送货,关闭预审
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2120,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘套组test00244444444套",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费不特价（单品打折为0）开单,不送货,关闭预审
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2120,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费特价（单品打折为1.5）开单,不送货,开启预审
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2118.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费不特价（单品打折为1.5）开单,不送货,开启预审
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2118.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费特价（单品打折为1.5）开单,不送货,关闭预审
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2118.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费不特价（单品打折为1.5）开单,不送货,关闭预审
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2118.5,
        'realAmount': 1.5,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }

    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 普通商品整单打折
def billings_05():
    # 不参加活动， 普通商品(不特价）整单打折(1折）
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21, 'salePriceTotal': 21,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2100,
        'discountAmount': 2079,
        'realAmount': 21,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品(特价）整单打折(1折）
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21, 'salePriceTotal': 21,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2100,
        'discountAmount': 2079,
        'realAmount': 21,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品(不特价）整单打折(0折）
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2100,
        'discountAmount': 2100,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品(特价）整单打折(0折）
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2100,
        'discountAmount': 2100,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 普通商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68, 'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 168,
        'discountAmount': 166.32,
        'realAmount': 1.68,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 普通商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 168,
        'discountAmount': 166.32,
        'realAmount': 1.68,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 普通商品(不特价）整单打折(1.2折）开启预审，添加商品附件
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 168,
        'discountAmount': 166.32,
        'realAmount': 1.68,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 普通商品(不特价）整单打折(1.2折）开启预审，添加订单附件
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
             'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 168,
        'discountAmount': 166.32,
        'realAmount': 1.68,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 普通商品(特价）整单打折(1.2折）开启预审，添加商品附件
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 168,
        'discountAmount': 166.32,
        'realAmount': 1.68,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 普通商品(特价）整单打折(1.2折）开启预审，添加订单附件
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
             'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 168,
        'discountAmount': 166.32,
        'realAmount': 1.68,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 服务费整单打折
def billings_06():
    # 不参加活动， 服务费商品(不特价）整单打折(1折）
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 21.2, 'salePriceTotal': 21.2,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2098.8,
        'realAmount': 21.2,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费商品(特价）整单打折(1折）
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 21.2, 'salePriceTotal': 21.2,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2098.2,
        'realAmount': 21.2,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费商品(不特价）整单打折(0折）
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2100,
        'discountAmount': 2100,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费商品(特价）整单打折(0折）
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2100,
        'discountAmount': 2100,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 服务费商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2094.56,
        'realAmount': 25.44,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 服务费商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2094.56,
        'realAmount': 25.44,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 服务费商品(不特价）整单打折(1.2折）开启预审，添加商品附件
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2094.56,
        'realAmount': 25.44,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 服务费商品(不特价）整单打折(1.2折）开启预审，添加订单附件
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
             'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2094.56,
        'realAmount': 25.44,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 服务费商品(特价）整单打折(1.2折）开启预审，添加商品附件
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2094.56,
        'realAmount': 25.44,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 服务费商品(特价）整单打折(1.2折）开启预审，添加订单附件
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
             'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 2120,
        'discountAmount': 2094.56,
        'realAmount': 25.44,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
# 套组商品整单打折
def billings_07():
    # 不参加活动， 套组商品(不特价）整单打折(1折）
    billing_one = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 5800,
        'discountAmount': 5742,
        'realAmount': 58,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品(特价）整单打折(1折）
    billing_two = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 5800,
        'discountAmount': 5742,
        'realAmount': 58,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品(不特价）整单打折(0折）
    billing_three = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 5800,
        'discountAmount': 5800,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品(特价）整单打折(0折）
    billing_four = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "customizedImage", 'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 5800,
        'discountAmount': 5800,
        'realAmount': 0,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card()
    }
    # 不参加活动， 套组商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件
    billing_five = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.81,
        'realAmount': 1.19,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 套组商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件
    billing_six = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.81,
        'realAmount': 1.19,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 套组商品(不特价）整单打折(1.2折）开启预审，添加商品附件
    billing_seven = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.81,
        'realAmount': 1.19,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 套组商品(不特价）整单打折(1.2折）开启预审，添加订单附件
    billing_eight = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
             'isSpecialPrice': 'false', 'goodsClass': "SET"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.81,
        'realAmount': 1.19,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 套组商品(特价）整单打折(1.2折）开启预审，添加商品附件
    billing_nine = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
             'remark': "osjdfsjdkjdskjlksjlksf ",
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': ""},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.81,
        'realAmount': 1.19,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    # 不参加活动， 套组商品(特价）整单打折(1.2折）开启预审，添加订单附件
    billing_ten = {
        'orderType': "1003",
        'customId': iop.order_user()[0],
        'orderGoods': [
            {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
             'isSpecialPrice': 'true', 'goodsClass': "SET"}],
        'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                      {'key': "expectedCompleteDate", 'value': timeStamp},
                      {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                            'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                      {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
        'addressId': iop.order_address(),
        'originalAmount': 99,
        'discountAmount': 97.81,
        'realAmount': 1.19,
        'remark': "南阳全盘西门子灶具",
        'orderDesc': "南阳全盘西门子灶具",
        'customDTO': {'realName': iop.order_user()[1]},
        'memberCardInfoDTO': iop.order_card(),
        'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
    }
    return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten


def billings_08():
    # 不参加活动， 普通商品与服务费整单打折
    # 不参加活动， 普通商品与套组整单打折
    # 不参加活动， 服务费与套组整单打折
    # 不参加活动， 普通商品整单优惠
    # 不参加活动， 套组商品整单优惠
    # 不参加活动， 服务费整单优惠
    # 不参加活动， 普通商品与套组整单优惠
    # 不参加活动， 普通商品与服务费整单优惠
    # 不参加活动， 服务费与套组账单优惠
    return iop

