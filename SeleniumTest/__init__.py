#coding:utf-8


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time


def login_firefox():
    dr = webdriver.Firefox()
    dr.maximize_window()
    dr.implicitly_wait(30)
    dr.get(r"http://d114.mlamp.co:8800/")
    input_username = dr.find_element_by_css_selector("input.form-control[type='text']")
    input_username.send_keys("admin")
    input_passwd = dr.find_element_by_css_selector("input.form-control[type='password']")
    input_passwd.send_keys("admin")
    btn_login = dr.find_element_by_css_selector("button.btn.btn-block")
    btn_login.send_keys(Keys.ENTER)
    dr.quit()

def login_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--test-type")
    #chrome_options.add_experimental_option('prefs', {'download.default_directory':'/tmp'})
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("no-default-browser-check")
    capabilities = DesiredCapabilities.CHROME

    capabilities.update(chrome_options.to_capabilities())
    dr = webdriver.Chrome(desired_capabilities=capabilities,executable_path='/usr/bin/chromedriver')
    dr.implicitly_wait(30)
    
    dr.maximize_window()
    dr.get("https://www.baidu.com/")
    '''
    input_username = dr.find_element_by_css_selector("input.form-control[type='text']")
    input_username.send_keys("admin")
    input_passwd = dr.find_element_by_css_selector("input.form-control[type='password']")
    input_passwd.send_keys("admin")
    btn_login = dr.find_element_by_css_selector("button.btn.btn-block")
    btn_login.send_keys(Keys.ENTER)
    '''
    dr.close()

if __name__ == '__main__':
    login_chrome()
    #login_firefox()
