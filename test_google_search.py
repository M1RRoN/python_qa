from selene.support.shared import browser
from selene import be, have


browser.config.window_height = 1024
browser.config.window_width = 768


def test_google_search_find(window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_search_not_find(window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('a2к4ек3342s2423a4234').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
