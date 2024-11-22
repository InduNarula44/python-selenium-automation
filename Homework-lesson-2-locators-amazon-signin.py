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

#------signin button on home page------
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()

# driver.find_element(By.XPATH,"//i[@aria-label='Amazon']").click()

#-----email--------

driver.find_element(By.ID,"ap_email").send_keys("abc@gmail.com")

#-----continue button------
driver.find_element(By.ID,"continue").click()
# driver.find_element(By.ID,"ap_password").send_keys("abc@234")

sleep(2)
#------condition of use of link and privacy notice link

driver.find_element(By.XPATH,"//a[text()='Conditions of Use']").click()
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']").click()



#------Need help link---------------
driver.find_element(By.CLASS_NAME,"a-expander-prompt").click()
#
# #-----Forgot your password and More ways to get support/Other issues with Sign-In Link by ID
#
driver.find_element(By.ID,"auth-fpp-link-bottom").click()
driver.find_element(By.ID,"ap-other-signin-issues-link").click()
#
#
# driver.find_element(By.ID,"ap-other-signin-issues-link").click()
# driver.find_element(By.XPATH,"//*[text()=' More ways to get support ']").click()
#
# ------with Xpath - Parent/child-forgot your password and More ways to get support------
# driver.find_element(By.XPATH,"//div[@aria-expanded='true']//a[@id='auth-fpp-link-bottom']").click()
# driver.find_element(By.XPATH,"//div[@aria-expanded='true']//a[@id='ap-other-signin-issues-link']").click()


#-------Create Your Amazon Account by ID-----------

driver.find_element(By.ID,'createAccountSubmit').click()



sleep(3)

driver.quit()





