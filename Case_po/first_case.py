from business.register_business import RegisterBusiness

class FirstCase(object):
    def __init__(self):
        self.login = RegisterBusiness()

    def test_login_email_error(self):
        pass
    # 通过assert判断是否为error

    def test_login_username_error(self):
        pass

    def test_login_code_error(self):
        pass

    def test_login_success(self):
        pass