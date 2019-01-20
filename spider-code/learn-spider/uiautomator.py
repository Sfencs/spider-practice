# -*- coding: utf-8 -*-

# from uiautomator import Device
#
# device=Device()
# print(device.dump())


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome(
    r'D:\chromeDriver\chromedriver_win32\chromedriver.exe')
driver.get('http://218.197.102.183/Course/login.do?msg=EyLaZl9yixsbIZDEIx06KKulsAYxONMkD79ZSU5AnTgjwqm51buxKbW1XnFaf56It1cFMMYb7B4A%0A41PT1aUXkEWakQ9D3k7%2Fvfp%2Bhj357tSNWNKn%2BRVV3qDqiGXqunQlAlBw9pYVSJyseM2g%2FZJ8emPS%0AWRh63bfYlF29ckKTi%2BA%3D%0A%23NT%2Bt7bDn1EDHgkGYWipqhVFNmIP6pPFTS5f4It4gLPO3nYtVHPodigc62FUBbo15egaOOKyl79l1%0Ad3uJ7e5qNgCNxnqCLqmBb9ksJlOlf6hdCMTG7H1zG%2Boh4dV%2Fw33Jw2Avl69h1MJ0RGXAUKCtvDDO%0Akx2DfY7WAzWN5FzAbQk%3D%0A%23E44ES8%2F0Hbc1iCXfrgl3Vx26Jhh0fXh5RjONq0mAYuKyXQ22M0z0iam7joZ5PA6Z11m%2BZiLUV21P%0AE9u5EtFxKB2BfDJyLEKBTX%2BQwiwPTPHOA2SnSTpgfbAaJ1IcXQB%2BbE3xROPf8gTgLC0e0ITIl1%2Fr%0AhLJVS0EmWc%2FM8z6EMic%3D%0A%23SqbFe86gaZfb9dQSXQU59pYnP899IwNnhqnksrZcUypXm2gMVq07NBYPKgjm2Q%2BD8uRi%2BitGeZDJ%0AscwBdNGHFXj6KvDEmOEbV4HaKYN6rwnr9bXrwSc68lA0EDW4fqrD3ULaf%2Bqy0nfCmfPSepwrZSvW%0AcWEqsNAn03vwkqESFm8%3D%0A%23a%2Bl8fqdAUzsFXCGh%2BY3RS8Q67kDX0Sf3xmgb6R6cyHGanDWwikLhxgEyNaBKcgmwP%2Bwbg0HlSQvC%0Ar7JqfC2sC963tAk2wDR%2B1BFbul7IfMFn%2Bk6S13ahPkAppigyIv4l63QAgXD6KjeLFmomTjBowfXT%0A0hT%2FFmo4r0GBInlVYLo%3D%0A%23')
# try:
#     WebDriverWait(
#         driver, 30).until(
#         expected_conditions.presence_of_element_located(
#             (By.CLASS_NAME, "SignContainer-switch")))
# except Exception as _:
#     print('超时了')

input('ddd')
for _ in range(100000):
    driver.refresh()
    time.sleep(5)












