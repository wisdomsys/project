from page.register_page import RegisterPage

class RegisterHandle(object):

    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    # 输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_username(self):
        pass

    # 输入密码
    def send_user_password(self):
        pass

    # 输入验证码
    def send_user_code(self):
        pass

    def click_register_button(self):
        pass