import json
import logging
import time

import allure
import selenium.webdriver
import appium.webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtils:
    __mp_driver = None
    __mis_driver = None
    __app_driver = None

    __mp_key = True
    __mis_key = True
    __app_key = True

    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(30)
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            time.sleep(3)
            cls.__mp_driver.quit()
            cls.__mp_driver = None

    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.implicitly_wait(30)
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver is not None and cls.__mis_key:
            time.sleep(3)
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None and cls.__mis_key:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            desired_caps['noReset'] = True
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    @classmethod
    def change_app_key(cls, key):
        cls.__app_key = key

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            time.sleep(3)
            cls.__app_driver.quit()
            cls.__app_driver = None


# 根据文本判断元素是否存在的公用方法
def is_element_exist(driver, text):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(text(),'{}')]".format(text)
    # 显示等待查找元素，如果能找到元素则返回元素对象，找不到返回False,并且抛出异常
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        logging.error(NoSuchElementException("找不到文本为{}的元素对象".format(text)))
        return False

def my_wait(driver, str_xpath):
    try:
        element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return element
    except Exception as e:
        NoSuchElementException("找不到{}的元素对象".format(str_xpath))



def is_el_by_attribute(driver, attr_name, attr_value):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(@{}, '{}')]".format(attr_name, attr_value)
    # 显示等待查找元素，如果能找到元素则返回元素对象，找不到返回False,并且抛出异常
    try:
        is_element = my_wait(driver, str_xpath)
        return is_element
    except Exception as e:
        logging.error(NoSuchElementException("找不到文本为{}的元素对象".format(attr_name)))
        return False


def check_channel_option(driver, channel_name, option_name):
    str_xpath = "//*[contains(@placeholder, '{}')]".format(channel_name)
    driver.find_element_by_xpath(str_xpath).click()
    channel_option = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    is_suc = False
    for option_element in channel_option:
        if option_element.text == option_name:
            option_element.click()
            is_suc = True
            break
        else:
            action = ActionChains(driver)
            action.move_to_element(option_element).send_keys(Keys.DOWN).perform()

    if is_suc is False:
        NoSuchElementException("can not find name is {} channel option".format(option_name))


def get_case_data(file_path):
    test_data = []
    with open(file=file_path, encoding='utf-8')as f:
        str_dict = json.load(f)

        for i in str_dict.values():
            test_data.append(list(i.values()))
            print(test_data)
    return test_data


def get_allure_pic(driver, filename):
    allure.attach(
        driver.get_screenshot_as_png(), filename, allure.attachment_type.PNG)