#! /usr/bin/python
#! coding=UTF-8
import unittest
'''
运行该unittest测试用例，但是会运行失败，原因是cnblogs登录需要验证码，所以登录不成功，只有添加了cookie才能跳过验证码直接登录
相应的代码需要fiddler抓包，需要在windows上运行fiddler

'''

from a_4_11_selenium_second_encapsulation import browser
from b_4_12_pageObject_selenuim  import LoginPage,login_url

class Login_test(unittest.TestCase):
    """
    登录页面的case
    """
    def setUp(self):
        self.driver = browser()
        self.login = LoginPage(self.driver)  #login参数是LoginPage的实例
        self.login.open(login_url)

    def login_case(self,username,psw,expect=True):

        """
        登录用例的方法
        """

    #第1步 ：输入账号
        self.login.input_username(username)
    #第2步 ：输入密码
        self.login.input_passwprd(psw)

    #第3步 ：点登录按钮
        self.login.click_submit()

    #第4步 ：测试结果，判断是否登录成功

        result = self.login.is_text_in_element(("id","lnk_current_usr"),"上海-悠悠")

    #第5步 ：期望结果
        expect_result = expect
        self.assertEqual(result,expect_result)

    def test_login01(self):
        """
        输入正确账号密码
        """
        self.login_case("min0893","yueliang_9513",True)

    def test_login02(self):
        """
        输入错误账号密码
        """
        self.login_case("min0893","aaa",False)

    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
