
import time
import sys

#import functions to create proper date and time
from pyMonthNum import month_num
from pyMonthNum import monthFormat

#import selenium for web browser usage
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#counter for looping
i = 0

#using chrome driver
driver = Chrome()
#amount of time to wait for the page to load (in seconds)
timeout = 5
def getExpiration(driver_type, time, i):
    while i < 2:
        driver_type.get("https://dell.com/support/home/us/en/04/")

        #root folder for submission directory
        id_box = driver_type.find_element_by_name('search-input')
        id_box.send_keys('5w2tms1')

        btn = driver_type.find_element_by_id('btnSearch')
        btn.click()

        element_present = EC.presence_of_element_located((By.ID, 'warrantyExpiringLabel'))

        WebDriverWait(driver_type, time).until(element_present)

        exp_date = driver_type.find_element_by_id('warrantyExpiringLabel')
        date = exp_date.text

        date = monthFormat(date)
        print("Tyler is expired past " + date)
        i +=1
getExpiration(driver,timeout, i)
driver.close()
