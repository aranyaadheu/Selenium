from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)

# button = driver.find_element(By.XPATH, value="//label[normalize-space()='All matches']")
# button.click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='All matches']"))
).click()

# wait for the table cells to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "td"))
)

#driver.quit()
# scrape data from a table using Selenium
matches = driver.find_elements(By.TAG_NAME, value="td") # grab multiple elements

"""
date = []
home_team = []
score = []
away_team = []
"""

for match in matches:
"""
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text))
    away_team.append(match.find_element(By.XPATH, './td[4]').text)"""

    print(match.text)