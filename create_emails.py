from selenium import webdriver
import time
import os

EMAIL_SHORT = os.getenv('EMAIL_SHORT')
EMAIL_ENV = os.getenv('EMAIL')
PASSWORD_ENV = os.getenv('PASSWORD')

url = 'https://protonmail.com/'

options = webdriver.ChromeOptions()

options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                       "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

driver.get(url)

driver.find_element_by_xpath(
    '//*[@id="bs-example-navbar-collapse-1"]/ul/li[9]/a').click()

time.sleep(2)

driver.find_element_by_class_name('panel-heading').click()

time.sleep(4)

driver.find_element_by_id('freePlan').click()

time.sleep(5)

driver.find_element_by_id(
    'username').click()
driver.find_element_by_id(
    'username').send_keys(EMAIL_SHORT)

time.sleep(1.5)

driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD_ENV)

time.sleep(2)

driver.find_element_by_xpath('//*[@id="passwordc"]').send_keys(PASSWORD_ENV)

time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="notificationEmail"]').send_keys(EMAIL_ENV)

time.sleep(2)

driver.find_element_by_class_name('signUpProcess-btn-create').click()

time.sleep(1)

driver.find_element_by_id('confirmModalBtn').click()
