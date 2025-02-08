import time

class LoginPage():
    def __init__(self,page):
        self.page = page
        self.username_field = '//*[@id="loginPanel"]/form/div[1]/input'
        self.password_field = '//*[@id="loginPanel"]/form/div[2]/input'
        self.login_button = '//*[@id="loginPanel"]/form/div[3]/input'

    def login(self, username, password):
        self.page.locator(self.username_field).type(username)  
        self.page.locator(self.password_field).type(password) 
        print("LOGIN USERNAME",username)
        print("LOGIN PASSWORD",password)
        time.sleep(5)
        self.page.locator(self.login_button).click()



