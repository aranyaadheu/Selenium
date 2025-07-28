from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://aranyaadheu.vercel.app/")
browser.maximize_window()
title = browser.title
print(title) # prints the website title.
assert "aranyaadheu" in title # to actually locate the exact title/

