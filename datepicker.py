from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url="https://formy-project.herokuapp.com/datepicker"
driver.get(url)
time.sleep(1)
date=driver.find_element(By.ID,"datepicker")
date.send_keys("12/12/2023")
time.sleep(1)