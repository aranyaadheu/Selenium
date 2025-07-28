# interact w/ browser through commands.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.minimize_window()
# driver.fullscreen_window()
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
time.sleep(5)
driver.back();
time.sleep(5)
driver.forward();
time.sleep(5)
driver.back();
time.sleep(5)
driver.refresh();
driver.quit()
# driver.close()