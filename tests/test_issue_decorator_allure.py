import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'M1RRoN')
@allure.feature('Issues tab')
@allure.story('Поиск Issues')
@allure.link('https://github.com/', 'tested_site')
def test_find_issue_with_decorator_allure():
    open_main_page()
    find_repository()
    open_repository()
    open_issue_tab()
    find_issue_with_name()


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий')
def find_repository():
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys('M1RRoN/python_qa').press_enter()


@allure.step('Заходим в репозиторий')
def open_repository():
    browser.element(by.link_text('M1RRoN/python_qa')).click()


@allure.step('Открываем табу Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие нужной issue')
def find_issue_with_name():
    browser.element(by.partial_text('test issue')).should(be.visible)