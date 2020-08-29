from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle
from utils import DriverUtils, check_channel_option


class PubAriPage(BasePage):

    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # frame
        self.ari_frame = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 内容
        self.ari_context = (By.CSS_SELECTOR, "body")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道选择框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道选项
        self.channel_option = (By.XPATH, "//*[text()='android']")
        # 发表
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    def find_ari_iframe(self):
        return self.find_elt(self.ari_frame)

    def find_ari_context(self):
        return self.find_elt(self.ari_context)

    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_channel_option(self):
        return self.find_elt(self.channel_option)

    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


class PubAriHandle(BaseHandle):

    def __init__(self):
        self.pub_ari_page = PubAriPage()

    def input_ari_title(self, title):
        self.input_text(self.pub_ari_page.find_ari_title(), title)

    def input_ari_context(self, context):
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_ari_page.find_ari_iframe())
        self.input_text(self.pub_ari_page.find_ari_context(), context)
        DriverUtils.get_mp_driver().switch_to.default_content()

    def check_ari_cover(self):
        self.pub_ari_page.find_ari_cover().click()

    def check_ari_channel(self, channel_name):
        check_channel_option(DriverUtils.get_mp_driver(), "请选择", channel_name)


    def click_btn(self):
        self.pub_ari_page.find_pub_btn().click()


class PubAriProxy:


    def __init__(self):
        self.pub_ari_handel = PubAriHandle()

    def test_pub_artical(self, title, context, channel_name):
        self.pub_ari_handel.input_ari_title(title)
        self.pub_ari_handel.input_ari_context(context)
        self.pub_ari_handel.check_ari_cover()
        self.pub_ari_handel.check_ari_channel(channel_name)
        self.pub_ari_handel.click_btn()
