import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Alerts.html")

driver.maximize_window()
print("Page title: ", driver.title)
driver.implicitly_wait(2)

# driver.find_element(By.XPATH, "//a[@href='SwitchTo.html']")

driver.find_element(By.ID, "OKTab").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()

# Explicit wait for alert
WebDriverWait(driver, 2).until(EC.alert_is_present())
driver.switch_to.alert.accept()
print("Accepted")

driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()

driver.find_element(By.ID, "CancelTab").click()

WebDriverWait(driver, 2).until(EC.alert_is_present())
driver.switch_to.alert.dismiss()
print("Dismissed")

driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()

driver.find_element(By.ID, "Textbox").click()
WebDriverWait(driver, 2).until(EC.alert_is_present())
txt = driver.switch_to.alert.text
print(txt)

WebDriverWait(driver, 2).until(EC.alert_is_present())
driver.switch_to.alert.send_keys('test')
WebDriverWait(driver, 2).until(EC.alert_is_present())
driver.switch_to.alert.dismiss()
print("Sent Keys")








