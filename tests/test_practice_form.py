import allure
from selene import browser

from data.users import User
from pages.registration_page import RegistrationPage
from utils import attach


@allure.tag("web")
@allure.label("owner", "M1RRoN")
@allure.feature("Регистрация пользователя")
def test_complete_practice_form():
    registration_page = RegistrationPage()

    # GIVEN
    user = User(
        first_name='test',
        last_name='user',
        email='test@user.com',
        gender='Male',
        phone_number='7999999999',
        month_of_birth='December',
        year_of_birth='2000',
        day_of_birth='25',
        subject='Maths',
        hobby='Reading',
        picture='image.jpg',
        current_address='Самара, Вилоновская 1',
        state='NCR',
        city='Delhi'
    )
    with allure.step("Открываем страницу регистрации"):
        registration_page.open()
        attach.add_screenshot(browser)

    # WHEN
    with allure.step("Заполняем и отправляем регистрационную форму"):
        registration_page.register(user)
        attach.add_screenshot(browser)

    # THEN
    with allure.step("Проверяем, что пользователь зарегистрирован"):
        registration_page.user_should_registered(user)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
