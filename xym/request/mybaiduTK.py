# encoding:utf-8
import requests

# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=LV2aC6Kj34osS5yqw1Ne9GgT&client_secret=tZ5z02acKzyTakZtgBhGuGsEfx1t2fDw'
# response = requests.get(host).json()['access_token']
# print(response)

def mytk():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=LV2aC6Kj34osS5yqw1Ne9GgT&client_secret=tZ5z02acKzyTakZtgBhGuGsEfx1t2fDw'
    response = requests.get(host).json()['access_token']
    print('百度tk', response)
    return response



