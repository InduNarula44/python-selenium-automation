from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com')

driver.find_element(By.ID,"account-sign-in").click()

# driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

sleep(3)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
# driver.find_element(By.XPATH,"//button[text()='Sign in']").click()


sleep(3)
#Verification



expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH,"//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
assert expected_result in actual_result,f'Expected text {expected_result} not in actual {actual_result}'
print("Test case passed")


driver.find_element(By.ID,"login").click()







sleep(3)

driver.quit()