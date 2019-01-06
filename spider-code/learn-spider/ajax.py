# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time


driver=webdriver.Chrome(r'D:\chromeDriver\chromedriver_win32\chromedriver.exe')
driver.get('http://www.le.com/ptv/vplay/31522468.html?ref=jrjd_pc')

try:
    WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"cmt-info j-cmt-info")))
    # WebDriverWait(driver, 30).until(
    #     expected_conditions.text_to_be_present_in_element(
    #         (By.CLASS_NAME, "content"),"通关"))
except Exception as _:
    print('超时了')


element=driver.find_element_by_xpath('//div[@class="content"]')
print(element.text)