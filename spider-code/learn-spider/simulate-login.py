# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome(
    r'D:\chromeDriver\chromedriver_win32\chromedriver.exe')
driver.get('https://www.zhihu.com/#signin')
try:
    WebDriverWait(
        driver, 30).until(
        expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "SignContainer-switch")))
except Exception as _:
    print('超时了')

convert = driver.find_element_by_xpath(
    '//div[@class="SignContainer-switch"]/span')
convert.click()
element = driver.find_element_by_name('username')
element.clear()
element.send_keys('用户名或手机号')
password = driver.find_element_by_name('password')
password.clear()
password.send_keys('密码')
input('输完验证码后回来随便点击')
login = driver.find_element_by_class_name('SignFlow-submitButton')
login.click()
input('输完验证码后回来随便点击')
login = driver.find_element_by_class_name('SignFlow-submitButton')
login.click()
try:
    WebDriverWait(
        driver, 30).until(
        expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, "ContentItem-actions")))
except Exception as _:
    print('超时了')

print(driver.page_source)
