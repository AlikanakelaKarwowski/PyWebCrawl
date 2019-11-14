
import time
import sys
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
#using chrome driver
i = 0
#sys.stdout = open('output.txt', 'w')
driver = Chrome()
timeout = 5
while i < 2:
    driver.get("https://dell.com/support/home/us/en/04/")

    #root folder for submission directory
    id_box = driver.find_element_by_name('search-input')
    id_box.send_keys('5w2tms1')

    btn = driver.find_element_by_id('btnSearch')
    btn.click()

    element_present = EC.presence_of_element_located((By.ID, 'warrantyExpiringLabel'))

    WebDriverWait(driver, timeout).until(element_present)

    exp_date = driver.find_element_by_id('warrantyExpiringLabel')
    date = exp_date.text

    date = monthFormat(date)
    print("Tyler is expired past " + date)
    i +=1
driver.close()
