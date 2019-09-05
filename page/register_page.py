from base.find_element import FindElement


class RegisterPage(object):

    def __init__(self, driver):
        self.find_element = FindElement(driver)

    def get_email_element(self):
        return self.find_element.get_element("user_email")

    def get_username_element(self):
        return self.find_element.get_element("user_name")

    def get_password_element(self):
        return self.find_element.get_element("password")

    def get_code_element(self):
        return self.find_element.get_element("code_text")

    def get_button_element(self):
        return self.find_element.get_element("register_button")

    # 错误信息......
    # 获取邮箱栏错误提示
    def get_email_error_info(self):
        return self.find_element.get_element("user_email_error")

    # 获取用户名错误提示
    def get_username_error_info(self):
        return self.find_element.get_element("user_email_error")

    # 获取密码错误提示
    def get_password_error_info(self):
        return self.find_element.get_element("password_error")

    # 获取验证码错误提示
    def get_code_error_info(self):
        return self.find_element.get_element("code_text_error")
