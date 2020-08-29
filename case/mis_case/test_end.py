import pytest

from utils import DriverUtils


@pytest.mark.run(order=104)
class TestEnd:

    def test_end(self):
        DriverUtils.change_mis_key(True)
        DriverUtils.quit_mis_driver()