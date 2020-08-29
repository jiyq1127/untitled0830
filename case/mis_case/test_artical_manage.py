import time

import config
import pytest

from page.mis_page.mis_artical_page import MisArticleProxy
from page.mis_page.mis_home_page import MisHomePage
from page.mis_page.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestArticleMana:

    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.login_page = MisLoginProxy()
        self.home_page = MisHomePage()
        self.ad_page = MisArticleProxy()

    # def setup_method(self):
    #     time.sleep(2)
    #     self.driver.get("http://ttmis.research.itcast.cn/#/home")

    def test_ari_pass(self):
        ari_title = config.PUB_ARTICLE_TITLE
        self.home_page.to_article_page()
        self.ad_page.test_pass(ari_title)

        assert is_element_exist(self.driver, "驳回")

    # @pytest.mark.run(order=3)
    # def test_reject_ari(self):
    #     self.home_page.to_article_page()

    def teardown_class(self):
        DriverUtils.quit_mis_driver()
