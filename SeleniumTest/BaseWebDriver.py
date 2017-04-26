#coding:utf-8

import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import os
import unittest
import threading




class HelpUtil(object):

    @classmethod
    def readCfgFile(cls, appconf, section, option):
        if os.path.exists(appconf) == False:
            #log the error
            return
        cf = ConfigParser()
        cf.read(appconf, encoding="utf-8")
        if section not in cf.sections():
            #log the error
            return
        if option not in cf.options(section):
            #log the error
            return
        return cf.get(section=section, option= option)

#实现单利模式
class BaseWebDriver(object):
    driver = None
    mutex = threading.Lock()

    def _init__(self):
        pass

    @staticmethod
    def GetInstance(appconf):
        if BaseWebDriver.driver == None:
            BaseWebDriver.mutex.acquire()
            if BaseWebDriver.driver == None:
                browsername = HelpUtil.readCfgFile(appconf= appconf, section="common", option="browsername")
                execPath = HelpUtil.readCfgFile(appconf= appconf, section=platform.system().lower(), option=browsername)
                downloadpath = HelpUtil.readCfgFile(appconf= appconf, section=platform.system().lower(), option="downloadpath")
                if browsername == "firefox":
                    BaseWebDriver.driver = webdriver.Firefox(executable_path=execPath, log_path=None)

                elif browsername == "chrome":
                    chrome_options = Options()
                    chrome_options.add_argument("--disable-extensions")
                    chrome_options.add_argument('--disable-logging')
                    chrome_options.add_argument("--ignore-certificate-errors")
                    chrome_options.add_argument("--test-type")
                    chrome_options.add_experimental_option('prefs', {'download.default_directory':downloadpath})
                    chrome_options.add_argument("--start-maximized")
                    chrome_options.add_argument("no-default-browser-check")
                    capabilities = DesiredCapabilities.CHROME
                    capabilities.update(chrome_options.to_capabilities())
                    BaseWebDriver.driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=execPath)
                print('初始化实例')
            else:
                print('单例已经实例化')
            BaseWebDriver.mutex.release()
        else:
            print('单例已经实例化')
        return BaseWebDriver.driver

#class BaseWebElement(object):


if __name__ == '__main__':
    driver1 = BaseWebDriver.GetInstance("app.conf")
    driver2 = BaseWebDriver.GetInstance("app.conf")
    '''
    js = "var q=document.getElementById(\"kw\");q.style.border=\"1px solid red\";"
        # 调用js
    self.driver.execute_script(js)
    '''
    print(driver1)
    print ("-----")
    print(driver2)