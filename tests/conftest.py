import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def init_settings():
    browser.config.timeout = 3
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield