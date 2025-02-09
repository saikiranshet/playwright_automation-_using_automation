import json
import random
import time
from playwright.sync_api import Page
from pom.login_page import LoginPage
# from data import *
import os

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
        password = "Password123"

        self.first_name_field.fill("John")
        self.last_name_field.fill("Doe")
        self.address_field.fill("123 Test St")
        self.city_field.fill("Test City")
        self.state_field.fill("Test State")
        self.zip_code_field.fill("12345")
        self.phone_number_field.fill("1234567890")
        self.ssn_field.fill("123-45-6789")
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.confirm_password_field.fill(password)
        self.register_button.click()
        time.sleep(5)  # Allow time for registration

        
        # file_path = os.path.join(os.getcwd(), "data/credentials.json")
        # if not os.path.exists(file_path):
        #     raise FileNotFoundError(f"Error: {file_path} not found.")    
      

        base_dir = os.path.dirname(os.path.dirname(__file__)) 
        data_dir = os.path.join(base_dir, "data")  
        file_path = os.path.join(data_dir, "credentials.json") 

        os.makedirs(data_dir, exist_ok=True)

        credentials = {"username": username, "password": password}
        with open(file_path, "w") as file:
            json.dump(credentials, file)

        assert self.page.title() == "ParaBank | Customer Created", "Registration failed!"

        self.logout.click()
        self.page.goto('https://parabank.parasoft.com/')
        login_page = LoginPage(self.page)
        time.sleep(5)
        login_page.login(username, password)
        assert self.page.title() == "ParaBank | Accounts Overview", "Login failed!"

        print(f"✅ Registration successful! Credentials saved in credentials.json")
