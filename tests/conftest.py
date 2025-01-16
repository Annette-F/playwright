from playwright.sync_api import Page
import pytest


@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto('https://www.litres.ru/')


    yield page
