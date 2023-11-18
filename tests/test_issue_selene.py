from selene import browser, by, be


def test_find_issue_with_selene():
    browser.open('https://github.com/').element('.search-input').click()
    browser.element('#query-builder-test').send_keys('M1RRoN/python_qa').press_enter()
    browser.element(by.link_text('M1RRoN/python_qa')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('test issue')).should(be.visible)
    browser.quit()