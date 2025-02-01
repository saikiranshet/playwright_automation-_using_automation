import pytest
from playwright.sync_api import sync_playwright
from pom.home_page import HomePage
from pom.registration_page import RegistrationPage
from pom.accounts_page import AccountsPage
from pom.new_accounts_page import NewAccountPage
from pom.bill_payment_page import BillPaymentPage
from pom.transfer_page import TransferPage


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="module")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def register_page(page):
    return RegisterPage(page)


@pytest.fixture()
def accounts_page(page):
    return AccountsPage(page)


@pytest.fixture()
def new_account_page(page):
    return NewAccountPage(page)


@pytest.fixture()
def bill_payment_page(page):
    return BillPaymentPage(page)


@pytest.fixture()
def transfer_page(page):
    return TransferPage(page)
