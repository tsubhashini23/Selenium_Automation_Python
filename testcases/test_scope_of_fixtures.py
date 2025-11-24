import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#FIXTURE CALLS ANOTHER FIXTURE

# @pytest.fixture(scope="function")
# def launch_browser():
#   options = Options()
#   # options.add_experimental_option("detach",True)
#   options.add_argument("--start-maximized")
#   driver = webdriver.Chrome(
#       service=Service(ChromeDriverManager().install()),
#       options=options
#   )
#   # driver = webdriver.Chrome()
#   yield driver
#   driver.quit()

# @pytest.fixture()  #default scope is "function" if not mentioned explicitly
# def test_launch_url(launch_browser):
#    launch_browser.get("https://www.redbus.in/")
#    time.sleep(5)
#    yield launch_browser
#
#
# def test_print_url(test_launch_url):
#     print(f"Current URI is {test_launch_url.current_url}")



#FIXTURE WITH SCOPE = CLASS

@pytest.fixture(scope="class")
def launch_browser_two(request):
  options = Options()
  # options.add_experimental_option("detach",True)
  options.add_argument("--start-maximized")
  driver = webdriver.Chrome(
      service=Service(ChromeDriverManager().install()),
      options=options
  )
  # driver = webdriver.Chrome()
  request.cls.driver = driver    #attach driver to the class
  yield driver
  driver.quit()


@pytest.mark.usefixtures("launch_browser_two")
class TestScopeOfFixtures:

    def test_launch_myntra(self):
        self.driver.get("https://www.myntra.com/")
        time.sleep(5)

    def test_print_myntra_url(self):
        print(f"Current URL: {self.driver.current_url}")
