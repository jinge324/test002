import json
import xym.request.myrequests
import xym.request.assertion
import xym.test_cases.test_fee_data.fee_one_data
import xym.test_cases.test_fee_data.fee_order_data
import datetime
import time
import unittest
import HTMLTestRunner
import HTMLTestRunnerCN


global run, headers, assertion, onedata
# 先实例化，然后再去调用run_main
run = xym.request.myrequests.RunMain()
assertion = xym.request.assertion
headers = xym.test_cases.test_fee_data.fee_one_data.headers
onedata = xym.test_cases.test_fee_data.fee_one_data

# 商场商户对订单是否需要审核
class authority(unittest.TestSuite):
    # 开启订单商场审核
    def order_qpproval_authority_01(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'true',
            'openPreAudit': 'false',
            'skipAfterPreAudit': 'false',
            'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        print(ress)
        assert ress['code'] == 200
        assertion.assertions(self, contrast=200, passvalue=ress['code'])

    # 开启订单商场预审
    def order_qpproval_authority_02(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'false',
            'openPreAudit': 'true',
            'skipAfterPreAudit': 'false',
            'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单预审后是跳过审核
    def order_qpproval_authority_03(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'false',
            'openPreAudit': 'false',
            'skipAfterPreAudit': 'true',
            'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单AI自动审核
    def order_qpproval_authority_04(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'false',
            'openPreAudit': 'false',
            'skipAfterPreAudit': 'false',
            'openAiAudit': 'true'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场审核, 开启订单商场预审
    def order_qpproval_authority_05(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'true',
            'openPreAudit': 'true',
            'skipAfterPreAudit': 'false',
            'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场审核, 开启订单预审后是跳过审核
    def order_qpproval_authority_06(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'true',
            'openPreAudit': 'false',
            'skipAfterPreAudit': 'true',
            'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场审核, 开启订单预审后是跳过审核
    def order_qpproval_authority_07(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'true',
            'openPreAudit': 'false',
            'skipAfterPreAudit': 'false',
            'openAiAudit': 'true'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场预审，订单预审后是跳过审核
    def order_qpproval_authority_08(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
            'openAudit': 'false',
            'openPreAudit': 'true',
            'skipAfterPreAudit': 'true',
            'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 订单预审后是跳过审核，开启订单AI自动审核
    def order_qpproval_authority_09(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
                'openAudit': 'false',
                'openPreAudit': 'true',
                'skipAfterPreAudit': 'false',
                'openAiAudit': 'true'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单AI自动审核，订单预审后是跳过审核
    def order_qpproval_authority_10(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
                'openAudit': 'false',
                'openPreAudit': 'false',
                'skipAfterPreAudit': 'true',
                'openAiAudit': 'true'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场审核, 开启订单预审后是跳过审核， 开启订单商场预审
    def order_qpproval_authority_11(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
                'openAudit': 'true',
                'openPreAudit': 'true',
                'skipAfterPreAudit': 'true',
                'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场预审，订单预审后是跳过审核，开启订单AI自动审核
    def order_qpproval_authority_12(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
                'openAudit': 'false',
                'openPreAudit': 'true',
                'skipAfterPreAudit': 'true',
                'openAiAudit': 'true'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 开启订单商场审核，开启订单商场预审，订单预审后是跳过审核，开启订单AI自动审核
    def order_qpproval_authority_13(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
                'openAudit': 'true',
                'openPreAudit': 'true',
                'skipAfterPreAudit': 'true',
                'openAiAudit': 'true'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

    # 不开启订单商场审核，不开启订单商场预审，订单预审后不跳过审核，不开启订单AI自动审核
    def order_qpproval_authority_14(self):
        url = 'http://api.xymtest.com/mall/order/audit/switch'
        data = {
                'openAudit': 'false',
                'openPreAudit': 'false',
                'skipAfterPreAudit': 'false',
                'openAiAudit': 'false'
        }
        ress = run.run_main(url, 'POST', headers, data)
        assert ress['code'] == 200

# 商户订单开单
class order(unittest.TestCase):
    ''' 商户新用户开单 '''
    def newuser(self):
        '''建立新用户'''
        global newcustid, newname
        ul = 'http://api.xymtest.com/merchant/store/order/manage/custom/add?customName=' + xym.test_cases.test_fee_data.fee_one_data.billing['newname']
        rl = '&mobile=' + xym.test_cases.test_fee_data.fee_one_data.billing['newnumber']
        url = ul + rl
        assert run.run_main(url, 'POST', headers)['code'] == 200
        newcustid = run.run_main(url, 'POST', headers)['data']['custId']
        newname = xym.test_cases.test_fee_data.fee_one_data.billing['newname']
        return newcustid, newname
    def newaddress(self):
        '''建立新用户地址'''
        url = 'http://api.xymtest.com/merchant/store/order/open/add/custom/address'
        data = {
            'mobile': xym.test_cases.test_fee_data.fee_one_data.billing['newnumber'],
            'receiver': newname,
            'customId': newcustid,
            'isDel': 0,
            'addType': 1000,
            'address': "天津市市辖区河东区额请问",
            'areaName': "天津市市辖区河东区",
            'addBlockDTO': {'blockName': "额", 'areaName': "天津市市辖区河东区", 'areaId': "120102"},
            'houseNo': "请问",
            'isDefault': 0
        }
        newaddressorder = run.run_main(url, 'POST', headers, data)
        assert newaddressorder['code'] == 200

    '''商户老用户开单'''
    # 开单老用户查询
    def order_user(self):
        global customid
        useru = 'http://api.xymtest.com/merchant/store/order/manage/get/custom/info?mobile='
        userr = xym.test_cases.test_fee_data.fee_one_data.billing['phonenumber']
        useeurl = useru + userr
        orderuser = run.run_main(useeurl, 'GET', headers)
        assertion.assertions(self, contrast=200, passvalue=orderuser['code'])
        assert orderuser['code'] != 500
        # print(orderuser)
        customid = orderuser['data'][0]['custId']
        realName = orderuser['data'][0]['realName']
        pan = orderuser['data']
        # print('顾客custid:', customid)
        return customid, realName, pan

    # 查询到开单老用户的地址
    def order_address(self):
        addressu = 'http://api.xymtest.com/merchant/store/order/open/distribution?customId='
        addressr = json.dumps(customid)
        addressurl = addressu + addressr
        addressdata = {
            "customId": customid
        }
        orderaddress = run.run_main(addressurl, 'POST', headers)
        assertion.assertions(self, contrast=200, passvalue=orderaddress['code'])
        assert orderaddress['code'] != 500
        # print('顾客地址：', orderaddress)
        address = orderaddress['data']['address'][0]['addId']
        return address

    # 查询开单用户会员卡
    def order_card(self):
        global cardid, cardtype
        cardu = 'http://api.xymtest.com/merchant/custom/member/card/query/list?customId='
        cardr = json.dumps(customid)
        cardl = '&orderId='
        cardurl = cardu + cardr + cardl
        ordercard = run.run_main(cardurl, 'GET', headers)
        assert ordercard['code'] != 500
        # print(ordercard)
        # 根据需要的联名卡来进行返回参数
        membershipcard = ordercard['data']
        for cardId in membershipcard:
            if cardId['cardName'] == xym.test_cases.test_fee_data.fee_one_data.billing['card']:
                cardid = cardId['cardId']
                cardtype = cardId['cardType']
                # print('顾客会员卡customId:', cardid, '\n顾客会员卡类型：', cardtype)
                break
        return cardId

    # 查询所关联的活动
    def activities(self):
        activitiesu = 'http://api.xymtest.com/merchant/store/order/manage/activity/list?customId=' + json.dumps(customid)
        activitiesr = '&cardId=' + cardid
        activitiesl = '&cardType=' + cardtype
        activitiesurl = activitiesu + activitiesr + activitiesl
        # print(activitiesurl)
        activitiesorder = run.run_main(activitiesurl, 'GET', headers)
        print(activitiesorder)
        assert activitiesorder['code'] != 500
        return activitiesorder

    '''商户开单'''
    # 异常开单
    def prequalification_001(self):
        print('001不添加商品顾客开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        # print(prequalificationorder)
        assert prequalificationorder['message'] == '订单至少包含一件商品'
        return prequalificationorder
    def prequalification_002(self):
        print('002开单商品收货，但不填写收货地址')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast='请添加送货地址', passvalue=prequalificationorder['message'])
        # print(prequalificationorder)
        # assert prequalificationorder['code'] == 200
        return prequalificationorder
    def prequalification_003(self):
        print('003开单不收货，单填写收货地址')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] == 200
        # print(prequalificationorder)
        return prequalificationorder
    def prequalification_004(self):
        print('004没有用户开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast='请填写购货人信息', passvalue=prequalificationorder['message'])
        print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_005(self):
        print('005用户没有会员卡开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast='请选择会员卡', passvalue=prequalificationorder['message'])
        # print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_006(self):
        print('006开单用户没有顾客姓名')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast='请填写顾客姓名', passvalue=prequalificationorder['message'])
        # print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_007(self):
        print('007开单不填预计完成时间')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast='订单预计完成时间不可为空', passvalue=prequalificationorder['message'])
        # print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_008(self):
        print('008开单预计完成时间填今天之前')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast='订单预计完成时间需今天或以后', passvalue=prequalificationorder['message'])
        # print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_009(self):
        print('009订单用其它店铺商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=500, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_010(self):
        print('009订单用其它店铺商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_01()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=500, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        # assert prequalificationorder['code'] != 500
        return prequalificationorder


    # 正常开单
    def prequalification_01(self):
        print('不参加活动,不需送货，单个普通商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        # assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        print(prequalificationorder)
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def prequalification_02(self):
        print('不参加活动,需送货，单个普通商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] == 200
        return prequalificationorder
    def prequalification_03(self):
        print('不参加活动,不需送货，单个套组品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_04(self):
        print('不参加活动,不需送货，单个服务费用商商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_05(self):
        print('不参加活动,多个普通商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_06(self):
        print('不参加活动,多个套组商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_07(self):
        print('不参加活动,多个服务费商品开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_08(self):
        print('不参加活动， 普通商品与套组开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_09(self):
        print('不参加活动， 普通商品与服务费开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_10(self):
        print('不参加活动， 套组与服务开单')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder

    # 订单特价开单
    # 普通商品
    def prequalification_11(self):
        print('普通商品特价（不打折）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_12(self):
        print('普通商品特价（不打折）开单,送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_13(self):
        print('普通商品特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_14(self):
        print('普通商品不特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_15(self):
        print('普通商品特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_16(self):
        print('普通商品不特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_17(self):
        print('普通商品特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_18(self):
        print('普通商品不特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_19(self):
        print('不普通商品特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_20(self):
        print('普通商品不特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_02()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 套组
    def prequalification_21(self):
        print('套组商品特价（不打折）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_22(self):
        print('套组商品特价（不打折）开单,送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_23(self):
        print('套组商品特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_24(self):
        print('套组商品不特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_25(self):
        print('套组商品特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_26(self):
        print('套组商品不特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_27(self):
        print('套组商品特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_28(self):
        print('套组商品不特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_29(self):
        print('套组商品特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_30(self):
        print('套组商品不特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_03()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 服务费用
    def prequalification_31(self):
        print('服务费特价（不打折）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_32(self):
        print('服务费特价（不打折）开单,送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_33(self):
        print('服务费特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_34(self):
        print('服务费不特价（单品打折为0）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_35(self):
        print('服务费特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_36(self):
        print('服务费不特价（单品打折为0）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_37(self):
        print('服务费特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_38(self):
        print('服务费不特价（单品打折为1.5）开单,不送货,开启预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_39(self):
        print('服务费特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_40(self):
        print('服务费不特价（单品打折为1.5）开单,不送货,关闭预审')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 普通商品整单打折
    def prequalification_41(self):
        print('普通商品(不特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_42(self):
        print('普通商品(特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_43(self):
        print('普通商品(不特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_44(self):
        print('普通商品(特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_45(self):
        print('普通商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        # print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_46(self):
        print('普通商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_47(self):
        print('普通商品(不特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_48(self):
        print('普通商品(不特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_49(self):
        print('普通商品(特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_50(self):
        print('普通商品(特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_05()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    #  服务费整单打折
    def prequalification_51(self):
        print('服务费商品(不特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_06()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_52(self):
        print('服务费商品(特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_06()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        # print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_53(self):
        print('服务费商品(不特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_54(self):
        print('服务费商品(特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_55(self):
        print('服务费商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_56(self):
        print('服务费商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_57(self):
        print('服务费商品(不特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_58(self):
        print('服务费商品(不特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_59(self):
        print('服务费商品(特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_60(self):
        print('服务费商品(特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_04()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    # 套组商品整单打折
    def prequalification_61(self):
        print('不参加活动， 套组商品(不特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[0]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_62(self):
        print('不参加活动， 套组商品(特价）整单打折(1折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[1]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        # print(prequalificationorder)
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_63(self):
        print('套组商品(不特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[2]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_64(self):
        print('套组商品(特价）整单打折(0折）')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[3]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_65(self):
        print('套组商品(特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[4]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_66(self):
        print('套组商品(不特价）整单打折(1.2折）开启预审，添加商品与订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[5]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_67(self):
        print('套组商品(不特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[6]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_68(self):
        print('套组商品(不特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[7]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_69(self):
        print('套组商品(特价）整单打折(1.2折）开启预审，添加商品附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[8]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder
    def prequalification_70(self):
        print('套组商品(特价）整单打折(1.2折）开启预审，添加订单附件')
        prequalificationurl = 'http://api.xymtest.com/merchant/store/order/open/create'
        prequalificationdata = xym.test_cases.test_fee_data.fee_order_data.billings_07()[9]
        prequalificationorder = run.run_main(prequalificationurl, 'POST', headers, json.dumps(prequalificationdata))
        assertion.assertions(self, contrast=200, passvalue=prequalificationorder['code'])
        assert prequalificationorder['code'] != 500
        return prequalificationorder

    # 查询订单
    global saleStartTime, saleEndTime
    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=7))
    threeDay = (datetime.datetime.now() + datetime.timedelta(days=7))
    # 转换为其他字符串格式
    saleStartTime = threeDayAgo.strftime("%Y-%m-%d")
    saleEndTime = threeDay.strftime("%Y-%m-%d")
    # 查询商户全部订单
    def query_order(self):
        print('测试查询商户全部订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(onedata.orderstatus['pageSize']) + '&saleStartTime=' +  saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=3000,3005,4000,4001,5000,6000,8000,9000,9001,9002,9003,9004,9999'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待支付订单
    def query_order_tbpaid(self):
        print('测试查询商户待支付订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
                onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=3000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待预审订单
    def query_order_tbprequal(self):
        print('测试查询商户待预审订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=3005'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户顾客签名订单
    def query_order_customeraut(self):
        print('测试查询商户顾客签名订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=4000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户商户待签名订单
    def query_order_merchantaut(self):
        print('测试查询商户商户待签名订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=4001'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待完成订单
    def query_order_tbcompleted(self):
        print('测试查询商户待完成订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=5000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户已完成订单
    def query_orde_completed(self):
        print('测试查询商户全部订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=6000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户已退货订单
    def query_order_returned(self):
        print('测试查询商户已退货订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=8000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待审核订单
    def query_order_tbreviewed(self):
        print('测试查询商户待审核订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9000'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户审核不通过订单
    def query_order_auditfailed(self):
        print('测试查询商户审核不通过订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9001'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户修改订单顾客待确认订单
    def query_order_modifycustomer(self):
        print('测试查询商户修改订单顾客待确认订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9002'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户待支付订单
    def query_order_modifymerchant(self):
        """sajfioawjefio"""
        print('测试查询商户待支付订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9003'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        # print(len(queryorder), queryorder[0]['orderNo'])
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户修改订单顾客待确认订单
    def query_order_passprequal(self):
        """sfopaweopf"""
        print('测试查询商户预审审核不通过订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9004'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        # print(len(queryorder), queryorder[0]['orderNo'])
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 查询商户已退单订单
    def query_order_chargeback(self):
        """百度搜索接口"""
        print('测试查询商户已退单订单')
        queryorderu = 'http://api.xymtest.com/merchant/store/order/manage/page/list?pageNo='
        queryorderr = json.dumps(onedata.orderstatus['pageNo']) + '&pageSize=' + json.dumps(
            onedata.orderstatus['pageSize']) + '&saleStartTime=' + saleStartTime + '&saleEndTime=' + saleEndTime
        queryorderl = '&orderStatusLists=9999'
        queryorderurl = queryorderu + queryorderr + queryorderl
        queryorder = run.run_main(queryorderurl, 'POST', headers)['data']['list']
        # print(len(queryorder), queryorder[0]['orderNo'])
        assert run.run_main(queryorderurl, 'POST', headers)['code'] != 500
        ordernos = []
        for conid in range(0, len(queryorder)):
            ordernos.append(queryorder[conid]['orderNo'])
        return ordernos
    # 取消待支付订单(近期一笔待支付订单）
    def tobepaid(self):
        iop = order.query_order_tbpaid(self)
        tobepaidu = 'http://api.xymtest.com/merchant/store/order/manage/cancel?orderNo='
        tobepaidr = iop[0]
        tobepaidurl = tobepaidu + tobepaidr
        tobepaidorde = run.run_main(tobepaidurl, 'POST', headers)
        assert tobepaidorde['code'] != 500
        return tobepaidorde
    # 取消商户全部待支付订单(时间段之内)
    def paid(self):
        iop = order.query_order_tbpaid(self)
        # print(iop)
        # print(len(iop))
        for i in range(0, len(iop)):
            tobepaidu = 'http://api.xymtest.com/merchant/store/order/manage/cancel?orderNo='
            tobepaidr = iop[i]
            tobepaidurl = tobepaidu + tobepaidr
            tobepaidorde = run.run_main(tobepaidurl, 'POST', headers)
            assert tobepaidorde['code'] != 500



