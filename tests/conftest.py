import pytest
from selene import browser
from resources.screen_resolutions import *


@pytest.fixture(params=[FULL_HD, HD])
def desktop_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[iPHONE_12_PRO, PIXEL_7])
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(params=[FULL_HD, HD, iPHONE_12_PRO, PIXEL_7])
def common_browser(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield width, height

    browser.quit()





