from pages.base_page import Page
from selenium.webdriver.common.by import By


class WellcomePage(Page):
    OPEN_BROWSER_BUTTON = (By.CSS_SELECTOR, "[href*='https://soft.reelly.io/sign-in']")

    def open(self):
        self.open_url('https://www.reelly.io')

    def click_button(self):
        self.click(*self.OPEN_BROWSER_BUTTON)


