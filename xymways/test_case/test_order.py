import json
from xymways.test_method.reques_Interface import runmain
from xymways.test_data.data_total import header_merchant
from xymways.test_data.data_total import time_obtain
import xymways.test_data.data_order


global saleStartTime, saleEndTime, run
ordertime = time_obtain()
saleStartTime = ordertime.time_YMD()[0]
saleEndTime = ordertime.time_YMD()[1]
run = runmain()
class Test_order():
    # 开单老用户查询
    def test_order_user(self):
        global customid
        useru = 'http://api.xymtest.com/merchant/store/order/manage/get/custom/info?mobile='
        userr = xymways.test_data.data_order.order_query().order()[0]
        useeurl = useru + userr
        orderuser = run.run_main(useeurl, 'GET', header_merchant)
        assert orderuser['code'] == 200
        # print(orderuser)
        customid = orderuser['data'][0]['custId']
        realName = orderuser['data'][0]['realName']
        pan = orderuser['data']
        # print('顾客custid:', customid)
        return customid, realName, pan
    # 查询到开单老用户的地址
    def test_order_address(self):
        addressu = 'http://api.xymtest.com/merchant/store/order/open/distribution?customId='
        addressr = json.dumps(customid)
        addressurl = addressu + addressr
        orderaddress = run.run_main(addressurl, 'POST', header_merchant)
        assert orderaddress['code'] != 500
        # print('顾客地址：', orderaddress)
        address = orderaddress['data']['address'][0]['addId']
        return address
    # 查询开单用户会员卡
    def test_order_card(self):
        global cardid, cardtype
        cardu = 'http://api.xymtest.com/merchant/custom/member/card/query/list?customId='
        cardr = json.dumps(customid)
        cardl = '&orderId='
        cardurl = cardu + cardr + cardl
        ordercard = run.run_main(cardurl, 'GET', header_merchant)
        assert ordercard['code'] != 500
        # print(ordercard)
        # 根据需要的联名卡来进行返回参数
        membershipcard = ordercard['data']
        for cardId in membershipcard:
            if cardId['cardName'] == xymways.test_data.data_order.order_query().order()[1]:
                cardid = cardId['cardId']
                cardtype = cardId['cardType']
                # print('顾客会员卡customId:', cardid, '\n顾客会员卡类型：', cardtype)
                break
        return cardId
    # 查询所关联的活动
    def test_activities(self):
        activitiesu = 'http://api.xymtest.com/merchant/store/order/manage/activity/list?customId=' + json.dumps(
                customid)
        activitiesr = '&cardId=' + cardid
        activitiesl = '&cardType=' + cardtype
        activitiesurl = activitiesu + activitiesr + activitiesl
        # print(activitiesurl)
        activitiesorder = run.run_main(activitiesurl, 'GET', header_merchant)
        # print(activitiesorder)
        assert activitiesorder['code'] != 500
        return activitiesorder

# 开单
class Test_Billings():
    # '''
    # 异常开单
    def test_prequalification_001(self):
        print('001不添加商品顾客开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        print(prequalificationorder)
        assert prequalificationorder['message'] == '订单至少包含一件商品'
        return prequalificationorder
    def test_prequalification_002(self):
        print('002开单商品收货，但不填写收货地址')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        print(prequalificationorder)
        assert prequalificationorder['message'] == '请添加送货地址'
        return prequalificationorder
    def test_prequalification_003(self):
        print('003开单不收货，单填写收货地址')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        assert prequalificationorder['code'] == 200
        print(prequalificationorder)
        return prequalificationorder
    def test_prequalification_004(self):
        print('004没有用户开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast='请填写购货人信息', passvalue=prequalificationorder['message'])
        print(prequalificationorder)
        assert prequalificationorder['message'] == '请填写购货人信息'
        return prequalificationorder
    def test_prequalification_005(self):
        print('005用户没有会员卡开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast='请选择会员卡', passvalue=prequalificationorder['message'])
        print(prequalificationorder)
        assert prequalificationorder['message'] == '请选择会员卡'
        return prequalificationorder
    def test_prequalification_006(self):
        print('006开单用户没有顾客姓名')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast='请填写顾客姓名', passvalue=prequalificationorder['message'])
        print(prequalificationorder)
        assert prequalificationorder['message'] == '请填写顾客姓名'
        return prequalificationorder
    def test_prequalification_007(self):
        print('007开单不填预计完成时间')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast='订单预计完成时间不可为空', passvalue=prequalificationorder['message'])
        print(prequalificationorder)
        assert prequalificationorder['message'] == '订单预计完成时间不可为空'
        return prequalificationorder
    def test_prequalification_008(self):
        print('008开单预计完成时间填今天之前')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast='订单预计完成时间需今天或以后', passvalue=prequalificationorder['message'])
        print(prequalificationorder)
        assert prequalificationorder['message'] == '订单预计完成时间需今天或以后'
        return prequalificationorder
    def test_prequalification_009(self):
        print('009订单用其它店铺商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=500, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 500
        return prequalificationorder
    def test_prequalification_010(self):
        print('010订单商品类型不一致开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=500, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_011(self):
        print('010订单商品类型不一致开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=500, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 500
        return prequalificationorder
    def test_prequalification_012(self):
        print('010订单商品类型不一致开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_01()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=500, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 500
        return prequalificationorder
    # 正常开单
    def test_prequalification_01(self):
        print('不参加活动,不需送货，单个普通商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_02(self):
        print('不参加活动,需送货，单个普通商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_03(self):
        print('不参加活动,不需送货，单个套组品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_04(self):
        print('不参加活动,不需送货，单个服务费用商商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_05(self):
        print('不参加活动,多个普通商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_06(self):
        print('不参加活动,多个套组商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_07(self):
        print('不参加活动,多个服务费商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_08(self):
        print('不参加活动， 普通商品与套组开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_09(self):
        print('不参加活动， 普通商品与服务费开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_10(self):
        print('不参加活动， 套组与服务开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 订单特价开单
    # 普通商品
    def test_prequalification_11(self):
        print('普通商品特价（不打折）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_12(self):
        print('普通商品特价（不打折）开单,送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_13(self):
        print('普通商品特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_14(self):
        print('普通商品不特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_15(self):
        print('普通商品特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_16(self):
        print('普通商品不特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_17(self):
        print('普通商品特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_18(self):
        print('普通商品不特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_19(self):
        print('不普通商品特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_20(self):
        print('普通商品不特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_02()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 套组
    def test_prequalification_21(self):
        print('套组商品特价（不打折）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_22(self):
        print('套组商品特价（不打折）开单,送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_23(self):
        print('套组商品特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_24(self):
        print('套组商品不特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_25(self):
        print('套组商品特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_26(self):
        print('套组商品不特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_27(self):
        print('套组商品特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_28(self):
        print('套组商品不特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_29(self):
        print('套组商品特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_30(self):
        print('套组商品不特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_03()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 服务费用
    def test_prequalification_31(self):
        print('服务费特价（不打折）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_32(self):
        print('服务费特价（不打折）开单,送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_33(self):
        print('服务费特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_34(self):
        print('服务费不特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_35(self):
        print('服务费特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_36(self):
        print('服务费不特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_37(self):
        print('服务费特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_38(self):
        print('服务费不特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_39(self):
        print('服务费特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_40(self):
        print('服务费不特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 普通商品整单打折
    def test_prequalification_41(self):
        print('普通商品(不特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_42(self):
        print('普通商品(特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_43(self):
        print('普通商品(不特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_44(self):
        print('普通商品(特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_45(self):
        print('普通商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        # print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_46(self):
        print('普通商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_47(self):
        print('普通商品(不特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_48(self):
        print('普通商品(不特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_49(self):
        print('普通商品(特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_50(self):
        print('普通商品(特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_05()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    #  服务费整单打折
    def test_prequalification_51(self):
        print('服务费商品(不特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_06()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_52(self):
        print('服务费商品(特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_06()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        # print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_53(self):
        print('服务费商品(不特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_54(self):
        print('服务费商品(特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_55(self):
        print('服务费商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_56(self):
        print('服务费商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_57(self):
        print('服务费商品(不特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_58(self):
        print('服务费商品(不特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_59(self):
        print('服务费商品(特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_60(self):
        print('服务费商品(特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 套组商品整单打折
    def test_prequalification_61(self):
        print('不参加活动， 套组商品(不特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_62(self):
        print('不参加活动， 套组商品(特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        # print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_63(self):
        print('套组商品(不特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_64(self):
        print('套组商品(特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_65(self):
        print('套组商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_66(self):
        print('套组商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_67(self):
        print('套组商品(不特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_68(self):
        print('套组商品(不特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_69(self):
        print('套组商品(特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_70(self):
        print('套组商品(特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_07()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 普通商品与服务费整单打折
    def test_prequalification_71(self):
        print('不参加活动，商品都特价，整单打折1')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_72(self):
        print('不参加活动，商品都不特价，整单打折1')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_73(self):
        print('不参加活动，商品都特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_74(self):
        print('不参加活动，商品都特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_75(self):
        print('不参加活动，商品都不特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_76(self):
        print('不参加活动，商品都不特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_77(self):
        print('不参加活动，普通特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_78(self):
        print('不参加活动，服务特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_79(self):
        print('不参加活动，服务特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_80(self):
        print('不参加活动，普通特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_81(self):
        print('不参加活动，服务特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_82(self):
        print('不参加活动，普通特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_08()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder

    # 普通商品与套组整单打折
    def test_prequalification_83(self):
        print('不参加活动，商品都特价，整单打折1')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_84(self):
        print('不参加活动，商品都不特价，整单打折1')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_85(self):
        print('不参加活动，商品都特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_86(self):
        print('不参加活动，商品都特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_87(self):
        print('不参加活动，商品都不特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_88(self):
        print('不参加活动，商品都不特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_89(self):
        print('不参加活动，普通特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_90(self):
        print('不参加活动，套组特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_91(self):
        print('不参加活动，套组特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_92(self):
        print('不参加活动，普通特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_93(self):
        print('不参加活动，服务特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_94(self):
        print('不参加活动，普通特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_09()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    # 服务费与套组整单打折
    def test_prequalification_95(self):
        print('不参加活动，商品都特价，整单打折1')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_96(self):
        print('不参加活动，商品都不特价，整单打折1')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_97(self):
        print('不参加活动，商品都特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_98(self):
        print('不参加活动，商品都特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_99(self):
        print('不参加活动，商品都不特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_100(self):
        print('不参加活动，商品都不特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_101(self):
        print('不参加活动，服务费特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_102(self):
        print('不参加活动，套组特价，整单打折0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_103(self):
        print('不参加活动，套组用特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_104(self):
        print('不参加活动，服务费特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_105(self):
        print('不参加活动，服务特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_106(self):
        print('不参加活动，服务费用特价，整单打折1000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_10()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    # 普通商品整单优惠
    def test_prequalification_107(self):
        print('商品整单优惠到789， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_108(self):
        print('商品整单优惠到789， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_109(self):
        print('商品整单优惠到0， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_110(self):
        print('商品整单优惠到0， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_111(self):
        print('商品整单优惠到比原价大， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_112(self):
        print('商品整单优惠到比原价大， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_113(self):
        print('商品整单优惠到789， 商品不特价, 添加大于限制的商品备注')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_114(self):
        print('商品整单优惠到789， 商品不特价, 添加正常的商品备注')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_115(self):
        print('商品整单优惠orderPreferens，为空')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_116(self):
        print('商品整单优惠不传orderPreferens')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_11()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder

    # 套组商品整单优惠
    def test_prequalification_117(self):
        print('套组商品整单优惠到789， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_118(self):
        print('套组商品整单优惠到789， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_119(self):
        print('套组商品整单优惠到0， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_120(self):
        print('套组商品整单优惠到0， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_121(self):
        print('套组商品整单优惠到比原价大， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_122(self):
        print('套组商品整单优惠到比原价大， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_123(self):
        print('套组商品整单优惠到789， 商品不特价, 添加大于限制的商品备注')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_124(self):
        print('套组商品整单优惠到789， 商品不特价, 添加正常的商品备注')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_125(self):
        print('套组商品整单优惠orderPreferens，为空')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_126(self):
        print('套组商品整单优惠不传orderPreferens')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_12()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder

    # 服务费商品整单优惠
    def test_prequalification_127(self):
        print('套组整单优惠到789， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_128(self):
        print('服务费整单优惠到789， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_129(self):
        print('服务费商品整单优惠到0， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_130(self):
        print('服务费商品整单优惠到0， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_131(self):
        print('服务费商品整单优惠到比原价大， 商品不特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_132(self):
        print('服务费商品整单优惠到比原价大， 商品特价')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_133(self):
        print('服务费商品整单优惠到789， 商品不特价, 添加大于限制的商品备注')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_134(self):
        print('服务费商品整单优惠到789， 商品不特价, 添加正常的商品备注')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_135(self):
        print('服务费商品整单优惠orderPreferens，为空')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_136(self):
        print('服务费商品整单优惠不传orderPreferens')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_13()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder

    # 普通商品与套组整单优惠
    def test_prequalification_137(self):
        print('不参加活动，商品都特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_138(self):
        print('不参加活动，商品都不特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_139(self):
        print('不参加活动，商品都特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_140(self):
        print('不参加活动，商品都特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_141(self):
        print('不参加活动，商品都不特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_142(self):
        print('不参加活动，商品都不特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_143(self):
        print('不参加活动，普通特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_144(self):
        print('不参加活动，套组特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_145(self):
        print('不参加活动，套组特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_146(self):
        print('不参加活动，普通特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_147(self):
        print('不参加活动，套组特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_148(self):
        print('不参加活动，普通特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_14()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    # '''
    # 普通商品与服务费整单优惠
    def test_prequalification_149(self):
        print('不参加活动，商品都特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_150(self):
        print('不参加活动，商品都不特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_151(self):
        print('不参加活动，商品都特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_152(self):
        print('不参加活动，商品都特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_153(self):
        print('不参加活动，商品都不特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_154(self):
        print('不参加活动，商品都不特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_155(self):
        print('不参加活动，普通特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_156(self):
        print('不参加活动，服务费特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_157(self):
        print('不参加活动，服务费特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_158(self):
        print('不参加活动，普通特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_159(self):
        print('不参加活动，服务费特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_160(self):
        print('不参加活动，普通特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_15()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder

    # 服务费与套组账单优惠
    def test_prequalification_161(self):
        print('不参加活动，商品都特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_162(self):
        print('不参加活动，商品都不特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_163(self):
        print('不参加活动，商品都特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_164(self):
        print('不参加活动，商品都特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def test_prequalification_165(self):
        print('不参加活动，商品都不特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_166(self):
        print('不参加活动，商品都不特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 251000010
        return prequalificationorder
    def test_prequalification_167(self):
        print('不参加活动，服务费特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_168(self):
        print('不参加活动，套组特价，整单优惠到0')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] != 200
        return prequalificationorder
    def test_prequalification_169(self):
        print('不参加活动，套组特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_170(self):
        print('不参加活动，服务费特价，整单优惠到10000')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_171(self):
        print('不参加活动，套组特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[10]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def test_prequalification_172(self):
        print('不参加活动，服务为特价，整单优惠到10')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xymways.test_data.data_order.order_billing.billings_16()[11]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', header_merchant,
                                             json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder


# 订单查询
# 商户订单查询
class Test_order_query():
    # 查询商户全部订单
    def test_query_order(self):
        global paging
        paging = xymways.test_data.data_order.order_query().paging()
        print('测试查询商户全部订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=3000,3005,4000,4001,5000,6000,8000,9000,9001,9002,9003,9004,9999'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] == 200
        # print(run.run_main(queryorderurl, 'POST', header_merchant))
        print(len(queryorder))
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        print(ordernos)
        return ordernos
    # 查询商户待支付订单
    def test_query_order_tbpaid(self):
        print('测试查询商户待支付订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=3000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        print(len(queryorder))
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        print(ordernos)
        return ordernos
    # '''
    # 查询商户待预审订单
    def test_query_order_tbprequal(self):
        print('测试查询商户待预审订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=3005'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
            # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户顾客签名订单
    def test_query_order_customeraut(self):
        print('测试查询商户顾客签名订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=4000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
            # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户商户待签名订单
    def test_query_order_merchantaut(self):
        print('测试查询商户商户待签名订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=4001'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
            # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待完成订单
    def test_query_order_tbcompleted(self):
        print('测试查询商户待完成订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=5000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户已完成订单
    def test_query_orde_completed(self):
        print('测试查询商户全部订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=6000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
            # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户已退货订单
    def test_query_order_returned(self):
        print('测试查询商户已退货订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=8000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待审核订单
    def test_query_order_tbreviewed(self):
        print('测试查询商户待审核订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户审核不通过订单
    def test_query_order_auditfailed(self):
        print('测试查询商户审核不通过订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9001'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户修改订单顾客待确认订单
    def test_query_order_modifycustomer(self):
        print('测试查询商户修改订单顾客待确认订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9002'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待支付订单
    def test_query_order_modifymerchant(self):
        print('测试查询商户待支付订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9003'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
            # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户修改订单顾客待确认订单
    def test_query_order_passprequal(self):
        print('测试查询商户预审审核不通过订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9004'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
        # print(len(queryorder), queryorder[0]['orderNo'])
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户已退单订单
    def test_query_order_chargeback(self):
        """百度搜索接口"""
        print('测试查询商户已退单订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(paging[0]) + '&pageSize=' + json.dumps(paging[1]) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9999'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', header_merchant)['data']['list']
            # print(len(queryorder), queryorder[0]['orderNo'])
        assert run.run_main(queryorderurl, 'POST', header_merchant)['code'] != 500
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # '''
    # 取消商户全部待支付订单(时间段之内)
    def test_paid(self):
        iop = Test_order_query().test_query_order_tbpaid()
        # print(iop)
        # print(len(iop))
        for i in range(0, len(iop)):
            tobepaidu = 'http://api.xymtest.com/merchant/store/order/manage/cancel?orderNo='
            tobepaidr = iop[i]
            tobepaidurl = tobepaidu + tobepaidr
            tobepaidorde = run.run_main(tobepaidurl, 'POST', header_merchant)
            assert tobepaidorde['code'] != 500
