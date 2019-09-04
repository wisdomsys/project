from handle.register_handle import RegisterHandle
# 调用RegisterHandle获取到页面元素，输入信息


class RegisterBusiness(object):
    # 执行操作
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, username, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_username(username)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)

    def register_success(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            False

    # 邮箱错误
    def login_email_error(self, email, username, password, code):
        self.user_base(email, username, password, code)
        if self.register_h.get_user_text('user_email_error') is None:
            print("邮箱校验不成功")
            return True
        else:
            return False

    # name错误
    def login_name_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text("user_name_error") is None:
            print("用户名校验不成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('password_error') is None:
            print("密码校验不成功")
            return True
        else:
            return False

    # 验证码错误
    def login__code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('code_text_error') is None:
            print("验证码校验不成功")
            return True
        else:
            return False
