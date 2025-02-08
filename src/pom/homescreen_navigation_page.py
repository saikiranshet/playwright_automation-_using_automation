from playwright.sync_api import Page
from pom.login_page import LoginPage
import time


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
    def verify_homescreen_menu(self):
        self.page.locator('//*[@id="headerPanel"]/ul[2]/li[1]/a').click()  
        assert self.page.title(),'| Welcome | Online Banking'

    def verify_emp_screen(self):
        self.page.locator('//*[@id="headerPanel"]/ul[2]/li[2]/a').click()  
        assert self.page.title(), 'ParaBank | About Us'

    def verify_customer_screen(self):
        self.page.locator('//*[@id="headerPanel"]/ul[2]/li[3]/a').click() 
        assert self.page.title(),'ParaBank | Customer Care'
    