import pytest
from playwright_stepik.pages.login_page import LoginPage
from playwright_stepik.pages.dashboard_page import DashboardPage


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        }
    }


# set cookies
@pytest.fixture(scope='session')
def browser_context_args_cookies(browser_context_args_cookies):
    return {
        **browser_context_args_cookies,
        'storage_state': {
            'cookies': [
                {
                    'name': 'stepik',
                    'value': 'sd4fFfv!x_cfcstepik',
                    'url': 'https://demo.playwright.dev/todomvc/#/'
                },
            ]
        },
    }


@pytest.fixture()
def login_page(page):
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page):
    return DashboardPage(page)
