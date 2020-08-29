from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle


class MisHomePage(BasePage, BaseHandle):

    def __init__(self):
        super().__init__()
        self.info_manage_tab = (By.XPATH, "//*[contains(text(), '信息管理')]")
        self.context_manage_tab = (By.XPATH, "//*[contains(text(),'内容审核')]")

    def to_article_page(self):
        self.find_elt(self.info_manage_tab).click()
        self.find_elt(self.context_manage_tab).click()