from  selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
url="https://sagar-test-qa.vercel.app/contact.html"
driver.get(url)
time.sleep(1)   

yourname=driver.find_element(By.ID, "name")
youremail=driver.find_element(By.ID, "email")
message=driver.find_element(By.XPATH, "//textarea[@id='message']")
send_message=driver.find_element(By.XPATH, "//button[@type='submit']")

yourname.send_keys("Riyaz Karmacharya")
time.sleep(1)
youremail.send_keys("riyaz.karmacharya@example.com")
time.sleep(1)
message.send_keys("Hello, this is a test message.")
time.sleep(1)
send_message.click()
time.sleep(3)

driver.quit()