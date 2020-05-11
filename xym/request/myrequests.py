import requests
import json

class RunMain:
    # # 实例初始化
    # def __init__(self, url, method, headers, data=None):
    #     self.res = self.run_main(url, method, headers, data)

    # 构造函数
    def send_post(self, url, headers, data):
        # post接口的
        res = requests.post(url=url, headers=headers, data=data).json()
        # 返回请求
        return res

    def send_get(self, url, headers, data):
        # get接口的
        res = requests.get(url=url, headers=headers, data=data).json()
        # 返回请求
        return res

    def run_main(self, url, method, headers=None, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, headers, data)
        else:
            res = self.send_post(url, headers, data)
        return res