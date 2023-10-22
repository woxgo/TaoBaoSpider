# 模拟登录
import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils import create_chrome_driver

browser = create_chrome_driver()
browser.get('https://login.taobao.com')

# 隐式等待
browser.implicitly_wait(10)

# 获取页面元素模拟用户输入和点击行为
username_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-id')
username_input.send_keys('13231165226')  # 填写用户名

password_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-password')
password_input.send_keys('PengYang@123')  # 填写对应的密码

# 登录按钮
login_button = browser.find_element(By.CSS_SELECTOR, '#login-form > div.fm-btn > button')
login_button.click()

# 显示等待
# wait_obj = WebDriverWait(browser, 10)
# wait_obj.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.m-userinfo')))
time.sleep(15)

# 获取登录的cookie数据，并且写入文件
with open('taobao2.json', 'w') as file:
    json.dump(browser.get_cookies(), file)