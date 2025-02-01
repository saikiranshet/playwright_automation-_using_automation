from playwright.sync_api import Page

class BillPaymentPage:
    def __init__(self, page: Page):
        self.page = page

    def pay_bill(self, account_number: str):
        self.page.locator("text=Bill Pay").click()
        self.page.locator("input[name='amount']").fill("100")
        self.page.locator("input[name='fromAccount']").fill(account_number)
        self.page.locator("input[type='submit']").click()
