#! /usr/bin/python
#! coding=UTF-8
import os
import sys
import unittest
reload(sys)
sys.setdefaultencoding('utf-8')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
print BASE_DIR

# from selenium_yoyo.selenium_report.unittest.selenium_second_encapsulation import Yoyo
from a_4_11_selenium_second_encapsulation import Yoyo


'''百度阅读，python selenium这本书的代码，
一、PageObject
1. PageObject设计模式就是把web的每一个页面写成一个page类（继承前面二次封装的）
2. 定位元素方法和操作元素方法分离开，元素定位全部放一起，每一个操作元素动作写成一个方法
二、定位方法对应参照表
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTTOR = "css selector"
'''

login_url = "http://passport.cnblogs.com/user/signin"

class LoginPage(Yoyo):
    # 定位器，定位页面元素
    username_loc = ("id","input1") #输入账号
    password_loc = ("id","input2")
    submit_loc = ("id","signin")
    remenber_loc = ("link text","remenber_me")
    retrive_loc = ("link text","找回")
    reset_loc = ("link text","重置")
    register_loc = ("link text","立即注册")
    feedback_loc = ("link text","反馈问题")

    def input_username(self,username):
        """
        输入账号框
        """
        self.send_keys(self.username_loc,username)

    def input_passwprd(self,password):
        """
        输入密码框
        """
        self.send_keys(self.password_loc,password)
    def click_submit(self):
        """
        登录按钮
        """
        self.click(self.submit_loc)
    def click_remember_live(self):
        """
        下次记住登录
        """
        self.click(self.remenber_loc)

    def click_retrieve(self):
        """
        找回密码
        """
        self.click(self.retrive_loc)

    def click_reset(self):
        """
        重置密码
        """
        self.click(self.reset_loc)

    def click_register(self):
        """
        注册新账号
        """
        self.click(self.register_loc)

    def click_feedback(self):
        """
        反馈问题
        """
        self.click(self.feedback_loc)

    def login(self,username,password):
        """
        登录方法
        """
        self.input_username(username)
        self.input_passwprd(password)
        self.click_submit()
