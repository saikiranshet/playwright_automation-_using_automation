import random
import string
from playwright.sync_api import Page
from pom.login_page import LoginPage
import time

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.locator("input[name='customer.firstName']")
        self.last_name_field = page.locator("input[name='customer.lastName']")
        self.address_field = page.locator("input[name='customer.address.street']")
        self.city_field = page.locator("input[name='customer.address.city']")
        self.state_field = page.locator("input[name='customer.address.state']")
        self.zip_code_field = page.locator("input[name='customer.address.zipCode']")
        self.phone_number_field = page.locator("input[name='customer.phoneNumber']")
        self.ssn_field = page.locator("input[name='customer.ssn']")
        self.username_field = page.locator("input[name='customer.username']")
        self.password_field = page.locator("input[name='customer.password']")
        self.confirm_password_field = page.locator("input[name='repeatedPassword']")
        self.register_button = page.locator('//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input')
        self.logout = page.locator('//*[@id="leftPanel"]/ul/li[8]/a')
        self.error_message_locator = page.locator(".error")  

    def generate_random_username(self):
        words = ["alpha", "beta", "gamma", "delta", "omega", "zeta"]
        numbers = str(random.randint(1000, 9999))
        return f"{random.choice(words)}{numbers}@gmail.com"

    def register_user(self):
        username = self.generate_random_username()
        # print(username)
        self.first_name_field.fill("John")
        self.last_name_field.fill("Doe")
        self.address_field.fill("123 Test St")
        self.city_field.fill("Test City")
        self.state_field.fill("Test State")
        self.zip_code_field.fill("12345")
        self.phone_number_field.fill("1234567890")
        self.ssn_field.fill("123-45-6789")
        self.username_field.fill(username)
        # self.username_field.fill("saikiranshet2")
        self.password_field.fill("Password123")
        self.confirm_password_field.fill("Password123")
        self.register_button.click()
        time.sleep(10)
        assert self.page.title(), "ParaBank | Customer Created"
        self.logout.click()
        self.page.goto('https://parabank.parasoft.com/')
        login_page = LoginPage(self.page)
        time.sleep(10)
        login_page.login(username,'Password123')
        assert self.page.title(), "ParaBank | Accounts Overview"

        


    
    
