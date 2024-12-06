from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open Target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('User click on Sign-in button')
def click_signin_button(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    sleep(1)

@when('User click on Sign in button on the navigation page on the right side')
def click_signin_button(context):
   context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@then('Verify Sign-In Form is opened')
def verify_signin_form(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1/span").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'
