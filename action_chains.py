import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

#custom options

# chr_options = Options()
# chr_options.add_experimental_option("detach", True)
# chr_options.add_argument("--headless")
#
#
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),  # Auto-manages chromedriver
#     options=chr_options                                # Pass custom options
# )

driver=webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.maximize_window()

actions = ActionChains(driver)

kids = driver.find_element(By.XPATH, "//a[@href='/shop/kids']")

time.sleep(2)
actions.move_to_element(kids).perform()

tshirts = driver.find_element(By.XPATH, "//div[@data-reactid='333']/div/div/div/div/li/ul/li[2]/a")

actions.click(tshirts).perform()

time.sleep(2)

search = driver.find_element(By.XPATH, "//div[@class='desktop-query']/input")

actions.click(search).key_up(Keys.SHIFT).send_keys("hellcat").key_down(Keys.SHIFT).send_keys(Keys.ENTER).perform()

time.sleep(5)

driver.quit()