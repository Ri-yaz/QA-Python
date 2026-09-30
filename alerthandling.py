#Import modules
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

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
password.send_keys("password")
login_button.click()
time.sleep(3)

driver.quit()

alert=driver.switch_to.alert
alert.accept()  # Accept the alert
time.sleep(2)  # Wait for the page to load after clicking the login button
driver.quit()