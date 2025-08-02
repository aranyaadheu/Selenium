from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

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
    EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr"))
)

#driver.quit()
# scrape data from a table using Selenium
matches = driver.find_elements(By.XPATH, value="//table/tbody/tr") # grab multiple elements
# find all rows
# rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

# lists to store data
date = []
home_team = []
score = []
away_team = []

for match in matches:
    tds = match.find_elements(By.TAG_NAME, "td")
    if len(tds) >= 4:
        date.append(tds[0].text)
        home_team.append(tds[1].text)
        away_team.append(tds[2].text)
        score.append(tds[3].text)
        print(f"{tds[0].text} | {tds[1].text} | {tds[2].text} | {tds[3].text}")

driver.quit()

df = pd.DataFrame(
    {
        'date': date,
        'home_team': home_team,
        'score': score,
        'away_team': away_team,
    }
)

df.to_csv('football_data.csv', index=False)
print(df)