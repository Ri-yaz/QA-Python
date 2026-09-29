
#Import modules
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url="https://saucedemo.com"
driver.get(url)
time.sleep(1)

#uusing ID
username=driver.find_element(By.ID, "user-name")
password=driver.find_element(By.ID, "password")
login_button=driver.find_element(By.ID,"login-button")

#uusing css-selector
username=driver.find_element(By.CSS_SELECTOR, "#user-name")

#using Xpath
login_button=driver.find_element(By.XPATH, "//*[@id='login-button']")
username=driver.find_element(By.XPATH, "//*[@id='user-name']")

#actions
username.send_keys("standard_user")
time.sleep(3)
password.send_keys("secret_sauce")
time.sleep(2)
login_button.click()
time.sleep(3)
driver.quit()


'''
id="user-name"
id="password"
id="login-button"


Xpath:
relative: //*[@id="login-button"]
absolute: /html/body/div/div/div[2]/div[1]/div/div/form/input
//*[@id="user-name"]
//*[@id="password"]
//*[@id="login-button"]
'''