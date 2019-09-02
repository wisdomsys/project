from handle.register_handle import RegisterHandle

class RegisterBusiness(object):
    # 执行操作
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def login(self, email, name, password, code, register_button):
        self.register_h.send_user_email(email)
        self.register_h.send_user_username(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button(register_button)
        if self.register_h.get_user_text("请输入有效的电子邮箱地址"):
            print("邮箱校验成功")
            return True
        else:
            return False