import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")

driver.maximize_window()
print("Page title: ", driver.title)
driver.implicitly_wait(5)

parent = driver.current_window_handle
print(parent)

driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

windows = driver.window_handles
print(windows)
# time.sleep(2)
for win in windows:
    if win!=parent:
        driver.switch_to.window(win)
# time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='/downloads']").click()
time.sleep(2)
driver.switch_to.window(parent)
time.sleep(2)
driver.quit()
