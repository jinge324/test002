import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    url = "https://a.imways.com/#/Login"
    # 1、打开浏览器，最大化浏览器
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    # 用户名元素
    userElement = driver.find_element(By.XPATH, "//*[@id='form-username']")
    # 密码元素
    passElement = driver.find_element(By.XPATH, "//*[@id='form-password']")
    # 验证码输入框元素
    codeElement = driver.find_element(By.XPATH, "//*[@id='form-captcha']")
    # 验证图片元素
    # imgElement = driver.find_element(By.XPATH, "//*[@id='login']/div[1]/div/div/div[2]/div/div[2]/form/div[3]/img")
    imgElement = driver.find_element_by_class_name('captchaImage')
    # 2、截取屏幕内容，保存到本地
    driver.save_screenshot("D://test/01.png")
    location = imgElement.location  # 获取验证码x,y轴坐标
    print(location)
    size = imgElement.size  # 获取验证码的长宽
    print(size)




    # 3、打开截图，获取验证码位置，截取保存验证码
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
    i = Image.open("D://test/01.png")  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4 = frame4.convert('RGB')
    frame4.save('D://test/02.png')  # 保存我们接下来的验证码图片 进行打码


    # 4、获取验证码图片，读取验证码
    imageCode = Image.open("D://test/02.png")  # 图像增强，二值化
    # imageCode.load()
    sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
    sharp_img.save("D://test/03.png")
    sharp_img.load()  # 对比度增强
    time.sleep(2)
    print('1', sharp_img)
    code = pytesseract.image_to_string(sharp_img).strip()
    # 5、收到验证码，进行输入验证
    print(code)

# userElement.send_keys('15871255250')
# passElement.send_keys('456789')
#
# # time.sleep(3)
# codeElement.send_keys(code)
# click_login = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input")
# click_login.click()
