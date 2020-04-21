
from selenium import webdriver
import time
import pymysql.cursors
#连接
connect = pymysql.connect(
    host='10.0.2.21',
    port=3306,
    user='root',
    passwd='123456',
    charset='utf-8'
)
print('连接成功！')
# #获取游标
# cursor = connect.cursor()
# #插入数据
# sql = "INSERT INTO ways_marketing_call_plan_oa_info(`oa_no`,`oa_name`,`name`,`mobile`,`mall_id`,`create_by`,`create_name`,`create_time`)
#   VALUES('987','赵金鸽','ceshi',CONCAT(mobile,'12'),66,912,'123',NOW())"
#
# sql = "insert into "
# connect.execute(sql)
# connect.commit()
# print('成功插入',cursor.rowcount,'条数据')
#
#
# #关闭连接
# cursor.close()
connect.close()


