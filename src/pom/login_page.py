from pom.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = "input[name='username']"
        self.password_field = "input[name='password']"
        self.login_button = "input[type='submit']"

    def login(self, username, password):
        self.type(self.username_field, username)
        self.type(self.password_field, password)
        self.click(self.login_button)
