from handle.register_handle import RegisterHandle


# 调用RegisterHandle获取到页面元素，输入信息
class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_handle = RegisterHandle(driver)

    def user_base(self, email, name, password, code):
        self.register_handle.send_user_email(email)
        self.register_handle.send_user_name(name)
        self.register_handle.send_user_password(password)
        self.register_handle.send_user_code(code)
        # self.register_handle.click_register_button()

    def register_success(self):
        if self.register_handle.get_register_text() is None:
            return True
        else:
            return False

    # 邮箱错误
    def login_email_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("email_error", "请输入有效的电子邮件地址") is None:
            print("邮箱校验不成功")
            return True
        else:
            return False

    # 用户名错误
    def login_username_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("username_error", "字符长度必须大于等于4，一个中文字算2个字符") is None:
            print("用户名校验成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("password_error", "最少需要输入 5 个字符") is None:
            print("密码校验成功")
            return True
        else:
            return False

    # 验证码错误
    def login_code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("password_error", "验证码错误") is None:
            print("验证码校验成功")
            return True
        else:
            return False
