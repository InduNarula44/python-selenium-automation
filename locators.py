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

#find element by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID,'nav-search-submit-button')

#find element by Xpath
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH,"//input[@role='searchbox']")
driver.find_element(By.XPATH,"//input[@tabindex='0']")

#find element by Xpath , any tag but with attribute
driver.find_element(By.XPATH,"//*[@role='searchbox']")


#Xpath by multiple attributes.
driver.find_element(By.XPATH,"//input[@tabindex='0'and @name='field-keywords' and @dir='auto' ]")


driver.find_element(By.XPATH,"//select[@aria-describedby='searchDropdownDescription']")
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']").click()
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']").click()



