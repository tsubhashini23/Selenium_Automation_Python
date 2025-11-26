import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @pytest.mark.usefixtures("browser")
# class TestCheckReport:
#
#     driver: webdriver.Chrome  # optional: removes PyCharm warnings "Unresolved attribute reference 'driver' for class 'CheckReport'" in the below statements
#
#     def test_launch_redbus(self):
#         self.driver.get("https://www.redbus.in/")
#         print(f"Current URL: {self.driver.current_url}")
#         WebDriverWait(self.driver, 10).until(
#             EC.url_contains("redbus")
#         )


class TestCheckReport:

    driver: webdriver.Chrome  # optional: removes PyCharm warnings "Unresolved attribute reference 'driver' for class 'CheckReport'" in the below statements

    def test_launch_redbus(self):
        self.driver.get("https://www.redbus.in/")
        print(f"Current URL: {self.driver.current_url}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(("id", "src")
        ))



