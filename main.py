from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
# options.add_argument("--window-size=500,500")
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#-----------------------------------------------------------#
#-----------------------------------------------------------#
driver.get("https://www.nintendo.com/")
print(driver.title)
driver.quit()