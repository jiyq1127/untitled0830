from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.context_tab = (By.XPATH, "//*[text()='内容管理']")
        self.pub_ari_tab = (By.XPATH, "//*[contains(text(),'发布文章')]")

    def find_context_tab(self):
        return self.find_elt(self.context_tab)

    def find_pub_ari_tab(self):
        return self.find_elt(self.pub_ari_tab)


class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    def click_context_tab(self):
        self.home_page.find_context_tab().click()

    def click_pub_ari_tab(self):
        self.home_page.find_pub_ari_tab().click()


class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    def to_pub_ari_page(self):
        self.home_handle.click_context_tab()
        self.home_handle.click_pub_ari_tab()


