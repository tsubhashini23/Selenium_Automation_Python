from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")

driver.find_element(By.ID, "email").send_keys("tsubha1@gmail.com")
driver.find_element(By.ID, "enterimg").click()

driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Subhashini")
# All possible XPATHs for Full Name
# (//input)[1]
# //form[@id='basicBootstrapForm']/child::div[1]/div[1]

driver.find_element(By.XPATH, "//*[@placeholder='Last Name']").send_keys("Thirumalavan")
# //div[@placeholder='Last Name']/parent::form

driver.find_element(By.XPATH, "//*[@type='email' and @ng-model='EmailAdress']").send_keys("test@gmailcom")

driver.quit()