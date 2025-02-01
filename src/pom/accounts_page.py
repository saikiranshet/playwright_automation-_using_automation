from playwright.sync_api import Page

class AccountsPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_balance_details(self):
        balance_locator = self.page.locator("div.balance")
        balance_locator.wait_for()
        assert balance_locator.is_visible(), "Balance details are not visible"
