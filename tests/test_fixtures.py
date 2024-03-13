from selene import browser


def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('a[href="/login"].d-inline-block').click()
