from pom.registration_page import RegistrationPage
from pom.login_page import LoginPage
from pom.homescreen_navigation_page import HomePage
from pom.new_accounts_page import NewAccountPage
import time

def test_navigate_to_parabank(setup):
    page = setup
    page.goto('https://parabank.parasoft.com/')
    assert page.title() == "ParaBank | Welcome | Online Banking"

def test_registration_with_login(setup):
    page = setup
    page.goto("https://parabank.parasoft.com/parabank/register.htm")
    registration_page = RegistrationPage(page)
    registration_page.register_user() 

def test_global_menu(setup):
    page = setup
    homepg_naa = HomePage(page)
    homepg_naa.verify_homescreen_menu()
    homepg_naa.verify_emp_screen()
    homepg_naa.verify_customer_screen()
    homepg_naa.verify_homescreen_menu()

def test_opening_account(setup):
    page = setup
    account_page = NewAccountPage(page)
    account_id = account_page.create_savings_account() 
    account_page.calculations()
    account_page.transfer_funds()
    account_page.pay_bill([account_id]) 