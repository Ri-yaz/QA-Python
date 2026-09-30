from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url = "https://formy-project.herokuapp.com/autocomplete"
driver.get(url)
time.sleep(1)

address = driver.find_element(By.ID, "autocomplete")
street_address = driver.find_element(By.ID, "street_number")
street_address2 = driver.find_element(By.ID, "route")
city = driver.find_element(By.XPATH, "//input[@id='locality']")
state = driver.find_element(By.XPATH, "//input[@id='administrative_area_level_1']")
zipcode = driver.find_element(By.ID, "postal_code")
country=driver.find_element(By.ID,"country")

address.send_keys("bhaktapur")
time.sleep(2)  # Wait for the autocomplete suggestions to appear
street_address.send_keys("01 kamalbinayak")
time.sleep(1)  # Wait for the street address to be filled
street_address2.send_keys("Bhatekpati")
time.sleep(1)  # Wait for the street address 2 to be filled
city.send_keys("Bhaktapur")
time.sleep(1)  # Wait for the city to be filled
state.send_keys("Bagmati")
time.sleep(1)  # Wait for the state to be filled
zipcode.send_keys("44800")  
time.sleep(1)  # Wait for the zipcode to be filled
country.send_keys("Nepal")

driver.quit()