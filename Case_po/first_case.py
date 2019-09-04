# coding = utf-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest


class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)
        print("这是case的前置条件")

    def tearDown(self):
        self.driver.close()
        print("这是case的后置条件")

    def test_login_email_error(self):
        user_email_error = self.login.login_email_error('34', 'user111', '122333', '1233')
        if user_email_error == True:
            print("注册成功，此条case执行失败")

    # 通过assert判断是否为error

    # def test_login_username_error(self):
    #     user_name_error = self.login.login_name_error('1232765@gmail.com', 'qw', '12333', '1231')
    #     if user_name_error == True:
    #         print("注册成功，此条case执行失败")

    # def test_login_password_error(self):
    #     password_error = self.login.login_password_error('12331441@gmail.com', 'joseji21', '123456', '1234')
    #     if password_error == True:
    #         print("注册成功，此条case执行失败")

    # def test_login_code_error(self):
    #     code_text_error = self.login.login__code_error('12321441@qq.com', 'josep_er', '123345', '1234')
    #     if code_text_error == True:
    #         print("注册成功，此条case执行失败")

    # def test_login_success(self):
    #     success = self.login.user_base('123@qq.com', 'joseph_beer', '111111', '1234')
    #     if self.login.register_success() == True:
    #         print("注册成功")


# def main():
#     first = FirstCase()
#     first.test_login_email_error()
#     first.test_login_username_error()
#     first.test_login_password_error()
#     first.test_login_code_error()
#     first.test_login_success()


if __name__ == '__main__':
    unittest.main()
