from pynput.mouse import Listener
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

import logging

logging.basicConfig(filename=("mouse_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Position ({0}, {1})'.format(x, y,))

with Listener(on_click=on_click) as listener:
    driver = Chrome()
    driver.set_window_size(974,1047)
    driver.set_window_position(-7,0)
    driver.get('https://footprints12.uakron.edu/footprints/servicedesk/login.html')
    print("Close out of the automation banner. Login in. click view. click cdma. click computers. click last page. click first ticket. then click just above submit. When you are done close out of the console and open the log file")
    listener.join()
