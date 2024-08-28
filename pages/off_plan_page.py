from pages.base_page import Page
from selenium.webdriver.common.by import By


class OffPlanPage(Page):

    def verify_off_plan_page_enter(self):
        expected_text = 'Total projects'
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text
        assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
