# coding=utf-8
from page.register_page import RegisterPage


# 调用page下的register（定位页面元素，输入信息）

class RegisterHandle(object):
    def __init__(self, driver):
        self.register_page = RegisterPage(driver)

    # 输入邮箱
    def send_user_email(self, email):
        self.register_page.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self, username):
        self.register_page.get_username_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        self.register_page.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, code):
        self.register_page.get_code_element().send_keys(code)

    # 获取错误信息（获取到注册页中的错误信息）
    def get_user_text(self, info, user_info):
        text = None
        if info == "register_email_error":
            text = self.register_page.get_email_error_info().send_keys("value")
        elif info == "register_username_error":
            text = self.register_page.get_username_error_info().send_keys("value")
        elif info == "register_password_error":
            text = self.register_page.get_password_error_info().send_keys("value")
        # elif info == "captcha_code_error":
        #     text = self.register_page.get_code_error_info().send_keys("value")
        else:
            print("遇到了未知的错误......")
        return text

    # 点击注册按钮
    def click_register_button(self, button):
        self.register_page.get_button_element().send_keys(button)

    # 获取注册按钮的文字
    def get_register_text(self):
        return self.register_page.get_button_element().text
