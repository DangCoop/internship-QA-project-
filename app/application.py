from pages.base_page import Page
from pages.wellcome_page import WellcomePage
from pages.sing_in_page import SingInPage
from pages.off_plan_page import OffPlanPage

class Application:
    def __init__(self, driver):

        self.page = Page(driver)
        self.wellcome_page = WellcomePage(driver)
        self.sing_in_page = SingInPage(driver)
        self.off_plan_page = OffPlanPage(driver)
