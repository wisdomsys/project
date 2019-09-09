from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
driver = webdriver.Chrome()
driver.maximize_window()
# 访问测试注册网站
driver.get('http://www.5itest.cn/register')
time.sleep(2)
# 判断是否是注册页面
print(EC.title_contains("注册"))
driver.save_screenshot("/Users/yangchao/Desktop/乐学/img.png") # 保存网页截图
# code_element = driver.find_element_by_xpath("//*[@id='getcode_num']")    # 定位验证码
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)     # 获取验证码的图片大小

# 因为截取的图片是实际定位地址图片坐标的2倍 故都乘以2
left = code_element.location['x']*2    # 横坐标
top = code_element.location['y']*2     # 竖坐标
right = code_element.size['width']*2+left
height = code_element.size["height"]*2+top

img = Image.open("/Users/yangchao/Desktop/乐学/img.png").crop((left, top, right, height))
img.save("/Users/yangchao/Desktop/乐学/img副本.png")
img.show()

# 关闭浏览器
driver.close()