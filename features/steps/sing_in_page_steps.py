from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@given('Open Reelly main page')
def open_google(context):
    context.driver.get('https://www.reelly.io')
    sleep(2)


@when('Click Open in Browser')
def click_open_browser(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='https://soft.reelly.io/sign-in']").click()


@when('Enter email {email} and {password}')
def input_email_and_password(self, email, password):
    # self.input_text(email, *self.EMAIL_INPUT_FIELD) .send_keys(email)
    # self.input_text(password, *self.PASS_INPUT_FIELD).send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "#email-2").send_keys(email)
    self.driver.find_element(By.CSS_SELECTOR, "#field" ).send_keys(password)
   # sleep(2)


@when('Click Continue Button')
def click_continue_button(context):
    context.driver.find_element(By.CSS_SELECTOR, ".login-button.w-button").click()
    sleep(2)


@then('Verify user is logged in')
def verify_sign_in_form(context):
    expected_text = 'Total projects'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".page-title.off_plan").text
    assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'