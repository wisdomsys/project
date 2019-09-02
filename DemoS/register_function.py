from selenium import webdriver
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from DemoS.find_element import FindElement
import time

class RegisterFunction(object):
    def __init__(self, url ,i):
        self.driver = self.get_driver(url,i)

# 获取driver，并且打开url
    def get_driver(self, url ,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Safari()
        driver.get(url)
        driver.maximize_window()
        return driver

# 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

# 定位用户信息 获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

# 获取随机数
    def get_range_user(self):
        user_info = ''.join(random.sample('123456789abcdefg', 8))
        return user_info

    # 获取图片
    def get_code_image(self, file_name):
        # self.driver.save_screenshot("/Users/joseph/Desktop/乐学/register.png") 截取整个网页的图片
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x'] * 2  # 横坐标
        top = code_element.location['y'] * 2  # 竖坐标
        right = code_element.size['width'] * 2 + left
        height = code_element.size["height"] * 2 + top
        im = Image.open(file_name)
        img_code = im.crop((left, top, right, height))
        img_code.save(file_name)

    #解析图片，获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "103808", "1f246b6e2d1c48aa919228586d68db37")
        r.addFilePara("image", file_name)
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text

    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info + "@163.com"
        file_name = "/Users/joseph/Desktop/乐学/code.png"
        code_text = self.code_online(file_name)
        self.send_user_info("user_email",user_email)
        self.send_user_info("user_name",user_name_info)
        self.send_user_info("password",user_email)
        self.send_user_info("code_text",code_text)
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error")
        if code_error ==None:
            print("注册成功")
        else:
            self.driver.save_screenshot("/Users/joseph/Desktop/乐学/code_error.png")
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()