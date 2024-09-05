from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class OffPlanPage(Page):
    PRICE1_FIELD = (By.CSS_SELECTOR, "[wized='unitPriceFromFilter']")
    PRICE2_FIELD = (By.CSS_SELECTOR, "[wized='unitPriceToFilter']")
    FILTER_BUTTON = (By.CSS_SELECTOR, ".filter-button.w-inline-block")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, ".button-filter.w-button")

    def verify_off_plan_page_enter(self):
        expected_text = 'Total projects'
        actual_text = self.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text
        assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

    def open_page(self):
        self.driver.get('https://soft.reelly.io/')

    def open_filter(self):
        self.click(*self.FILTER_BUTTON)

    def filter_by_price(self, price1, price2):
        self.input_text(price1, *self.PRICE1_FIELD)
        self.input_text(price2, *self.PRICE2_FIELD)

    def apply_filter(self):
        self.click(*self.APPLY_FILTER_BUTTON)

    # Option 1 - Verify prices at the first page
    #def verify_price(self):
    #     projects = self.find_elements(By.CSS_SELECTOR,".price-value")
    #     for project in projects:
    #         price_text = project.text.replace("AED", "").replace(",", "").strip()
    #         price = int(price_text)
    #         assert 1200000 <= price <= 2000000, f"Product price {price} is out of range"

    # Option 2 - Verify prices at the all 7 pages, knowing that there are 7 of them
    def verify_price(self):
        total_pages = 7

        for current_page in range(1, total_pages + 1):
            print(f"Processing page {current_page}")

            # Wait for the data to load
            self.wait.until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.price-value"))
            )

            # Process the data on the page
            projects = self.find_elements(By.CSS_SELECTOR, "div.price-value")
            for project in projects:
                price_text = project.text.replace("AED", "").replace(",", "").strip()
                if price_text.isdigit():
                    price = int(price_text)
                    assert 1200000 <= price <= 2000000, f"Product price {price} is out of range"
                else:
                    raise ValueError(f"Price text '{price_text}' is not a valid number")

            # If not the last page, navigate to the next page
            if current_page < total_pages:
                next_button = self.find_element(By.CSS_SELECTOR, ".pagination__button.w-inline-block")
                next_button.click()
                # Ensure the next page has loaded completely
                self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.price-value"))
                )

        # Option 3 (must be updated!!!) - Verify prices at the all pages, not knowing how many there are

        # current_page = int(self.find_element(By.CSS_SELECTOR, "[wized='currentPageProperties']").text)
        #
        # while True:
        #     try:
        #         # Wait for the prices to be visible on the page before attempting to interact
        #         self.wait.until(
        #             EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.price-value"))
        #         )
        #         projects = self.find_elements(By.CSS_SELECTOR, "div.price-value")
        #
        #         for project in projects:
        #             price_text = project.text.replace("AED", "").replace(",", "").strip()
        #             print(f"Raw price text: '{project.text}'")
        #             print(f"Processed price text: '{price_text}'")
        #
        #             if price_text.isdigit():
        #                 price = int(price_text)
        #                 assert 1200000 <= price <= 2000000, f"Product price {price} is out of range"
        #             else:
        #                 raise ValueError(f"Price text '{price_text}' is not a valid number")
        #         sleep(8)
        #
        #         next_button = self.wait.until(
        #                       EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination__button.w-inline-block"))
        #         )
        #         next_page = int(self.find_element(By.CSS_SELECTOR, "[wized='totalPageProperties']").text)
        #
        #         if next_page == current_page:
        #             print(f'Next page: {next_page}')
        #             print(f'Current page: {current_page}')
        #             break
        #         else:
        #             # current_page = next_page
        #             next_button.click()
        #             # Ensure that the next page has loaded and prices are updated
        #             #self.wait.until(
        #            #     EC.staleness_of(projects[0])
        #             #)
        #             self.wait.until(
        #                 EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.price-value"))
        #             )
        #             self.wait.until(
        #                 EC.presence_of_element_located((By.CSS_SELECTOR, "div.price-value"))
        #             )
        #             projects = self.find_elements(By.CSS_SELECTOR, "div.price-value")
        #     except Exception as e:
        #         print(f"Encountered an error: {e}")
        #         # Optionally, capture the full traceback if the basic message isn't enough:
        #         import traceback
        #         print(traceback.format_exc())
        #         break  # Break out of the loop if there are any issues navigating pages
