from utils import DriverUtils


class BasePage:

    def __init__(self):
        self.driver = DriverUtils.get_mp_driver()

    def find_elt(self, location):
        return self.driver.find_element(*location)

class BaseHandle:

    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

