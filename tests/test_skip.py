import pytest
from selene import browser
from resources.screen_resolutions import DESKTOP_W, DESKTOP_H, MOBILE_W, MOBILE_H


def test_github_desktop(common_browser):
    if common_browser[0] in DESKTOP_W and common_browser[1] in DESKTOP_H:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip(reason='Test only for desktop')


def test_github_mobile(common_browser):
    if common_browser[0] in MOBILE_W and common_browser[1] in MOBILE_H:
        browser.open('/')
        browser.element('a[href="/login"].d-inline-block').click()
    else:
        pytest.skip(reason='Test only for mobile')
