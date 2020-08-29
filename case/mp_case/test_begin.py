import pytest

from utils import DriverUtils


@pytest.mark.run(order=1)
class TestBegin:

    def test_begin(self):
        DriverUtils.change_mp_key(False)