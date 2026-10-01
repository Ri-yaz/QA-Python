
#Import modules
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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

#mouseactions 
actions = ActionChains(driver)
actions.move_to_element(login_button).click().perform()
time.sleep(3)
actions.context_click(login_button).perform()
time.sleep(3)
actions.double_click(login_button).perform()


#dropdown
sort_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Sort products']")
select=Select(sort_dropdown)
select.select_by_value("lohi")
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