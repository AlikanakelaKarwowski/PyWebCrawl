
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

#----------------------------------#
#------Global Mouse Positions------#
#----------------------------------#
#p1 = the close automation window
p1 = (934, 100)
#p2 = login Button
p2 = (486, 446)
#p3 = cmdb hover
p3 = (676, 310)
#p4 = move to computers
p4 = (839, 310)
#p5 = move to last page
p5 = (275, 1015)
#p6 = click first ticket
p6 = (366, 374)
#p7 = submit Button
p7 = (72, 291)
#----------------------------------#
#----------------------------------#
def login_Function(mouse, driver, p1,p2):
    #closes the automation method
    mouse.position = p1
    mouse.click(Button.left, 2)
    time.sleep(1)
    #finds login box and sends the username to the box
    login_id = driver.find_element_by_name('username')
    login_id.send_keys(username)

    #finds password box and sends the password to the box
    login_pass = driver.find_element_by_name('password')
    login_pass.send_keys(password)

    #clicks login button, it doesnt always work so click it to hell
    mouse.position = p2
    time.sleep(1)
    mouse.click(Button.left, 5)

    #wait for page to load element
    #element_present = EC.presence_of_element_located((By.classname(), "x-grid-item-container"))
    #wait some more not really
    #WebDriverWait(driver, 45).until(element_present)

    #wait for loading
    time.sleep(40)

def ticketing(mouse, driver,p3,p4,p5):

    #moves to view and clicks
    driver.find_element_by_id("tab-1064").click()

    #moves to cmdb
    mouse.position = p3
    time.sleep(3)

    #moves to computers and clicks
    mouse.position = p4
    time.sleep(1)
    mouse.click(Button.left, 1)

    #wait for loading
    time.sleep(3)

    #move to last page and clicks
    mouse.position = p5
    time.sleep(1.5)
    mouse.click(Button.left, 1)

    #wait for loading
    time.sleep(3)

def ticket_auto(mouse, driver, p6):
    #move to the first ticket number and clicks
    mouse.position = p6
    time.sleep(1)
    mouse.click(Button.left, 1)

    #wait for loading
    time.sleep(3)

    #get the serial number value and return as a string
    serial_box = driver.find_element_by_name('serial_number')
    serial_number = serial_box.get_attribute('value')
    return serial_number

def warranty_search(timeout, keyboard, serial,driver2):
    #create driver for new chrome page
    try:
        driver2.get('https://dell.com/support/home/us/en/04/')
        time.sleep(1.5)

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

        #tab out to the other page
        keyboard.press(Key.alt)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.alt)

    except:
        warranty_search(timeout,keyboard, serial, driver2)
    else:
        #return the date
        return date

def ticket_fill(date, driver, mouse,p7):
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
    mouse.position = p7
    time.sleep(1)
    mouse.click(Button.left, 1)
    time.sleep(3)
    print("Ticket updated")

#driver.get('https://footprints12.uakron.edu/footprints/servicedesk/login.html')
# main program loop
def queryOnce(driver, driver2, p1, p2, p3, p4, p5, p6, p7):
    while True:
        try:
            #mouse object
            mouse = Controller()
            keyboard = KeyboardController()
            driver.get('https://footprints12.uakron.edu/footprints/servicedesk/login.html')

            login_Function(mouse, driver, p1,p2)
            ticketing(mouse, driver, p3, p4, p5)

            while True:
                #click the current ticket
                serial = ticket_auto(mouse, driver, p6)
                #get the date
                #amount of time to wait for the page to load (in seconds)
                timeout = 5
                date = warranty_search(timeout, keyboard, serial,driver2)
                #submit the information
                ticket_fill(date, driver, mouse, p7)
        except:
            pass
        else:
            break

# repeat loop in case of crashing
def queryRepeadetly(driver, driver2, p1, p2, p3, p4, p5, p6, p7):
    while True:
        queryOnce(driver, driver2, p1, p2, p3, p4, p5, p6, p7)
        time.sleep(5)

#using chrome driver
driver = Chrome()
driver.set_window_size(974,1047)
driver.set_window_position(-7,0)
driver2 = Chrome()
driver2.set_window_position(904, 453)
driver2.set_window_size(1030, 747)
queryRepeadetly(driver, driver2, p1, p2, p3, p4, p5, p6, p7)
