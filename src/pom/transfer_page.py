from playwright.sync_api import Page

class TransferPage:
    def __init__(self, page: Page):
        self.page = page

    def transfer_funds(self, from_account: str, to_account: str, amount: str):
        self.page.locator("text=Transfer Funds").click()
        self.page.locator("input[name='amount']").fill(amount)
        self.page.locator("input[name='fromAccount']").fill(from_account)
        self.page.locator("input[name='toAccount']").fill(to_account)
        self.page.locator("input[type='submit']").click()
