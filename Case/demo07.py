from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.5itest.cn/register')  # 访问测试注册网站
time.sleep(2)
print(EC.title_contains("注册"))  # 判断是否是注册页面
driver.save_screenshot("/Users/yangchao/Desktop/乐学/img.png")     # 保存网页截图
code_element = driver.find_element_by_id("getcode_num")     # 定位验证码

left = code_element.location['x']*2    # 横坐标
top = code_element.location['y']*2     # 竖坐标
right = code_element.size['width']*2+left
height = code_element.size["height"]*2+top

img = Image.open("/Users/yangchao/Desktop/乐学/img.png").crop((left, top, right, height))
img.save("/Users/yangchao/Desktop/乐学/img副本.png")

r = ShowapiRequest("http://route.showapi.com/184-4","103808","1f246b6e2d1c48aa919228586d68db37" )
r.addFilePara("image","/Users/yangchao/Desktop/乐学/img副本.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text)

driver.find_element_by_id("register_email").send_keys("13788@163.com")
# 找到用户名
user_element = driver.find_elements_by_class_name("controls")[1]
user_element_class = user_element.find_element_by_class_name("form-control")
user_element_class.send_keys("joseph")

# 找到密码
driver.find_element_by_name("password").send_keys("ych19951005")
# 找到验证码
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys(text)
# 点击注册
driver.find_element_by_id("register-btn").click()
driver.save_screenshot("/Users/yangchao/Desktop/乐学/img_login.png")
time.sleep(10)

# 关闭浏览器
driver.close()
