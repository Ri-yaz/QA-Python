from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/frames")

# Find frames
frames = driver.find_elements(By.TAG_NAME, "iframe")

# Switch to second frame
driver.switch_to.frame(frames[1])

# Scroll inside the frame
driver.execute_script("window.scrollTo(0, 500);")

time.sleep(2)