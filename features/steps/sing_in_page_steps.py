from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Reelly wellcome page')
def open_google(context):
    #context.driver.get('https://www.reelly.io')
    context.app.wellcome_page.open()
    sleep(2)


@when('Click Open in Browser')
def click_open_browser(context):
    #context.driver.find_element(By.CSS_SELECTOR, "[href*='https://soft.reelly.io/sign-in']").click()
    context.app.wellcome_page.click_button()


@when('Enter email {email} and {password}')
def input_email_and_password(context, email, password):
    context.app.sing_in_page.enter_email_and_pass(email, password)
    # self.driver.find_element(By.CSS_SELECTOR, "#email-2").send_keys(email)
    # self.driver.find_element(By.CSS_SELECTOR, "#field").send_keys(password)


@when('Click Continue Button')
def click_continue_button(context):
    context.app.sing_in_page.click_cont_button()
    #context.driver.find_element(By.CSS_SELECTOR, ".login-button.w-button").click()
    #sleep(2)


@then('Verify user is logged in')
def verify_sign_in_form(context):
    context.app.off_plan_page.verify_off_plan_page_enter()
    # expected_text = 'Total projects'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text
    # assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'