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

driver.get('https://www.amazon.com')
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()

driver.find_element(By.ID,"createAccountSubmit").click()
#
#
# locator for amazon sign using CSS by class
driver.find_element(By.CSS_SELECTOR,'.a-icon.a-icon-logo')


#Locator for create login page using by ID
driver.find_element(By.ID,"ap_customer_name").send_keys("Indu Narula")
driver.find_element(By.ID,"ap_email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"ap_password").send_keys("abc12345")
driver.find_element(By.ID,"ap_password_check").send_keys("abc12345")
driver.find_element(By.ID,"continue")
#
#
# #Locator for amazon create login page by using CSS
# driver.find_element(By.CSS_SELECTOR,"input.a-input-text[aria-describedby='ap_customer_name_context_message_section']").send_keys("Jas")
# driver.find_element(By.CSS_SELECTOR,"input[class='a-input-text.a-span12.auth-autofocus.auth-required-field.a-form-error']").send_keys('Indu')
# driver.find_element(By.CSS_SELECTOR,"#ap_customer_name").send_keys("Indu Narula")
# driver.find_element(By.CSS_SELECTOR,'input.a-input-text.a-span12.auth-autofocus.auth-required-field.a-form-error').send_keys("Rajvir")
# driver.find_element(By.CSS_SELECTOR,"input[aria-describedby='ap_customer_name_context_message_section']").send_keys("Raj")
# driver.find_element(By.CSS_SELECTOR,"#ap_email").send_keys("abchn@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"#ap_password").send_keys("abc12345")
# driver.find_element(By.CSS_SELECTOR,"#ap_password_check").send_keys("abc12345")
# driver.find_element(By.CSS_SELECTOR,"#continue").click()


#
#
# #driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']").click()
# #locator for condition of use link
# driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']").click()
#
# #locator for privacy link

# driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']").click()

# driver.find_element(By.XPATH,"//a[text()='Conditions of Use']").click()

driver.find_element(By.XPATH,"//a[text()='Privacy Notice']").click()
sleep(4)


