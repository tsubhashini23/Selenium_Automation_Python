import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()
print("Page title: ", driver.title)
driver.implicitly_wait(2)

driver.find_element(By.ID, "email").send_keys("tsubha1@gmail.com")
driver.find_element(By.ID, "enterimg").click()

driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Subhashini")
# //* ----> Matches any element
# //input
# (//input)[1]
# (//input)[last()]
# (//input[@type='text'])[2]
# //input[@id='email']
# //input[@id='email' and @type='text']
# //input[@id='email' or @name='userEmail']
# //label[text()='Full Name*']
# //label[contains(text(),'word')]
# //form[@id='basicBootstrapForm']/child::div[1]/div[1]---->Gives the childs of form tag
# //form[@id='basicBootstrapForm']/child::div ( Similar to //form[@id='basicBootstrapForm']/div )
# //form[@id='basicBootstrapForm']/parent::div---->Gives the direct parent of form tag
# //form[@id='basicBootstrapForm']/ancestor::div-->Gives all the parent tags(eg, div tags) up in the hierarchy until the root
# //form[@id='basicBootstrapForm']/ancestor::*-->Gives all the parent tags(eg, html, head, div) up in the hierarchy until the root
# //form[@id='basicBootstrapForm']/descendant::div ( similar to //form[@id='basicBootstrapForm']//div )
# //input[@id='checkbox1']/following-sibling::label
# //label[text()='Movies ']/preceding-sibling::input
# //label[normalize-space(text())='Movies']/preceding-sibling::input-->Removes extra spaces
# input[contains(@placeholder, 'name')]
# input[starts-with(@placeholder, 'name')]
# input[ends-with(@placeholder, 'name')]
# //*[@id='email')

# Logical combinations
# //input[@id='name' or contains(@placeholder, 'name')]
# input[text()='name' and starts-with(@id, 'user')]


#Using not
# //input[not(@type='text')]

driver.find_element(By.XPATH, "//*[@placeholder='Last Name']").send_keys("Thirumalavan")
# //div[@placeholder='Last Name']/parent::form

driver.find_element(By.XPATH, "//*[@type='email' and @ng-model='EmailAdress']").send_keys("test@gmailcom")

driver.find_element(By.XPATH, "//input[@value= 'FeMale']")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


#Select Multiple checkbox, find_elements

element_list = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")

for element in element_list:
    val = element.get_attribute('value')
    print(val)
    # if val == 'Movies':
    element.click()



# Select class
dropdown_element = driver.find_element(By.XPATH, "//select[@id = 'Skills']")
click_dropdown_element = Select(dropdown_element)

click_dropdown_element.select_by_index(1)

click_dropdown_element.select_by_value('Android')

click_dropdown_element.select_by_visible_text('Art Design')

print(driver.current_url)

driver.get("https://www.google.com/?zx=1757678760816&no_sw_cr=1")

print(driver.current_url)

driver.back()

print(driver.current_url)

driver.refresh()

driver.forward()

print(driver.current_url)


driver.quit()