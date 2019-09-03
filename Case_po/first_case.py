# coding = utf-8
from business.register_business import RegisterBusiness
from selenium import webdriver


class FirstCase(object):
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('http://www.5itest.cn/register')
        driver.maximize_window()
        self.login = RegisterBusiness(driver)

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34', 'user111', '122333', '1233')
        if email_error == True:
            print("注册成功，此条case执行失败")

    # 通过assert判断是否为error

    def test_login_username_error(self):
        username_error = self.login.login_name_error('123@qq.com', 'qw', '12333', '1231')
        if username_error == True:
            print("注册成功，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error('123@qq.com', 'joseph_beer', '1', '1234')
        if password_error == True:
            print("注册成功，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login__code_error('123@qq.com', 'joseph_beer', '1', '1234')
        if code_error == True:
            print("注册成功，此条case执行失败")

    def test_login_success(self):
        success = self.login.user_base('123@qq.com', 'joseph_beer', '1', '1234')
        if self.login.register_success() == None:
            print("注册成功")


def main():
    first = FirstCase()
    first.test_login_email_error()
    first.test_login_username_error()
    first.test_login_password_error()
    first.test_login_code_error()
    first.test_login_success()


if __name__ == '__main__':
    main()
