from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
# 浏览器初始化
def driver_init():
    driver.maximize_window()
    driver.get('http://www.5itest.cn/register')  # 访问测试注册网站
    time.sleep(2)

# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('123456789abcdefg', 8))
    return user_info

# 获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    left = code_element.location['x'] * 2  # 横坐标
    top = code_element.location['y'] * 2  # 竖坐标
    right = code_element.size['width'] * 2 + left
    height = code_element.size["height"] * 2 + top
    im = Image.open(file_name)
    img_code = im.crop((left, top, right, height))
    img_code.save(file_name)

#解析图片，获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "103808", "1f246b6e2d1c48aa919228586d68db37")
    r.addFilePara("image",file_name)
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    return text

# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    file_name = "/Users/joseph/Desktop/乐学/code.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("qweasd")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    driver.find_element_by_id("register-btn").click()
    return user_email,user_name_info
    time.sleep(10)
    driver.close()
run_main()