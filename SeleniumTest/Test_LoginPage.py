import os
import unittest
import time
from selenium.webdriver.common.keys import Keys
from BaseWebDriver import BaseWebDriver


class Test_Login(unittest.TestCase):

    def test_login(self):
        self.driver.implicitly_wait(30)
        input_username = self.driver.find_element_by_css_selector("input.form-control[type='text']")
        input_username.send_keys("admin")
        input_passwd = self.driver.find_element_by_css_selector("input.form-control[type='password']")
        input_passwd.send_keys("admin")
        btn_login = self.driver.find_element_by_css_selector("button.btn.btn-block")
        btn_login.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(30)


    def setUp(self):
        appconf = os.getcwd() + os.path.sep +  "SeleniumTest"  + os.path.sep + "app.conf"
        self.driver = BaseWebDriver.GetInstance(appconf)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://d114.mlamp.co:8800/#/")

    def tearDown(self):
        self.driver.quit()
        self.driver = None


if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTest(Test_Login("test_login_invalidInput"))
    suite.addTest(Test_Login("test_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
