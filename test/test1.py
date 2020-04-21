'''
项目
'''
from selenium import webdriver
import time

if __name__ == '__main__':
    # 创建浏览器驱动
    driver = webdriver.Chrome()
    # 打开浏览器
    driver.get("https://www.jinchutou.com/")
    # 最大化
    driver.maximize_window()
    time.sleep(3)
    # 点击登录
    driver.find_element_by_xpath("//span/a[text()='[登录]']").click()
    # 登录
    time.sleep(2)
    driver.find_element_by_id("Content_txtUserName").send_keys("asdf");
    driver.find_element_by_id("Content_txtPassword").send_keys("123456");
    time.sleep(2)
    driver.find_element_by_id("Content_btnLogin").click();
    # 点击专题库
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/li[2]/a").click()
    time.sleep(2)
    # # 获取当前的窗口
    # nowhandle = driver.current_window_handle
    # driver.find_element_by_xpath("//div[@class='h3']").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='form1']/div[3]/div/div[4]/table/tbody/tr/td[1]/div[2]/ul/li[2]/a").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='listmain']/div[2]/div[1]/dl[2]/dd/a[2]").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("//*[@id='listmain']/div[2]/div[1]/dl[3]/dd/a[3]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='listmain']/div[2]/div[1]/dl[4]/dd/a[3]").click()
    # time.sleep(3)
    # # 获取当前的窗口
    # nowhandle = driver.current_window_handle
    # driver.find_element_by_xpath("//ul[@id='content']/li[2]/p[1]/a/img").click()
    # time.sleep(2)
    # # 跳窗口
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # # 点击下一页
    # time.sleep(2)
    # driver.find_element_by_xpath("//li[@class='paging']/input[@id='nextPageButton']").click()
    # # 收藏
    # time.sleep(2)
    # driver.find_element_by_xpath("//td/input[@value='收藏']").click()
    # time.sleep(3)
    # driver.switch_to_frame(0)
    # time.sleep(2)
    # driver.find_element_by_id("txtAwardName").send_keys("1")
    # driver.find_element_by_xpath("//td/input[@name='selectfolderradio']").click()
    # # 加入收藏
    # time.sleep(2)
    # driver.find_element_by_id("Button1").click()
    # driver.switch_to_alert().accept()
    # # 退回顶层框架
    # driver.switch_to_default_content();
    # # 我的书房
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='headerplace']/div/div/span/span[2]/a[2]").click()
    # time.sleep(2)
    # # 我的收藏
    # driver.find_element_by_xpath("//*[@id='form1']/div[3]/table/tbody/tr/th/div/ul/dl[1]/dd/ul/li[5]/a").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//table[@class='bmtable']//tr/td[2]/a").click()
    # time.sleep(3)
    # windows = driver.window_handles
    # driver.switch_to_window(windows[2])
    # driver.close()
    # time.sleep(3)
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # driver.close()
    # driver.switch_to_window(nowhandle)
    # # 点击专题库 进行精品推荐
    # driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/li[2]/a").click()
    # # 获取当前的窗口
    # nowhandle1 = driver.current_window_handle
    # # 点击精品推荐第一个
    # driver.find_element_by_xpath("//a[text()='专业毕业设计论文大全']").click()
    # # 跳窗口
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # time.sleep(2)
    # driver.find_element_by_xpath(
    #     "//*[@id='form1']/div[3]/div/table/tbody/tr/td[1]/div[2]/div[2]/li[1]/table/tbody/tr/td[2]/a").click()
    # # 跳窗口
    # windows = driver.window_handles
    # driver.switch_to_window(windows[2])
    # # 点击下一页
    # time.sleep(2)
    # driver.find_element_by_xpath("//li[@class='paging']/input[@id='nextPageButton']").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//li[@class='paging']/input[@id='nextPageButton']").click()
    # # 关闭浏览器
    # time.sleep(3)
    # driver.close()
    # # 一键打包带走
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # driver.find_element_by_xpath("//div[@class='cart']/a").click()
    # time.sleep(2)
    # # 点击微信支付
    # driver.find_element_by_xpath("//img[@id='zhifu004']").click()
    # driver.switch_to_frame(0)
    # time.sleep(4)
    # driver.find_element_by_xpath("//a[@class='d-close']").click()
    # driver.close()
    # # 回到原先的窗口
    # time.sleep(2)
    # driver.switch_to_window(nowhandle1)
    # # 点击全部分类的工作/办公/管理
    # driver.find_element_by_xpath("//li[@id='tj01']/a").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='form1']/div[3]/div/div[1]/div/div[1]/table/tbody/tr/td/div/div/a[3]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='form1']/div[3]/div/div[1]/div/div[1]/table/tbody/tr/td/div/div/a[4]").click()
    # nowhandle = driver.current_window_handle
    # time.sleep(2)
    # driver.find_element_by_xpath("//p/a[text()='家庭教育有妙招']").click()
    # # 跳窗口
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # # 点击视图模式
    # time.sleep(2)
    # driver.find_element_by_xpath("//dl[@class='cam']/dd/a").click()
    # # 一键打包
    # time.sleep(2)
    # driver.find_element_by_xpath("//div[@class='cart']/a").click()
    # # 点击支付宝
    # time.sleep(2)
    # driver.find_element_by_xpath("//img[@id='zhifu005']").click()
    # windows = driver.window_handles
    # driver.switch_to_window(windows[2])
    # time.sleep(3)
    # driver.close()
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # time.sleep(2)
    # driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/a").click()
    # driver.close()
    # time.sleep(2)
    # driver.switch_to_window(nowhandle)
    # time.sleep(3)
    # # 点击PPT模板库
    # driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[2]/li[3]/a").click()
    # time.sleep(2)
    # # 获取当前的窗口
    # nowhandle = driver.current_window_handle
    # # 点击热门推荐
    # driver.find_element_by_xpath(
    #     "//*[@id='form1']/div[3]/div/div[3]/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/a").click()
    # time.sleep(2)
    # # 跳窗口
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # # 点击下一页
    # time.sleep(2)
    # driver.find_element_by_xpath("//li[@class='paging']/input[@id='nextPageButton']").click()
    # time.sleep(2)
    # # 关闭浏览器
    # driver.close()
    # driver.switch_to_window(nowhandle)
    # # 查询
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='listmain']/div[2]/div[1]/dl[3]/dd/a[2]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='listmain']/div[2]/div[1]/dl[4]/dd/a[3]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='listmain']/div[2]/div[1]/dl[5]/dd/a[3]").click()
    # time.sleep(2)
    # # 鼠标滑动
    # js = "var q=document.documentElement.scrollTop=600"
    # driver.execute_script(js)
    # # 点击查询出来的ppt
    # time.sleep(2)
    # driver.find_element_by_xpath("//*[@id='content']/li[7]/p[1]/a/img").click()
    # windows = driver.window_handles
    # driver.switch_to_window(windows[1])
    # time.sleep(2)
    # driver.close()
    # driver.switch_to_window(nowhandle)
    # # 鼠标往上滑动
    # js = "var q=document.documentElement.scrollTop=0"
    # driver.execute_script(js)
    # time.sleep(2)
    # # 点击切换模式
    # driver.find_element_by_xpath("//div[@class='listan']/li/a").click()
    # js = "var q=document.documentElement.scrollTop=600"
    # driver.execute_script(js)
    # time.sleep(2)
    # driver.find_element_by_xpath("//div[@class='listan']/li[@class='wz']/a").click()
    # time.sleep(2)
    # # 向下滑
    # js = "var q=document.documentElement.scrollTop=600"
    # driver.execute_script(js)
    # driver.execute_script("var q=document.documentElement.scrollTop=0");
    # time.sleep(2)
    # driver.find_element_by_xpath("//div[@class='border']/form/input").send_keys("计算机")
    # time.sleep(2)
    # driver.find_element_by_xpath("//div[@class='border']/form/input[2]").click()
    # time.sleep(2)
    # driver.find_element_by_xpath(
    #     "//*[@id='form1']/div[3]/div/div[2]/div[2]/ul/li[1]/div[1]/table/tbody/tr/td/a/img").click()
    # time.sleep(2)
    # driver.quit()
