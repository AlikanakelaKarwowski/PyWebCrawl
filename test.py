import time
import sys

#import functions to create proper date and time
from pyMonthNum import month_num
from pyMonthNum import monthFormat

#simulate mouse usage
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
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
mouse = MouseController()
keyboard = KeyboardController()
print ("Current Position" + str(mouse.position))

driver.get('https://footprints12.uakron.edu/footprints/servicedesk/login.html')
print("hover over the little x box and dont move")
time.sleep(5)
print(mouse.position)
time.sleep(10)
