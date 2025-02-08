import pytest
from playwright.sync_api import sync_playwright
from pom.homescreen_navigation_page import HomePage
from pom.registration_page import RegistrationPage
from pom.accounts_page import AccountsPage
from pom.new_accounts_page import NewAccountPage
from pom.bill_payment_page import BillPaymentPage
from pom.transfer_page import TransferPage


@pytest.fixture(scope="session")
def setup():
    """Set up the browser and page for all tests in the session."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()
