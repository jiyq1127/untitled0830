import logging
import time

import allure

import config
from page.mp_page.home_page import HomeProxy
from page.mp_page.login_page import LoginProxy
from page.mp_page.publish_artical_page import PubAriProxy
from utils import DriverUtils, is_element_exist, get_case_data, get_allure_pic
import pytest


@pytest.mark.run(order=3)
class TestPubArtical:

    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.pub_ari_proxy = PubAriProxy()

    def setup_method(self):
        self.driver.get('http://ttmp.research.itcast.cn/')

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("ari_title", "ari_context", "ari_channel", "expect"),
                             get_case_data("./data/mp/test_pub_ari_data.json"))
    def test_pub_ari(self, ari_title, ari_context, ari_channel, expect):
        config.PUB_ARTICLE_TITLE = ari_title.format(time.strftime('%H%M%S'))
        logging.info("发布文章的标题为：{}".format(config.PUB_ARTICLE_TITLE))
        self.home_proxy.to_pub_ari_page()
        self.pub_ari_proxy.test_pub_artical(config.PUB_ARTICLE_TITLE, ari_context, ari_channel)
        get_allure_pic(self.driver, "发布文章")
        assert is_element_exist(self.driver, expect)

    def teardown_class(self):
        DriverUtils.quit_mp_driver()