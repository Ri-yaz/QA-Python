#to scroll down the page we can use execute_script method of selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url="https://formy-project.herokuapp.com/scroll"
driver.get(url)
time.sleep(1)

# Scroll down the page
driver.execute_script("window.scrollBy(0, 800);")
time.sleep(2)

fullname=driver.find_element(By.ID,"name")
fullname.send_keys("John Doe")
time.sleep(1)
date=driver.find_element(By.ID,"date")
date.send_keys("12/12/2023")
time.sleep(1)
driver.execute_script("window.scrollTo(0, 0);")
driver.close()
driver.quit()