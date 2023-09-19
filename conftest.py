import pytest
from selene.support.shared import browser


@pytest.fixture
def window():
    browser.config.window_height = 1024
    browser.config.window_width = 768
