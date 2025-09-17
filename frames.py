import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()
print("Page title: ", driver.title)
driver.implicitly_wait(5)


# WebDriverWait(driver, 2).until(EC.alert_is_present())

# driver.switch_to.frame('singleframe')
# driver.switch_to.frame('SingleFrame')

frame_section = driver.find_element(By.ID, "singleframe")
driver.switch_to.frame(frame_section)

txt_box = driver.find_element(By.TAG_NAME, 'input')
txt_box.send_keys("test keys")
# txt_box.send_keys(Keys.RETURN)
time.sleep(2)

driver.switch_to.default_content()

time.sleep(2)

driver.find_element(By.XPATH, "//div[@class='tabpane']/ul/li[2]").click()
print("Clicked on IFrame within an IFrame button")

time.sleep(2)

driver.quit()
