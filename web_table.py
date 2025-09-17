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
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

select_date = "22-Sep-2025"

dates = select_date.split("-")
print(dates)

driver.find_element(By.ID, 'jDate').click()

td = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar ng-tns-c59-10']//a")

time.sleep(2)
for d in td:
    print(d.text)
    if d.text == dates[0]:
        d.click()
        break


time.sleep(2)

driver.quit()
