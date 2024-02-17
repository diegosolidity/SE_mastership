import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.execute_script("document.getElementById('datepicker').value='25/11/2024'")

time.sleep(5)

driver.quit()

