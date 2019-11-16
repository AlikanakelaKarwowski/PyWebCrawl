
import time
import sys

#import functions to create proper date and time
from pyMonthNum import month_num
from pyMonthNum import monthFormat

#simulate mouse usage
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController

#import selenium for web browser usage
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login_Function(mouse, driver):
    #closes the automation method
    mouse.position = (745,104)
    mouse.click(Button.left, 2)
    #finds login box
    login_id = driver.find_element_by_name('username')
    username = input("What is your username: ")
    #sends username to box
    login_id.send_keys(username)
    #finds password box
    login_pass = driver.find_element_by_name('password')
    password = input('What is your password: ')
    #sends password to box
    login_pass.send_keys(password)
    #clicks login button
    mouse.position = (394, 361)
    mouse.click(Button.left, 2)
    #wait for loading
    time.sleep(30)

def ticketing(mouse):
    #moves to view and clicks
    mouse.position = (655, 314)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(3)

    #moves to cdma
    mouse.position = (674, 346)
    time.sleep(1)

    #moves to computers and clicks
    mouse.position = (530, 349)
    time.sleep(1)
    mouse.click(Button.left, 1)

    #wait for loading
    time.sleep(3)

    #move to last page and clicks
    mouse.position = (274, 797)
    time.sleep(3)
    mouse.click(Button.left, 1)

    #wait for loading
    time.sleep(3)

def ticket_auto(mouse, driver):
    #move to the first ticket number and clicks
    mouse.position = (366, 434)
    time.sleep(1)
    mouse.click(Button.left, 1)

    #wait for loading
    time.sleep(3)

    #get the serial number value and return as a string
    serial_box = driver.find_element_by_name('serial_number')
    serial_number = serial_box.get_attribute('value')
    return serial_number

def warranty_search(timeout, keyboard, serial, driver2, intialized):
    if intialized == true:
        keyboard.press(Key.alt)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.alt)

    #get search box and send it the serial number
    id_box = driver2.find_element_by_name('search-input')
    id_box.send_keys(serial)

    #click the search button by element id
    btn = driver2.find_element_by_id('btnSearch')
    btn.click()

    #wait for page to load element
    element_present = EC.presence_of_element_located((By.ID, 'warrantyExpiringLabel'))
    #wait some more not really
    WebDriverWait(driver2, timeout).until(element_present)

    #find the expiration date
    exp_date = driver2.find_element_by_id('warrantyExpiringLabel')
    date = exp_date.text

    #convert the date to proper formating
    date = monthFormat(date)
    #return the date
    return date

def ticket_fill(date, driver, mouse):
    #find expiration box and send in the date
    exp_box = driver.find_element_by_name('date_warranty_expires')
    exp_box.send_keys(date)

    #find warranty_type and send in "Dell"
    war_box = driver.find_element_by_name('warranty_type')
    war_box.send_keys('Dell')

    #find the requisition number box and send in unknown
    req_box = driver.find_element_by_name('requisition_number')
    req_box.send_keys('unknown')

    #move to submit and click submit
    mouse.position = (74, 350)
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(3)
    print("Happy Time")

#counter for looping
i = 0
#using chrome driver
driver = Chrome()
#amount of time to wait for the page to load (in seconds)
timeout = 7

intialized= "false"
#mouse object
mouse = Controller()
keyboard = KeyboardController()

driver.get('https://footprints12.uakron.edu/footprints/servicedesk/login.html')

login_Function(mouse, driver)

ticketing(mouse)
driver2 = Chrome()
driver2.get('https://dell.com/support/home/us/en/04/')
#tab out to the other page
keyboard.press(Key.alt)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.release(Key.alt)
while i <  25:
    #click the current ticket
    serial = ticket_auto(mouse, driver)
    #get the date
    date = warranty_search(timeout, keyboard, "123wer", driver2, intialized )
    #tab out to the other page
    #submit the information
    ticket_fill(date, driver, mouse)
    intialized = "true"
    i +=1
