# coding = utf-8
from selenium import webdriver
import time
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.5itest.cn/register')  # 访问测试注册网站
    time.sleep(2)