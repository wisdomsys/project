from base.find_element import FindElement


# 调用base文件下的find_element方法，用于获取元素定位

# 根据元素定位
class RegisterPage(object):

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")

    # 获取用户名
    def get_username_element(self):
        return self.fd.get_element("user_name")

    # 获取密码
    def get_password_element(self):
        return self.fd.get_element("password")

    # 获取验证码
    def get_code_element(self):
        return self.fd.get_element("code_text")

    # 获取注册按钮
    def get_button_element(self):
        return self.fd.get_element("register_button")

    # 获取邮箱错误提示
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")

    # 获取用户名错误提示
    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")

    # 获取密码错误提示
    def get_password_error_element(self):
        return self.fd.get_element("password_error")

    # 获取验证码错误提示
    def get_code_error_element(self):
        return self.fd.get_element("code_text_error")
