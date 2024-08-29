from behave import given, when, then
from time import sleep

@given('Open Off-plan page')
def open_off_plan_page(context):
    context.app.off_plan_page.open_page()


@when('Verify the right page opens')
def verify_sign_in_form(context):
    context.app.off_plan_page.verify_off_plan_page_enter()
    sleep(4)


@then('Open filter menu')
def open_filter_menu(context):
    context.app.off_plan_page.open_filter()


@then('Filter the products by price range from {price1} to {price2} AED')
def filter_products_by_price_range(context, price1, price2):
    context.app.off_plan_page.filter_by_price(price1, price2)
    sleep(4)


@then('Apply Filter')
def click_apply_filter(context):
    context.app.off_plan_page.apply_filter()
    sleep(10)


@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def verify_price_in_all_projects(context):
    context.app.off_plan_page.verify_price()
