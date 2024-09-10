from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
SEARCH_SUBMIT_MOBILE = (By.CSS_SELECTOR, "[data-ved='0ahUKEwjI45awubeIAxVwhP0HHZ7bDGQQ4dUDCA4']")


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    #context.driver.find_element(*SEARCH_SUBMIT).click()
    search_button = context.driver.find_element(*SEARCH_SUBMIT_MOBILE)
    context.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
    search_button.click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
