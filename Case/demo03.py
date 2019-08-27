from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from PIL import Image



driver = webdriver.Chrome()
driver.maximize_window()
# 访问测试注册网站
driver.get('http://www.5itest.cn/register')
time.sleep(5)
# 判断是否是注册页面
print(EC.title_contains("注册"))
driver.save_screenshot("/Users/yangchao/Desktop/乐学/img.png")
# 定位验证码
code_elemet = driver.find_element_by_id("getcode_num")
# 获取验证码的坐标
location = code_elemet.location
print(location)
# 获取验证码的图片大小
size = code_elemet.size
print(size)

# 横坐标
left = code_elemet.location['x']
# 竖坐标
top = code_elemet.location['y']

right = code_elemet.size['width']+left
height = code_elemet.size['height']+top
im = Image.open("/Users/yangchao/Desktop/乐学/img.png")
img = im.crop((left,top, right, height))
img.save("/Users/yangchao/Desktop/乐学/img1.png")



email_element = driver.find_element_by_id("register_email")
email = ['qq','163','gmail']
for i in range(5):
    for j in email:
        user_email =''.join(random.sample('1234567890abcdefg', 5))+"@"+j+'.com'
        print(user_email)
email_element.send_keys(user_email([1]))
print(email_element.get_attribute("value"))

# 找到用户名
user_element = driver.find_elements_by_class_name("controls")[1]
user_element_class = user_element.find_element_by_class_name("form-control")
user_element_class.send_keys("joseph_beer")

# 找到密码
driver.find_element_by_name("password").send_keys("ych19951005")
# 找到验证码
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
# 点击注册
driver.find_element_by_id("register-btn").click()

# 关闭浏览器
driver.close()
