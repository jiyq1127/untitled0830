import unittest

from parameterized import parameterized

from page.app_page.index_page import IndexProxy
from utils import DriverUtils, is_el_by_attribute


class TestQueryAritcal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.get_app_driver()
        cls.index_proxy = IndexProxy()

    def setup(self):
        self.driver.start_activity("com.itcast.toutiaoApp", ".MainActivity")

    @parameterized.expand(["架构"])
    def test_qy_article(self, channel_name):
        # channel_name = "架构"
        self.index_proxy.test_qari_by_channel(channel_name)
        self.assertTrue(is_el_by_attribute(self.driver, "text", "点赞"))

    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_app_driver()