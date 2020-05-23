import datetime
import time
# 测试商场下的
headers_market = {
        'x - application - context': 'component - gateway - server:8888',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'tk': 'MTA4MTEwOTUtYjE0YS00MGZhLTg3MTctYmY1MGFmN2U0YmJlMTU4NzEyNTUyNTA=c3RhZmY=MTU4OTk2NTU2OA=='
        }
# 商户南阳店下
header_merchant = {
        'x - application - context': 'component - gateway - server:8888',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'tk': 'NjJmZjliNmUtNGQ1My00NDgyLTk2YWEtYWJmMDU1N2I5NTZjMTM3MDAwMDAwMTI=Y2xlcms=MTU4OTg4MzgxOA=='
        }

class time_obtain():
    # 时间戳
    def time_stamp(self):
        # 先获得时间数组格式的日期
        threeDayAgo = (datetime.datetime.now() + datetime.timedelta(days=1))
        # 转换为时间戳
        timeStamp = int(time.mktime(threeDayAgo.timetuple()))
        return timeStamp

    # 时间前后7（Y-M-D）
    def time_YMD(self):
        # 先获得时间数组格式的日期
        threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=7))
        threeDay = (datetime.datetime.now() + datetime.timedelta(days=7))
        ootime = datetime.datetime.now()
        # 转换为其他字符串格式
        saleStartTime = threeDayAgo.strftime("%Y-%m-%d")
        saleEndTime = threeDay.strftime("%Y-%m-%d")
        newtime = ootime.strftime("%Y-%m-%d")
        return saleStartTime, saleEndTime, newtime