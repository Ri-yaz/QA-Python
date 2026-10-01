#to perfrom drag and drop using action chains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url="https://formy-project.herokuapp.com/dragdrop"
driver.get(url)
time.sleep(1)

source_element=driver.find_element(By.XPATH,"//div[@id='image']//img")
destination_element=driver.find_element(By.XPATH,"//div[@id='box']")

actions=ActionChains(driver)
actions.drag_and_drop(source_element,destination_element).perform()
time.sleep(3)   
driver.quit()