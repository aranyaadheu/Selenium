# fetch name from the website. 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

PATH = "C:\\Windows\\chromedriver.exe"

# set up the chrome driver service
service = Service(PATH)
options = Options()

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://aranyaadheu.vercel.app")

print(driver.title)
driver.quit()
