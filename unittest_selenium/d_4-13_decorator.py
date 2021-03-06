#! /usr/bin/python
#! coding=UTF-8
import unittest

import time
from selenium import webdriver

'''
4.13装饰器之异常后截图 
实现百度搜索功能
'''

driver = webdriver.Firefox()

# 截图功能

def get_screen():
    nowTime = time.strftime("%Y%m%d.%H%M%S")
    driver.get_screenshot_as_file('%s.jpg'%nowTime)
    # 自动截图装饰器

def screen(func):
    # 截图装饰器
    def inner(*args,**kwargs):
        try:
            f = func(*args,**kwargs)
            return f
        except:
            return  get_screen()
    return inner()

@screen
def search(driver):
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw11").send_keys("python")
    driver.find_element_by_id("su").click()

if __name__=="__main__":
    search(driver)
