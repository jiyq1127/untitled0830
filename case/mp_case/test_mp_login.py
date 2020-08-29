import allure
import pytest

from page.mp_page.login_page import LoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=2)
class TestMpLogin:

    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.login_proxy = LoginProxy()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_mp_login(self):
        username = '15811859004'
        code = '246810'
        self.login_proxy.test_mp_login(username, code)
        assert is_element_exist(self.driver, '江苏传智播客')


    def teardown_class(self):
        DriverUtils.quit_mp_driver()
