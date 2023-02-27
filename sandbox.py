import threading
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the search expression
search_expression = "OpenAI"
# Open Chrome browser
driver = webdriver.Chrome()
# Navigate to the Google site
driver.get("https://www.google.com/")
# Find the search box element
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
# Enter the search expression in the search box
search_box.send_keys(search_expression)
# Press Enter key
search_box.send_keys(Keys.RETURN)
# Wait for the search results to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)
# Find the first search result link
first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
# Click the first link
first_link.click()
# Wait for a random amount of time between 1 and 5 minutes before closing the browser
wait_time = random.randint(60, 300)
time.sleep(wait_time)
driver.quit()

