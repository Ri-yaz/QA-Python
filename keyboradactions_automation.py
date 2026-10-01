#Import modules
#import keys and perform actions from keyboard keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url="https://sagar-test-qa.vercel.app/"
driver.get(url)
time.sleep(1)

username=driver.find_element(By.ID, "username")
password=driver.find_element(By.XPATH, "//*[@id='password']")
login_button=driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

username.send_keys("admin")
time.sleep(1)
password.send_keys("password")
time.sleep(1)


actions = ActionChains(driver)
password.send_keys(Keys.TAB)  # Press Tab key to move focus to the login button
actions.send_keys(Keys.ENTER)  # Press Enter key to click the login button  
time.sleep(3)


driver.quit()