from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_navigation_menu(self):
        menu = self.page.locator("nav")  # Example selector for the navigation menu
        menu.wait_for()
        assert menu.is_visible(), "Navigation menu is not visible"
