import pytest
from playwright.sync_api import sync_playwright
from pom.registration_page import RegistrationPage
from pom.login_page import LoginPage
from pom.home_page import HomePage


@pytest.fixture
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_parabank_workflow(setup):
    page = setup

    # 1. Navigate to the application
    page.goto("https://parabank.parasoft.com/parabank/register.htm")

    # 2. Create a new user from registration page
    registration_page = RegistrationPage(page)
    username = registration_page.register_user()

    # # 3. Login to the application with the user created
    # login_page = LoginPage(page)
    # login_page.login(username)

    # # 4. Verify if the Global navigation menu is working as expected
    # home_page = HomePage(page)
    # assert home_page.verify_global_navigation(), "Global navigation menu is not working."

