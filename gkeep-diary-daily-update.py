"""Created on 12-Feb-18.
Author: Spencer
Description: gkeep-diary-daily-update.py -
"""

import time
start = time.time()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import logging
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)
logging.getLogger("selenium").setLevel(logging.WARNING)

# Chromedriver file location.
driver_location = r"C:\\Users\Spencer\Programming\cmd\chromedriver.exe"

# Opt for headless and English language
options = webdriver.ChromeOptions()
# logging.debug('running headless')
# options.set_headless(headless=True)
options.add_argument('--lang=en-GB')  # en-US didn't work, so used GB
options.add_argument(r"user-data-dir=C:\Users\Spencer\AppData\Local\Google\Chrome\User Data\Default")

# Find webdriver.Chrome wherever saved locally.
browser = webdriver.Chrome(executable_path=driver_location,
                           chrome_options=options)

# Set wait for Expected Conditions - this will be used to allow loading
wait = WebDriverWait(browser, 10)

try:
    browser.get("https://keep.google.com")
    time.sleep(8)
finally:
    browser.quit()
    print('Completed in: ' + str(time.time() - start) + ' seconds')
