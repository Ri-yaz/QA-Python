from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


driver = webdriver.Chrome()
driver.maximize_window()
url="https://www.saucedemo.com/"
driver.get(url)
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

wait = WebDriverWait(driver, 10)  # Wait for a maximum of 10 seconds
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))  # Wait until the login button is clickable

username.send_keys("standard_user")
password.send_keys("secret_sauce")  
login_button.click()

if "https://www.saucedemo.com/inventory.html" in driver.current_url:
    print("Login successful. Current URL:", driver.current_url)
else:
    print("Login failed. Current URL:", driver.current_url)
driver.quit()