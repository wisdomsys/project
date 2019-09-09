from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 访问测试注册网站
driver.get('http://www.5itest.cn/register')
time.sleep(5)
# 判断是否是注册页面
print(EC.title_contains("注册"))

# ①判断元素是否显示
# element = driver.find_element_by_class_name("controls")
# EC.visibility_of_element_located(element)

# ② ---采用
# locator = (By.CLASS_NAME,"controls")
# element = driver.find_element_by_class_name("controls")
#
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element))



# 找到邮箱地址
# ① driver.find_element_by_id("register_email").send_keys("1396871335@qq.com")

# 获取元素的属性值
# email_element = driver.find_element_by_id("register_email")
# random.sample('')
# print(email_element.get_attribute("placeholder"))
# email_element.send_keys("test@163.com")
# print(email_element.get_attribute("value"))

email_element = driver.find_element_by_id("register_email")
for i in range(5):
    user_email = random.sample('1234567890abcdefg', 5)
    print(user_email)

#找到用户名
# 三种找元素的方式
# ①driver.find_element_by_id("register_nickname").send_keys("joseph_beer") 多个元素定位时，id是唯一的
# ②driver.find_element_by_xpath("//*[@id='register_nickname']").send_keys("joseph_beer") Xpath定位
# ③当遇到多个class元素相同时，选择下列这种方式，根据返回的class list的len[n]选择需要定位的class
user_element = driver.find_elements_by_class_name("controls")[1]
user_element_class = user_element.find_element_by_class_name("form-control")
user_element_class.send_keys("joseph_beer")

# 找到密码
driver.find_element_by_name("password").send_keys("ych19951005")
# 找到验证码
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
# 点击注册
driver.find_element_by_id("register-btn").click()

time.sleep(500)
# 关闭浏览器
driver.close()
