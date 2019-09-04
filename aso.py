# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.5itest.cn/register')
driver.find_element_by_id("register-btn").click()
driver.find_element_by_id("register_email").send_keys("123")

text = driver.find_element_by_id('register_email-error').get_attribute('value')
print(text)