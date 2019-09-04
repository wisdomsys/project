# coding=utf-8
from page.register_page import RegisterPage


# 调用page下的register（定位页面元素，输入信息）

class RegisterHandle(object):

    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    # 输入邮箱
    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_username(self, username):
        self.register_p.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, code):
        self.register_p.get_code_element().send_keys(code)

    # 获取报错信息
    def get_user_text(self, info):
        if info == "user_email_error":
            text = self.register_p.get_email_error_element().get_attribute('value')
            print(text)
        elif info == "user_name_error":
            text = self.register_p.get_name_error_element().get_attribute('value')
            print(text)
        elif info == "password_error":
            text = self.register_p.get_password_error_element().get_attribute('value')
            print(text)
        else:
            text = self.register_p.get_code_error_element().get_attribute('value')
            print(text)
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 获取注册按钮
    def get_register_text(self):
        return self.register_p.get_button_element().get_attribute("value")
