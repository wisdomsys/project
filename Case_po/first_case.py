# coding = utf-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest


class FirstCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.register_business = RegisterBusiness(self.driver)
        print("----前置----")

    def tearDown(self) -> None:
        self.driver.close()
        print("----后置----")

    def test_login_email_error(self):
        user_email_error = self.register_business.login_email_error('34', 'user111', '122333', '1233')
        self.assertTrue(user_email_error, "注册失败，此条case执行成功")

    # 通过assert判断是否为error

    def test_login_username_error(self):
        user_name_error = self.register_business.login_username_error('1232765@gmail.com', 'qw', '12333', '1231')
        if user_name_error is True:
            print("注册失败，此条case执行成功")

    def test_login_password_error(self):
        password_error = self.register_business.login_password_error('12331441@gmail.com', 'joseji21', '123456', '1234')
        if password_error is True:
            print("注册失败，此条case执行成功")

    def test_login_code_error(self):
        code_text_error = self.register_business.login_code_error('12321441@qq.com', 'josep_er', '123345', '1234')
        if code_text_error is True:
            print("注册失败，此条case执行成功")

    def test_login_success(self):
        success = self.register_business.user_base('123@qq.com', 'joseph_beer', '111111', '1234')
        if self.register_business.register_success() is True:
            print("注册成功")


def main():
    first = FirstCase()
    first.test_login_email_error()
    # first.test_login_username_error()
    # first.test_login_password_error()
    # first.test_login_code_error()
    # first.test_login_success()


if __name__ == '__main__':
    unittest.main()
