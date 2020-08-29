import pytest

from page.mis_page.mis_login_page import MisLoginProxy
from utils import DriverUtils


@pytest.mark.run(order=102)
class TestMisLogin:

    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.mis_login_proxy = MisLoginProxy()

    def setup_method(self):
        self.driver.get("http://ttmis.research.itcast.cn/")

    def test_mis_login(self):
        username = "testid"
        password = "testpwd123"
        self.mis_login_proxy.test_mis_login(username, password)

    def teardown_class(self):
        DriverUtils.quit_mis_driver()

