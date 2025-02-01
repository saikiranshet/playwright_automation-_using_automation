import pytest
import random
import string
from playwright.sync_api import sync_playwright
import time

# Utility function to generate a random username
def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

# Test Steps
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for CI/CD or production
        yield browser
        browser.close()

def test_para_bank_registration_and_actions(browser):
    # 1. Navigate to Para Bank application
    page = browser.new_page()
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    
    # 2. Create a new user from user registration page
    username = generate_random_username()  # Unique username for every test execution
    page.fill('input[name="customer.firstName"]', 'John')
    page.fill('input[name="customer.lastName"]', 'Doe')
    page.fill('input[name="customer.address.street"]', '123 Main St')
    page.fill('input[name="customer.address.city"]', 'Anytown')
    page.fill('input[name="customer.address.state"]', 'CA')
    page.fill('input[name="customer.address.zipCode"]', '12345')
    page.fill('input[name="customer.phoneNumber"]', '555-1234')
    page.fill('input[name="customer.ssn"]', '123-45-6789')
    page.fill('input[name="customer.username"]', username)  # Random username
    page.fill('input[name="customer.password"]', 'password')
    page.fill('input[name="repeatedPassword"]', 'password')
    time.sleep(10)
    page.click('xpath=//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
    
    # # 3. Login to the application with the user created
    # page.goto("https://parabank.parasoft.com/parabank/register.htm")
    # page.fill('input[name="username"]', username)
    # page.fill('input[name="password"]', 'password')
    # page.click('input[type="submit"]')
    
    # time.sleep(10)
    # 4. Verify if the Global navigation menu on the home page is working
    # assert page.is_visible('text=Accounts Overview')
    # assert page.is_visible('text=Bill Pay')
    # assert page.is_visible('text=Transfer Funds')
    
    # 5. Create a Savings account from “Open New Account Page”
    page.goto("https://parabank.parasoft.com/parabank/openaccount.htm")
    page.select_option('select[name="type"]', 'SAVINGS')  # Select Savings account
    page.fill('input[name="customer.id"]', '1')  # Assuming '1' is a valid customer ID
    page.click('input[type="submit"]')
    account_number = page.locator('text=Account Number:').text_content()  # Capture the account number
    assert account_number, "Account number not captured."

    # 6. Validate if Accounts overview page is displaying the balance details as expected
    page.goto("https://parabank.parasoft.com/parabank/overview.htm")
    balance = page.locator('text=Balance:').text_content()
    assert balance, "Balance details are not displayed."

    # 7. Transfer funds from the created account to another account
    page.goto("https://parabank.parasoft.com/parabank/transfer.htm")
    page.fill('input[name="amount"]', '100')
    page.fill('input[name="fromAccountId"]', account_number)
    page.fill('input[name="toAccountId"]', '2')  # Transfer to another account, here '2' is used
    page.click('input[type="submit"]')

    # 8. Pay the bill with the created account
    page.goto("https://parabank.parasoft.com/parabank/billpay.htm")
    page.fill('input[name="payee.name"]', 'Electricity Bill')
    page.fill('input[name="amount"]', '50')
    page.fill('input[name="fromAccountId"]', account_number)
    page.click('input[type="submit"]')

    # 9. Add necessary assertions at each test step whenever it is needed.
    page.wait_for_selector('text=Bill payment complete')
    assert page.is_visible('text=Bill payment complete')

    page.close()
