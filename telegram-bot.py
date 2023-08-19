from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


print("sample test case started")

# Replace this with the actual path to the chromedriver.exe file
chrome_driver_path = 'chromedriver_win32 (1)/chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
driver.get("https://www.google.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("pornhub")

time.sleep(10)
search = driver.find_element(By.NAME, "btnK")
search.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()

print("sample test case successfully completed")
