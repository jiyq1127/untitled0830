import allure
from selenium.webdriver.common.by import By

from base.mp_base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.username = (By.CSS_SELECTOR, "[placeholder*='手机号']")
        # 验证码
        self.code = (By.CSS_SELECTOR, "[placeholder*='验证码']")
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_username(self):
        return self.find_elt(self.username)

    def find_code(self):
        return self.find_elt(self.code)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    @allure.step(title="输入用户名")
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    @allure.step(title="输入密码")
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    @allure.step(title="点击登录")
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    @allure.step(title="执行调用操作层方法")
    def test_mp_login(self, username, code):
        self.login_handle.input_username(username)
        self.login_handle.input_code(code)
        self.login_handle.click_login_btn()
