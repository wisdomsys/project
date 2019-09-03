from handle.register_handle import RegisterHandle
# 调用RegisterHandle获取到页面元素，输入信息


class RegisterBusiness(object):
    # 执行操作
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_username(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)

    def register_success(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            False

    # 邮箱错误
    def login_email_error(self, email, name, password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('email_error', "请输入有效的电子邮箱地址") == None:
            print("邮箱校验不成功")
            return True
        else:
            return False

    # name错误
    def login_name_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('name_error', "字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名校验不成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('name_error', "最少需要输入 5 个字符") == None:
            print("密码校验不成功")
            return True
        else:
            return False

    # 验证码错误
    def login__code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
            print("验证码校验不成功")
            return True
        else:
            return False
