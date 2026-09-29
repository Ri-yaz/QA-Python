#Import modules
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
url="https://sagar-test-qa.vercel.app/about.html"
driver.get(url)
time.sleep(1)

fullname=driver.find_element(By.ID, "fullname")
phone=driver.find_element(By.ID, "phone")
email=driver.find_element(By.ID, "email") 
hobby=driver.find_element(By.ID, "hobby")
submit_button=driver.find_element(By.XPATH, "//button[@type='submit']")

fullname.send_keys("Riyaz Karmacharya")
time.sleep(1)
phone.send_keys("1234567890")
email.send_keys("riyaz.karmacharya@example.com")
time.sleep(1)
hobby.send_keys("Reading")
submit_button.click()
time.sleep(3)

driver.quit()