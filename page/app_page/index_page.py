from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.app_base.base_page import BasePage
from utils import DriverUtils


class IndexPage(BasePage):

    def __init__(self):
        super().__init__()
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        self.channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
        self.first_article = (By.XPATH, "//*[contains(@text,'评论')]")

    def find_channel_option(self, channel_name):
        # return self.find_elt(self.channel_option)
        return DriverUtils.get_app_driver().find_element(self.channel_option[0],
                                                         self.channel_option[1].format(channel_name))

    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    def find_first_article(self):
        return self.find_elt(self.first_article)


class IndexHandle():

    def __init__(self):
        self.index_page = IndexPage()

    def check_channel_option(self, channel_name):
        area_element = self.index_page.find_channel_area()
        x = area_element.location['x']
        y = area_element.location['y']
        w = area_element.size['width']
        h = area_element.size['height']
        start_y = y + h * 0.5
        start_x = x + w * 0.8
        end_y = start_y
        end_x = x + w * 0.2

        while True:
            page_old = DriverUtils.get_app_driver().page_source

            try:
                self.index_page.find_channel_option(channel_name).click()
                break
            except Exception as e:
                DriverUtils.get_app_driver().swipe(start_x, start_y, end_x, end_y)
                page_new = DriverUtils.get_app_driver().page_source
                if page_new == page_old:
                    raise NoSuchElementException("没有找到{}")

    def click_first_article(self):
        self.index_page.find_first_article().click()


class IndexProxy:

    def __init__(self):
        self.index_handle = IndexHandle()

    def test_qari_by_channel(self, channel_name):
        self.index_handle.check_channel_option(channel_name)
        self.index_handle.click_first_article()






