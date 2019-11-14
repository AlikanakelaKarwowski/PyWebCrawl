
import time
import sys
from pyMonthNum import month_num
from pyMonthNum import monthFormat
#import selenium for web browser usage
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

#using chrome driver
i = 0
#sys.stdout = open('output.txt', 'w')
driver = Chrome()
while i < 2:
    driver.get("https://dell.com/support/home/us/en/04/")

    #root folder for submission directory
    id_box = driver.find_element_by_name('search-input')
    id_box.send_keys('5w2tms1')
    btn = driver.find_element_by_id('btnSearch')
    btn.click()
    time.sleep(4)
    exp_date = driver.find_element_by_id('warrantyExpiringLabel')
    date = exp_date.text
    monthFormat(date)
    i +=1
driver.close()
