import time
from selenium import webdriver

# test this on multiple screen sizes
# multiple different different viewports.

#viewports will change in preferred sizes.
viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]


driver = webdriver.Chrome()
driver.get("https://www.google.com/")

# driver.set_window_size(768,1024)
# time.sleep(3)

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(4)

finally:
    driver.close()

