from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

url="https://formy-project.herokuapp.com/switch-window"
driver.get(url)
time.sleep(1)

open_new_tab_button=driver.find_element(By.ID,"new-tab-button")

open_new_tab_button.click()
time.sleep(2)

windows=driver.window_handles
print("All windows: ",windows)
driver.switch_to.window(windows[1])

print("driver is in this window: ",driver.current_window_handle)

assert "https://formy-project.herokuapp.com/switch-window" in driver.current_url, "window is not switched"
driver.quit()