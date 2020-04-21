from selenium import webdriver
import time

if __name__ == '__main__':
    # # 创建浏览器驱动
    # driver = webdriver.Chrome()
    # # 打开浏览器
    # driver.get("https://www.baidu.com")
    # #用搜素引擎搜关键字“微博评论爬虫 python”
    # driver.find_element_by_id("kw").send_keys("微博评论爬虫 python")
    # #点击百度一下
    # driver.find_element_by_id("su").click()
    # #点击搜索工具
    # time.sleep(1)
    # driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[2]/div/i").click()
    # #添加时间限制“一周内”
    # time.sleep(1)
    # driver.find_element_by_class_name("search_tool_tf ").click()
    # driver.find_element_by_xpath("//*[@id='c-tips-container']/div[1]/div/div/ul/li[3]/a").click()
    # #最大化窗体
    # driver.maximize_window()
    driver = webdriver.Chrome()
    driver.get("https://www.weibo.com/109240924?is_all=1#_rnd1584949927309")







