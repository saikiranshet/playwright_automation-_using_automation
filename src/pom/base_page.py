from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def type(self, selector: str, text: str):
        self.page.fill(selector, text)

    def is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
