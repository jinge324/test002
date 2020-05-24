import xymways.test_case.test_order
import xymways.test_data.data_total
import datetime
import time

global iop, timeStamp, qwe
iop = xymways.test_case.test_order.Test_order()
timeStamp = xymways.test_data.data_total.time_obtain()
# timeStamp = xymways.test_data.data_total.time_obtain()
# 订单查询
class order_query():
    # 订单分页
    def paging(self):
        pageNo = 1
        pageSize = 100
        return pageNo, pageSize
    def order(self):
        # 老用户手机号
        oldnumber = '15871255250'
        # 开单时会员卡的选择
        card = '喜盈门会员卡'
        # 新用户数据
        newnumber = '12315151556'
        newname = '41afewa'
        return oldnumber, card, newnumber, newname

# 订单开单
class order_billing:
    # 异常开单
    def billings_01():
        # 开单不添加商品
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单送货，不添加地址
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': '',
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单不送货，添加地址
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 0},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单没有用户
        billing_four = {
            'orderType': "1003",
            'customId': '',
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单用户没有会员卡
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': ''
        }
        # 开单用户没有顾客姓名
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': '',
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单不填预计完成时间
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': ''},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单预计完成时间填今天之前
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1}, {'key': "expectedCompleteDate", 'value': 1557504000},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 开单商品是其它店铺的商品
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169348", 'orderQty': "1", 'marketPrice': 100, 'salePrice': 100, 'salePriceTotal': 100,
                 'isSpecialPrice': 'false', 'goodsClass': "COM"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 100,
            'discountAmount': 100,
            'realAmount': 100,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 修改开单商品的类型
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 商品特价类型不填/填错
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'fales', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        billing_twelev = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'fales', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelev
    # 正常开单
    def billings():
        # 不参加活动,不需送货，单个普通商品开单
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动,需送货，单个普通商品开单
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "2", 'marketPrice': 1000, 'salePrice': 1000, 'salePriceTotal': 2000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2000,
            'discountAmount': 0,
            'realAmount': 2000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动,不需送货，单个套组品开单
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动,不需送货，单个服务费用商商品开单
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动,多个普通商品开单
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动,多个套组商品开单
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"},
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动,多个服务费商品开单
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品与套组开单
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品与服务费开单
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组与服务开单
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 2000, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "超好吃唱个歌炒个菜",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 普通商品特价
    def billings_02():
        # 不参加活动， 普通商品特价（不打折）开单,不送货,开启预审
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 1000, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 0,
            'realAmount': 1000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品特价（不打折）开单,送货,关闭预审
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169350", 'orderQty': "1", 'marketPrice': 3333, 'salePrice': 3333, 'salePriceTotal': 3333,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2100, 'salePriceTotal': 2100,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 5433,
            'discountAmount': 0,
            'realAmount': 5433,
            'remark': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
            'orderDesc': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品特价（单品打折为0）开单,不送货,开启预审
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品不特价（单品打折为0）开单,不送货,开启预审
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品特价（单品打折为0）开单,不送货,关闭预审
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品不特价（单品打折为0）开单,不送货,关闭预审
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 2000, 'salePrice': 0, 'salePriceTotal': 1000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品特价（单品打折为1.5）开单,不送货,开启预审
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4898,
            'discountAmount': 4896.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品不特价（单品打折为1.5）开单,不送货,开启预审
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4898,
            'discountAmount': 4896.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品特价（单品打折为1.5）开单,不送货,关闭预审
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4898,
            'discountAmount': 4896.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品不特价（单品打折为1.5）开单,不送货,关闭预审
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169316", 'orderQty': "1", 'marketPrice': 4898, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4898,
            'discountAmount': 4896.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }

        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 套组商品特价
    def billings_03():
        # 不参加活动， 套组商品特价（不打折）开单,不送货,开启预审
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 99, 'salePriceTotal': 99,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 0,
            'realAmount': 99,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品特价（不打折）开单,送货,关闭预审
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 99, 'salePriceTotal': 99,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 0,
            'realAmount': 99,
            'remark': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
            'orderDesc': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品特价（单品打折为0）开单,不送货,开启预审
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 99,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品不特价（单品打折为0）开单,不送货,开启预审
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 99,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品特价（单品打折为0）开单,不送货,关闭预审
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169290", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 99,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘套组test00244444444套",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品不特价（单品打折为0）开单,不送货,关闭预审
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 0, 'salePriceTotal': 99,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 99,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品特价（单品打折为1.5）开单,不送货,开启预审
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品不特价（单品打折为1.5）开单,不送货,开启预审
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品特价（单品打折为1.5）开单,不送货,关闭预审
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品不特价（单品打折为1.5）开单,不送货,关闭预审
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }

        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 服务费特价
    def billings_04():
        # 不参加活动， 服务费特价（不打折）开单,不送货,开启预审
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 2120, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 0,
            'realAmount': 2120,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "测试代销",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费特价（不打折）开单,送货,关闭预审
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 2120, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 0,
            'realAmount': 2120,
            'remark': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
            'orderDesc': "南阳全盘TOTO浴缸1可乐无缝结合浴缸超大容量吃的 等",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费特价（单品打折为0）开单,不送货,开启预审
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费不特价（单品打折为0）开单,不送货,开启预审
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费特价（单品打折为0）开单,不送货,关闭预审
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘套组test00244444444套",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费不特价（单品打折为0）开单,不送货,关闭预审
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 2120,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费特价（单品打折为1.5）开单,不送货,开启预审
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2118.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费不特价（单品打折为1.5）开单,不送货,开启预审
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2118.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费特价（单品打折为1.5）开单,不送货,关闭预审
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2118.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费不特价（单品打折为1.5）开单,不送货,关闭预审
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.5, 'salePriceTotal': 1.5,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 0}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2118.5,
            'realAmount': 1.5,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }

        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 普通商品整单打折
    def billings_05():
        # 不参加活动， 普通商品(不特价）整单打折(1折）
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21, 'salePriceTotal': 21,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2100,
            'discountAmount': 2079,
            'realAmount': 21,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品(特价）整单打折(1折）
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21, 'salePriceTotal': 21,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2100,
            'discountAmount': 2079,
            'realAmount': 21,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品(不特价）整单打折(0折）
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2100,
            'discountAmount': 2100,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品(特价）整单打折(0折）
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2100,
            'discountAmount': 2100,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 普通商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 168,
            'discountAmount': 166.32,
            'realAmount': 1.68,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 普通商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 168,
            'discountAmount': 166.32,
            'realAmount': 1.68,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 普通商品(不特价）整单打折(1.2折）开启预审，添加商品附件
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 168,
            'discountAmount': 166.32,
            'realAmount': 1.68,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 普通商品(不特价）整单打折(1.2折）开启预审，添加订单附件
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 168,
            'discountAmount': 166.32,
            'realAmount': 1.68,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 普通商品(特价）整单打折(1.2折）开启预审，添加商品附件
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 168,
            'discountAmount': 166.32,
            'realAmount': 1.68,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 普通商品(特价）整单打折(1.2折）开启预审，添加订单附件
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169312", 'orderQty': "1", 'marketPrice': 168, 'salePrice': 1.68, 'salePriceTotal': 1.68,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 168,
            'discountAmount': 166.32,
            'realAmount': 1.68,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 服务费整单打折
    def billings_06():
        # 不参加活动， 服务费商品(不特价）整单打折(1折）
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 21.2, 'salePriceTotal': 21.2,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2098.8,
            'realAmount': 21.2,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费商品(特价）整单打折(1折）
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 21.2, 'salePriceTotal': 21.2,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2098.2,
            'realAmount': 21.2,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费商品(不特价）整单打折(0折）
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2100,
            'discountAmount': 2100,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费商品(特价）整单打折(0折）
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2100,
            'discountAmount': 2100,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 服务费商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2094.56,
            'realAmount': 25.44,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 服务费商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2094.56,
            'realAmount': 25.44,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 服务费商品(不特价）整单打折(1.2折）开启预审，添加商品附件
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2094.56,
            'realAmount': 25.44,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 服务费商品(不特价）整单打折(1.2折）开启预审，添加订单附件
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2094.56,
            'realAmount': 25.44,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 服务费商品(特价）整单打折(1.2折）开启预审，添加商品附件
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2094.56,
            'realAmount': 25.44,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 服务费商品(特价）整单打折(1.2折）开启预审，添加订单附件
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 25.44, 'salePriceTotal': 25.44,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2094.56,
            'realAmount': 25.44,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 套组商品整单打折
    def billings_07():
        # 不参加活动， 套组商品(不特价）整单打折(1折）
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 5800,
            'discountAmount': 5742,
            'realAmount': 58,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品(特价）整单打折(1折）
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 5800,
            'discountAmount': 5742,
            'realAmount': 58,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品(不特价）整单打折(0折）
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 5800,
            'discountAmount': 5800,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品(特价）整单打折(0折）
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "customizedImage", 'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 5800,
            'discountAmount': 5800,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card()
        }
        # 不参加活动， 套组商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.81,
            'realAmount': 1.19,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 套组商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.81,
            'realAmount': 1.19,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 套组商品(不特价）整单打折(1.2折）开启预审，添加商品附件
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.81,
            'realAmount': 1.19,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 套组商品(不特价）整单打折(1.2折）开启预审，添加订单附件
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.81,
            'realAmount': 1.19,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 套组商品(特价）整单打折(1.2折）开启预审，添加商品附件
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'remark': "osjdfsjdkjdskjlksjlksf ",
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': ""},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.81,
            'realAmount': 1.19,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动， 套组商品(特价）整单打折(1.2折）开启预审，添加订单附件
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182868", 'orderQty': "1", 'marketPrice': 99, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 99,
            'discountAmount': 97.81,
            'realAmount': 1.19,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 普通商品与服务费整单打折
    def billings_08():
        # 不参加活动，商品都特价，整单打折1
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0.5, 'salePriceTotal': 0.5,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}, {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 1953,
            'realAmount': 217,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折1
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0.5, 'salePriceTotal': 0.5,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 1953,
            'realAmount': 217,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都特价，整单打折0
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都特价，整单打折1000
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折1000
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折0
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，普通特价，整单打折0
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，服务特价，整单打折0
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，服务特价，整单打折1000
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，普通特价，整单打折1000
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 21700,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，普通特价，整单打折1
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 1,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，服务特价，整单打折1
        billing_twelve = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 1,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelve
    # 普通商品与套组整单打折
    def billings_09():
        # 不参加活动，商品都特价，整单打折1
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0.5, 'salePriceTotal': 0.5,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 1953,
            'realAmount': 217,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折1
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0.5, 'salePriceTotal': 0.5,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 1953,
            'realAmount': 217,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都特价，整单打折0
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都特价，整单打折1000
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折1000
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折0
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，普通特价，整单打折0
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，套组特价，整单打折0
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'ture', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，套组特价，整单打折1000
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，普通特价，整单打折1000
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 21700,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，普通特价，整单打折1
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 1,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，套组特价，整单打折1
        billing_twelve = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169256", 'orderQty': "1", 'marketPrice': 50, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 1,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelve
    # 服务费与套组整单打折
    def billings_10():
        # 不参加活动，商品都特价，整单打折1
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 1953,
            'realAmount': 217,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都不特价，整单打折1
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 1953,
            'realAmount': 217,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，商品都特价，整单打折0
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0'}]
        }
        # 不参加活动，商品都特价，整单打折1000
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '1000'}]
        }
        # 不参加活动，商品都不特价，整单打折1000
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '1000'}]
        }
        # 不参加活动，商品都不特价，整单打折0
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0'}]
        }
        # 不参加活动，服务费特价，整单打折0
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0'}]
        }
        # 不参加活动，套组特价，整单打折0
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'ture', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -2170,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0'}]
        }
        # 不参加活动，套组特价，整单打折1000
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 2170,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '1000'}]
        }
        # 不参加活动，服务费特价，整单打折1000
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 10}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': -19530,
            'realAmount': 21700,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '1000'}]
        }
        # 不参加活动，服务费特价，整单打折1
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 1,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        # 不参加活动，套组特价，整单打折1
        billing_twelve = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 1.19, 'salePriceTotal': 1.19,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58, 'salePriceTotal': 58,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "discount", 'value': 0.1}, {'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2170,
            'discountAmount': 2170,
            'realAmount': 1,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "3000", 'preferenVal': '0.1'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelve
    # 普通商品整单优惠
    def billings_11():
        # 商品整单优惠到789， 商品不特价
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 211,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 商品整单优惠到789， 商品特价
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 211,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 商品整单优惠到0， 商品不特价
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '0'}]
        }
        # 商品整单优惠到0， 商品特价
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '0'}]
        }
        # 商品整单优惠到比原价大， 商品不特价
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 10000000, 'salePriceTotal': 10000000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 10000000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '10000000'}]
        }
        # 商品整单优惠到比原价大， 商品特价
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 10000000, 'salePriceTotal': 10000000,
                 'isSpecialPrice': 'ture', 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 10000000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '10000000'}]
        }
        # 商品整单优惠到789， 商品不特价, 添加大于限制的商品备注
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa", 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 211,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 商品整单优惠到789， 商品不特价, 添加正常的商品备注
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 211,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 商品整单优惠orderPreferens，为空
        billing_nine = {
             'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 211,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': []
        }
        # 商品整单优惠不传orderPreferens
        billing_ten = {
             'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169284", 'orderQty': "1", 'marketPrice': 1000, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "COMMON"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 211,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            # 'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }

        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 套组商品整单优惠
    def billings_12():
        # 套组整单优惠到789， 商品不特价
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 3311,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 套组整单优惠到789， 商品特价
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 3311,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 套组整单优惠到0， 商品不特价
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 4100,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '0'}]
        }
        # 套组整单优惠到0， 商品特价
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 4100,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '0'}]
        }
        # 套组整单优惠到比原价大， 商品不特价
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 10000000,
                 'salePriceTotal': 10000000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 4100,
            'realAmount': 10000000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '10000000'}]
        }
        # 套组整单优惠到比原价大， 商品特价
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 10000000,
                 'salePriceTotal': 10000000,
                 'isSpecialPrice': 'ture', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 1000,
            'discountAmount': 1000,
            'realAmount': 10000000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '10000000'}]
        }
        # 套组整单优惠到789， 商品不特价, 添加大于限制的商品备注
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false',
                 'remark': "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa",
                 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 3311,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 套组整单优惠到789， 商品不特价, 添加正常的商品备注
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 3311,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 套组整单优惠orderPreferens，为空
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 3311,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': []
        }
        # 套组整单优惠不传orderPreferens
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182873", 'orderQty': "1", 'marketPrice': 4100, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 4100,
            'discountAmount': 3311,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            # 'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }

        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 服务费整单优惠
    def billings_13():
        # 服务费整单优惠到789， 商品不特价
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 1331,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 服务费整单优惠到789， 商品特价
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 1331,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 服务费整单优惠到0， 商品不特价
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '0'}]
        }
        # 服务费整单优惠到0， 商品特价
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '0'}]
        }
        # 服务费整单优惠到比原价大， 商品不特价
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 10000000,
                 'salePriceTotal': 10000000,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 10000000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '10000000'}]
        }
        # 服务费整单优惠到比原价大， 商品特价
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 10000000,
                 'salePriceTotal': 10000000,
                 'isSpecialPrice': 'ture', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 2120,
            'realAmount': 10000000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '10000000'}]
        }
        # 服务费整单优惠到789， 商品不特价, 添加大于限制的商品备注
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false',
                 'remark': "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa",
                 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 1331,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 服务费整单优惠到789， 商品不特价, 添加正常的商品备注
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 1331,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }
        # 服务费整单优惠orderPreferens，为空
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 1331,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': []
        }
        # 服务费整单优惠不传orderPreferens
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'remark': "ssssss", 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 2120,
            'discountAmount': 1331,
            'realAmount': 789,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            # 'orderPreferens': [{'preferenType': "2000", 'preferenVal': '789'}]
        }

        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten
    # 普通商品与套组整单优惠
    def billings_14():
        # 不参加活动，商品都特价，整单优惠到10
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2.66, 'salePriceTotal': 2.66,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 7.34, 'salePriceTotal': 7.34,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，商品都不特价，整单优惠到10
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2.66, 'salePriceTotal': 2.66,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 7.34, 'salePriceTotal': 7.34,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，商品都特价，整单优惠到0
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，商品都特价，整单优惠到100000
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21000, 'salePriceTotal': 21000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58000, 'salePriceTotal': 58000,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，商品都不特价，整单优惠到100000
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21000, 'salePriceTotal': 21000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58000, 'salePriceTotal': 58000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，商品都不特价，整单优惠到0
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，普通特价，整单优惠到0
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'ture', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，套组特价，整单优惠到0
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'ture', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，套组特价，整单优惠到10000
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2100, 'salePriceTotal': 2100,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58000, 'salePriceTotal': 58000,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，普通特价，整单优惠到1000
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21000, 'salePriceTotal': 21000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 5800, 'salePriceTotal': 5800,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，普通特价，整单优惠到10
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2100, 'salePriceTotal': 2100,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': -2090, 'salePriceTotal': -2090,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，套组特价，整单优惠到10
        billing_twelve = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': '-5700', 'salePriceTotal': '-5700',
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 5800, 'salePriceTotal': 5800,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelve
    # 普通商品与服务费整单优惠
    def billings_15():
        # 不参加活动，商品都特价，整单优惠到10
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2.66, 'salePriceTotal': 2.66,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，商品都不特价，整单优惠到10
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2.66, 'salePriceTotal': 2.66,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，商品都特价，整单优惠到0
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，商品都特价，整单优惠到100000
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21000, 'salePriceTotal': 21000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，商品都不特价，整单优惠到100000
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21000, 'salePriceTotal': 21000,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，商品都不特价，整单优惠到0
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}
            ],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，普通特价，整单优惠到0
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'ture', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，服务费特价，整单优惠到0
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，服务费特价，整单优惠到10000
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2100, 'salePriceTotal': 2100,
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，普通特价，整单优惠到1000
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 21000, 'salePriceTotal': 21000,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，普通特价，整单优惠到10
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': 2100, 'salePriceTotal': 2100,
                 'isSpecialPrice': 'true', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，服务费特价，整单优惠到10
        billing_twelve = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "169286", 'orderQty': "1", 'marketPrice': 2100, 'salePrice': '-5700', 'salePriceTotal': '-5700',
                 'isSpecialPrice': 'false', 'goodsClass': "COMMON"},
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelve
    # 服务费与套组账单优惠
    def billings_16():
        # 不参加活动，商品都特价，整单优惠到10
        billing_one = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 7.34, 'salePriceTotal': 7.34,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，商品都不特价，整单优惠到10
        billing_two = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 7.34, 'salePriceTotal': 7.34,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，商品都特价，整单优惠到0
        billing_three = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，商品都特价，整单优惠到100000
        billing_four = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58000, 'salePriceTotal': 58000,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，商品都不特价，整单优惠到100000
        billing_five = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58000, 'salePriceTotal': 58000,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，商品都不特价，整单优惠到0
        billing_six = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，服务费特价，整单优惠到0
        billing_seven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，套组特价，整单优惠到0
        billing_eight = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 0, 'salePriceTotal': 0,
                 'isSpecialPrice': 'ture', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 0,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '0'}]
        }
        # 不参加活动，套组特价，整单优惠到10000
        billing_nine = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 58000, 'salePriceTotal': 58000,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，服务费特价，整单优惠到1000
        billing_ten = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 5800, 'salePriceTotal': 5800,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7900,
            'realAmount': 10000,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10000'}]
        }
        # 不参加活动，服务费特价，整单优惠到10
        billing_eleven = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'true', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': -2090, 'salePriceTotal': -2090,
                 'isSpecialPrice': 'false', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        # 不参加活动，套组特价，整单优惠到10
        billing_twelve = {
            'orderType': "1003",
            'customId': iop.test_order_user()[0],
            'orderGoods': [
                {'goodsId': "182889", 'orderQty': "1", 'marketPrice': 2120, 'salePrice': 789, 'salePriceTotal': 789,
                 'isSpecialPrice': 'false', 'goodsClass': "SERVICE_FEE"},
                {'goodsId': "182867", 'orderQty': "1", 'marketPrice': 5800, 'salePrice': 5800, 'salePriceTotal': 5800,
                 'isSpecialPrice': 'true', 'goodsClass': "SET"}],
            'orderExts': [{'key': "needDelivery", 'value': 1},
                          {'key': "expectedCompleteDate", 'value': timeStamp.time_stamp()},
                          {'key': "orderInvoice", 'value': 1}, {'key': "customizedImage",
                                                                'value': "order/attach/66/4284/5630/20200518/4047af48-9f23-9cbe-7303-5dcf49ef6725"},
                          {'key': "addDesignerFriend", 'value': 0}, {'key': "preliminaryAuditFlag", 'value': 1}],
            'addressId': iop.test_order_address(),
            'originalAmount': 7900,
            'discountAmount': 7890,
            'realAmount': 10,
            'remark': "南阳全盘西门子灶具",
            'orderDesc': "南阳全盘西门子灶具",
            'customDTO': {'realName': iop.test_order_user()[1]},
            'memberCardInfoDTO': iop.test_order_card(),
            'orderPreferens': [{'preferenType': "200", 'preferenVal': '10'}]
        }
        return billing_one, billing_two, billing_three, billing_four, billing_five, billing_six, billing_seven, billing_eight, billing_nine, billing_ten, billing_eleven, billing_twelve

