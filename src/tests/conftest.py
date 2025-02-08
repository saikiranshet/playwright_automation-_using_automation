import pytest
from playwright.sync_api import sync_playwright
from pom.homescreen_navigation_page import HomePage
from pom.registration_page import RegistrationPage
from pom.new_accounts_page import NewAccountPage


@pytest.fixture(scope="session")
def pytest_addoption(parser):
    """Add a command-line option for running tests in headless mode."""
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")


@pytest.fixture(scope="session")
def setup():
    """Set up the browser and page for all tests in the session."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--start-maximized'])
        page = browser.new_page(no_viewport=True)
        yield page
        browser.close()
