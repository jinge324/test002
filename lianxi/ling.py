'''
Created on 2018年10月25日

@author: Administrator
'''
from platform import node
#from asn1crypto._ffi import null

if __name__ == '__main__':
    #总金额
    totalmoney = 0
    jihe = []
    print("*********欢迎光临xx旅游网***************")
    while 1 == 1:
        print("1.添加出行订单  2.查看我的出行订单  3.修改订单信息  4.删除出行人  5.查看行程   6.退出系统[4~6待开发]")
        xuan = int(input("请选择："))
        if xuan == 1:
            date = input("请输入出行日期（如：20170501）：")
            while True:
                phonenumber = input("请输入联系人手机号码：")
                if len(phonenumber) == 11:
                    break
                else:
                    print("电话号格式不对，请重新输入！")
            print("*********添加出行人信息**************")
            while True:
                xuanlei = int(input("1.成人  2.儿童（1.2米以下）  3.老人（65岁以上）"))
                if xuanlei == 1:
                    name = input("请输入姓名：")
                    age = int(input("请输入年龄："))
                    totalmoney += 2000;
                    linshi = [name,age,'  否  ',2000]
                    jihe.append(linshi)
                    print("姓名：",name,"年龄：",age,"本次出行金额：",totalmoney)
                elif xuanlei == 2:
                    name = input("请输入姓名：")
                    age = int(input("请输入年龄："))
                    zhan = int(input("是否占床：1.占床 2.不占床"))
                    if zhan == 1:
                        totalmoney += 30;
                        print("姓名：",name , "年龄：",age ,"占床1.2m以下儿童免费，本次金额：30元")
                        linshi = [name,age,'是',30]
                        jihe.append(linshi)
                    else :
                        print("姓名：",name , "年龄：",age ,"不占床1.2m以下儿童免费，本次金额：元")
                        linshi = [name,age,'不是',0]
                        jihe.append(linshi)
                elif xuanlei == 3:
                    name = input("请输入姓名：")
                    age = int(input("请输入年龄："))
                    if age <= 65:
                        print("对不起，老人订单年龄需为65岁以上！")
                    else:
                        print("姓名：",name , "年龄：",age ,"65岁以上老年人半价，本次金额：1000元")
                        totalmoney += 1000;
                        linshi = [name,age,1000]
                        jihe.append(linshi)
                else:
                    print("输入有误，请正确输入！")
                if input("是否继续添加（Y/N）?:") == "n":
                    break;
            print("***********订单信息****************")
            print("出行日期：" , date)
            print("手机号：" , totalmoney)
            print("订单总金额：" , totalmoney , "元")
        elif xuan==2:
            #print(jihe)
            print("姓名    年龄    儿童是否占床    金额");
            for i in jihe:
                for j in i:
                    print(j,end="  ")
                print( )
        elif xuan == 3:
            Newdate = input("请输入新的出行日期：")
            Newnumber = input("请输入新的联系人手机号码：")
            date = Newdate
            while True:
                if len(phonenumber)==11:
                    phonenumber = Newnumber
                    break;
                else:
                    print("电话号格式不对，请重新输入！")
            print("出行日期：",date,"联系人手机号码：",phonenumber,"修改成功！")
        elif xuan == 4:
            for i in jihe:
                for j in i:
                    print(j[0])
                print( )
        elif xuan == 5:
            pass
        else:
            print("谢谢使用！")
            break;