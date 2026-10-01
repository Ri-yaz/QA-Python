from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url="https://formy-project.herokuapp.com/buttons"
driver.get(url)
time.sleep(1)


primary_button=driver.find_element(By.XPATH,"//button[normalize-space()='Primary']")
Success_button=driver.find_element(By.XPATH,"//button[normalize-space()='Success']")
Info_button=driver.find_element(By.XPATH,"//button[normalize-space()='Info']")
Warning_button=driver.find_element(By.XPATH,"//button[normalize-space()='Warning']") 
Danger_button=driver.find_element(By.XPATH,"//button[normalize-space()='Danger']") 
Link_button=driver.find_element(By.XPATH,"//button[normalize-space()='Link']") 
left_button=driver.find_element(By.XPATH,"//button[normalize-space()='Left']")
right_button=driver.find_element(By.XPATH,"//button[normalize-space()='Right']")    
middle_button=driver.find_element(By.XPATH,"//button[normalize-space()='Middle']")
one_button=driver.find_element(By.XPATH,"//button[normalize-space()='1']") 
two_button=driver.find_element(By.XPATH,"//button[normalize-space()='2']")
dropdown_button=driver.find_element(By.ID,"btnGroupDrop1")
primary_button.click()
time.sleep(1)
Success_button.click()
time.sleep(1)
Info_button.click()
time.sleep(1)
Warning_button.click()
time.sleep(1)
Danger_button.click()
time.sleep(1)
Link_button.click()
time.sleep(1)
left_button.click()
time.sleep(1)
right_button.click()
time.sleep(1)
middle_button.click()
time.sleep(1)
one_button.click()
time.sleep(1)
two_button.click()
time.sleep(1)
dropdown_button.click()
time.sleep(1)

driver.quit()