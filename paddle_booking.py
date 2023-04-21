import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

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
    #driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[1]/div[4]/div/div/button[4]").click()
    #time.sleep(2)

    # Continue to next step
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[2]/div[2]/div[2]").click()
    time.sleep(2)

    # Change the number of players to 1
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div/div/button[1]").click()
    time.sleep(1)

    # Continue to next step
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/table/tbody/tr/td[2]/div[2]/div").click()
    time.sleep(2)

    # Uncheck Smart Selection
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/div[1]/div/span[5]/div").click()
    time.sleep(1)

    # Book the court
    driver.find_element("xpath", "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[3]/div[2]/table/tbody/tr/td[2]/div[1]/div[4]/div/div/div/button").click()
    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    book_court()