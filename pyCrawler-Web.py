
import time
import sys

#import selenium for web browser usage
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

#using chrome drive
i = 5
sys.stdout = open('output.txt', 'w')
driver = Chrome()
while i < 10:
    driver.get("https://dell.com/support/home/us/en/04/")

    #root folder for submission directory
    id_box = driver.find_element_by_name('search-input')
    id_box.send_keys('5w2tms1')
    btn = driver.find_element_by_id('btnSearch')
    btn.click()
    time.sleep(3)
    exp_date = driver.find_element_by_id('warrantyExpiringLabel')
    date = exp_date.text
    print(date)
    i +=1
