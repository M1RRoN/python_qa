from pages.registration_page import RegistrationPage


def test_complete_practice_form():
    # GIVEN
    registration_page = RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.fill_first_name("test")
    registration_page.fill_last_name("user")
    registration_page.fill_email("test@user.com")
    registration_page.fill_gender()
    registration_page.fill_number('79999999999')
    registration_page.fill_date_of_birth(2000, "December", 25)
    registration_page.choose_subject('math')
    registration_page.choose_hobbies()
    registration_page.upload_image()
    registration_page.fill_current_address('Самара, Вилоновская 1')
    registration_page.choose_state('NCR')
    registration_page.choose_city('Delhi')
    registration_page.delete_footer()
    registration_page.submit_form()

    # THEN
    registration_page.should_registered_user_with(
        'test user',
        'test@user.com',
        'Male',
        '7999999999',
        '25 December,2000',
        'Maths',
        'Reading',
        'image.jpg',
        'Самара, Вилоновская 1',
        'NCR Delhi'
    )
