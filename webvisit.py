#IMport modules
from selenium import webdriver
import time
#initialize driver
driver=webdriver.Brave()
time.sleep(1)

#maximize window
driver.maximize_window()

#delay execution using time module 
driver.get("https://www.google.com")
time.sleep(2)

#navigates to url
driver.get(url)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()

#refresh
driver.refresh()

#visit saucedemo webpage
driver.get("https://www.saucedemo.com/")

#print title and current url
print(driver.title)
print(driver.current_url)

#Quit Driver and browser
driver.quit() 