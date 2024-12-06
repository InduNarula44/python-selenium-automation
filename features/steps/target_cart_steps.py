from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('User Clicks on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()
    sleep(5)

@then('Verify "Your Cart is empty" message is shown')
def verify_cart_is_empty(context):
    expected_result= 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH,"//*[text()='Your cart is empty']").text
    assert expected_result in actual_result,f'Expected text{expected_result} not in actual {actual_result}'
    print("test case passed")