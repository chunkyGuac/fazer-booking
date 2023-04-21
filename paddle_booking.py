import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager, ChromeType

chrome_version = '95.0.4638'
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    executable_path=ChromeDriverManager(chrome_type=ChromeType.GOOGLE, version=chrome_version).install(),
    options=options)

from dotenv import load_dotenv

load_dotenv()

# Replace with your email and password
email = os.environ["COURT_BOOKING_EMAIL"]
password = os.environ["COURT_BOOKING_PASSWORD"]

def book_court():
    driver.get("https://app.playbypoint.com/users/sign_in")
    time.sleep(2)

    # Log in
    driver.find_element("xpath", "//input[@name='user[email]']").send_keys(email)
    driver.find_element("xpath", "//input[@name='user[password]']").send_keys(password)
    driver.find_element("xpath", "//input[@name='commit']").click()
    time.sleep(2)

    # Navigate to the booking page
    driver.find_element("css selector", "#facility_home_box > div:nth-child(1) > div.mt30.mb10 > a").click()
    time.sleep(2)

    # Select paddle tennis
    # Navigate to the booking page
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/div[2]/div/button[4]").click()
    time.sleep(2)

    # Select last date
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div/div/div/button[8]").click()
    #dates = driver.find_elements("xpath", "//div[@class='date-selector__date']")
    #dates[-1].click()
    time.sleep(2)

    # Select time slots
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[3]/div[2]/button[29]").click()
    time.sleep(1)
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[3]/div[2]/button[30]").click()
    time.sleep(1)

    # Select court
    #driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[4
