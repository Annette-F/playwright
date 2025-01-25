import pytest
import allure


@allure.feature('Authorization')
@allure.story('Login Feature')
@allure.title('Authorization with wrong credentials')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_failure(login_page):
    with allure.step('Open login page'):
        login_page.navigate()
    with allure.step('Enter invalid credentials in the authorization form'):
        login_page.login('invalid_user', 'invalid_password')
    with allure.step('The error is displayed - Invalid credentials. Please try again'):
        assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@allure.feature('Authorization')
@allure.story('Login Feature')
@allure.title('Authorization with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Open login page'):
        login_page.navigate()
    with allure.step('Enter valid credentials in the authorization form'):
        login_page.login(username, password)
    with allure.step("A welcome message with the user's name is displayed."):
        dashboard_page.assert_welcome_message(f'Welcome {username}')
