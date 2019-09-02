from base.find_element import FindElement
class RegisterPage(object):

    def __init__(self,driver):
        self.f = FindElement(driver)

    # 获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")

    def get_username_element(self):
        return self.fd.get_element("user_name")

    def get_password_element(self):
        return self.fd.get_element("password")

    def get_code_element(self):
        return self.fd.get_element("code_text")