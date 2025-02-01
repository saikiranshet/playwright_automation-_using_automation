from playwright.sync_api import Page

class NewAccountPage:
    def __init__(self, page: Page):
        self.page = page

    def create_savings_account(self):
        self.page.locator("text=Open New Account").click()
        self.page.locator("select[name='type']").select_option("SAVINGS")
        self.page.locator("input[type='submit']").click()
        account_number = self.page.locator("div.accountNumber").text_content()
        return account_number
