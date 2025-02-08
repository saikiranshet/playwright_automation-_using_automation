import pytest
from playwright.sync_api import sync_playwright
from pom.homescreen_navigation_page import HomePage
from pom.registration_page import RegistrationPage
from pom.new_accounts_page import NewAccountPage



@pytest.fixture(scope="session")
def setup():
    """Set up the browser and page for all tests in the session."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
