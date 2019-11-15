
import time
import sys

#import functions to create proper date and time
from pyMonthNum import month_num
from pyMonthNum import monthFormat

#simulate mouse usage
from pynput.mouse import Button, Controller
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
#mouse object
mouse = Controller()

print ("Current Position" + str(mouse.position))

driver.get('https://footprints12.uakron.edu/footprints/servicedesk/login.html')

login_id = driver.find_element_by_name('username')
username = input("What is your username: ")
login_id.send_keys(username)

login_pass = driver.find_element_by_name('password')
password = input('What is your password: ')
login_pass.send_keys(password)

login_btn = driver.find_element_by_id('btnLogin')
login_btn.click()

mouse.position = (655, 244)

time.sleep(3)

mouse.click(Button.left, 1)

time.sleep(3)

mouse.position = (696, 297)

mouse.position = (831, 300)

time.sleep(3)

mouse.click(Button.left, 1)

time.sleep(3)

mouse.position = (275, 1011)

time.sleep(3)

mouse.click(Button.left, 1)

time.sleep(3)

mouse.position = (365, 365)

time.sleep(3)

mouse.click(Button.left, 1)

time.sleep(3)

serial_box = driver.find_element_by_name('serial_number')
serial_number = serial_box.get_attribute('value')

driver.get('https://dell.com/support/home/us/en/04/')

#link_id = driver.find_elements_by_xpath('//*[@id="tableview-1298-record-14300"]/tbody/tr/td[3]/div')

id_box = driver.find_element_by_name('search-input')
id_box.send_keys(serial_number)

btn = driver.find_element_by_id('btnSearch')
btn.click()

element_present = EC.presence_of_element_located((By.ID, 'warrantyExpiringLabel'))

WebDriverWait(driver, timeout).until(element_present)

exp_date = driver.find_element_by_id('warrantyExpiringLabel')
date = exp_date.text

date = monthFormat(date)
print("Tyler has been expired since: " + date)

driver.close()
