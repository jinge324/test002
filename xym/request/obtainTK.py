import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import path
import xym.request.mybaiduTK
import base64
import requests
import xym.request.myrequests
import json
import HTMLTestRunner
import unittest

reqs = xym.request.myrequests.RunMain

class TK(unittest.TestSuite):
    # 截取图片验证码并增强验证码图片的像素
    def obtaincode(self):
        # global url
        # 控制浏览器
        driver = webdriver.Chrome()
        # 浏览器最大化
        driver.maximize_window()
        # 按地址进入界面
        driver.get('https://a.imways.com/#/Login')
        # 刷新图片验证码
        driver.find_element_by_class_name('captchaImage').click()
        time.sleep(1)
        # 截取屏幕内容，保存到本地
        driver.save_screenshot('D://test/01.png')
        # 获取验证码x,y轴坐标
        imgElement = driver.find_element_by_class_name('captchaImage')
        xy = imgElement.location
        print(xy)
        # 获取验证码的长宽
        size = imgElement.size
        print(size)
        # 定义验证码位置坐标
        position = (int(xy['x']), int(xy['y']), int(xy['x'] + size['width']), int(xy['y'] + size['height']))
        # 打开截图
        rangle = Image.open("D://test/01.png")
        # 使用Image的crop函数，从截图中截取验证码
        frame4 = rangle.crop(position).convert('RGB')
        # 保存我们接下来的验证码图片
        frame4.save('D://test/02.png')
        # 获取验证码图片，读取验证码
        imageCode = Image.open("D://test/02.png")
        # 图像增强，二值化
        sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
        sharp_img.save("D://test/03.png")
        sharp_img.load()  # 对比度增强
        time.sleep(2)
        print(sharp_img)
        # code = pytesseract.image_to_string(sharp_img).strip()
        # code = pytesseract.image_to_string(sharp_img)
        # # 收到验证码，进行输入验证
        # print(code)
        # driver.close()
        # return code
    # 百度识别图片验证码
    def Distinguishcode(self, baidutk):
        global res
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
        # 二进制方式打开图片文件
        f = open('D:/test/03.png', 'rb')
        img = base64.b64encode(f.read())

        params = {'image': img}
        access_token = baidutk
        request_url = request_url + "?access_token=" + access_token

        headers = {'content-type': 'application/x-www-form-urlencoded'}
        res = requests.post(request_url, data=params, headers=headers).json()['words_result'][0]['words'].strip()
        if res[0] == " ":
            trim(res[1:])
        else:
            print('没有空格')
        print('图片验证码：', res)
        print(res)
        return res
    # 登录网页获取系统tk
    def gettk(self, signname, signpass):
        signurl = 'https://api.imways.com/authentication/mall/staff/signin'
        signheaders = {
            'content-type': 'application/json;charset=UTF-8',
            'cookie': 'ways_captcha_id=9a0e7feb-9ece-4af9-9f9d-3f11d490426c; SESSION=ca541381-2964-4664-8783-d1aca7515c12; SERVERID=c0d431612f22feee04ca31341db22539|1586485082|1586221459'

        }
        signdata = {
            'type': 0,
            'source': 'staff',
            'userName': signname,
            'targetUrl': '',
            'password': signpass,
            'captcha': res
        }
        tk = requests.post(signurl, data=signdata).json()
        print(tk)
        print(tk['code'])
        return tk['code'], tk['data']

if __name__ == '__main__':
    i = TK()
    # 访问网址
    url = 'https://a.imways.com/#/Login'
    # 图片验证码class元素
    classa = 'captchaImage'
    # 调用截取验证码
    # a = i.obtaincode(url, classa)
    i.obtaincode()
    # 获取百度应用tk
    o = xym.request.mybaiduTK.mytk()
    # 百度接口识别图片验证码
    i.Distinguishcode(o)
    # 进行登录接口验证
    signname = '15871255250'
    signpass = '654789'
    a, b = i.gettk(signname, signpass)
    print(b)
