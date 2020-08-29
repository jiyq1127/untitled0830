import time

from selenium.webdriver.common.by import By

from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


class MisArticlePage(BasePage):

    def __init__(self):
        super().__init__()
        self.ari_title_box = (By.CSS_SELECTOR, "[placeholder*='文章']")
        self.query_btn = (By.CSS_SELECTOR, ".find")
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        self.con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_ari_title_box(self):
        return self.find_elt(self.ari_title_box)

    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    def find_con_rej_btn(self):
        return self.find_elt(self.con_rej_btn)


class MisArticleHandle(BaseHandle):

    def __init__(self):
        self.mis_article_page = MisArticlePage()

    def input_ari_title(self, ari_title):
        self.input_text(self.mis_article_page.find_ari_title_box(), ari_title)

    def check_ari_status(self, ari_status):
        check_channel_option(DriverUtils.get_mis_driver(), "请选择状态", ari_status)

    def click_query_btn(self):
        self.mis_article_page.find_query_btn().click()

    def click_aduit_pass_btn(self):
        self.mis_article_page.find_pass_btn().click()

    def click_regic_btn(self):
        self.mis_article_page.find_reject_btn().click()

    def click_confim_btn(self):
        self.mis_article_page.find_con_rej_btn().click()


class MisArticleProxy:

    def __init__(self):
        self.mis_ari_handle = MisArticleHandle()

    def test_pass(self, ari_title):
        self.mis_ari_handle.input_ari_title(ari_title)
        self.mis_ari_handle.check_ari_status("待审核")
        self.mis_ari_handle.click_query_btn()
        self.mis_ari_handle.click_aduit_pass_btn()
        time.sleep(2)
        self.mis_ari_handle.click_confim_btn()
        time.sleep(2)
        self.mis_ari_handle.check_ari_status("审核通过")
        self.mis_ari_handle.click_query_btn()
        time.sleep(3)

    def test_reject(self):
        # 3.选择文章状态
        self.mis_ari_handle.check_ari_status("待审核")
        # 4.点击查询按钮
        self.mis_ari_handle.click_query_btn()
        time.sleep(3)
        # 5.点击驳回按钮
        self.mis_ari_handle.click_regic_btn()
        # 6.点击提示框的确定按钮
        self.mis_ari_handle.click_confim_btn()
        time.sleep(3)
        # 7.切换审核失败界面
        self.mis_ari_handle.check_ari_status("审核失败")
        # 8.点击查询按钮
        self.mis_ari_handle.click_query_btn()
        time.sleep(3)
