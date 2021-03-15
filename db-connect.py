from selenium import webdriver
import time
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from numpy import random 
import pyautogui
username = input("username ")
password = input("password ")
inputfile = input("input sheet name with .xlsx ")
driver = webdriver.Chrome()
action = ActionChains(driver) 
driver.maximize_window()
driver.get("https://in.linkedin.com/")
driver.find_element_by_xpath("//input[@id='session_key']").send_keys(username)
driver.find_element_by_xpath("//input[@id='session_password']").send_keys(password)
driver.find_element_by_xpath("//input[@id='session_key']").send_keys(Keys.ENTER)
a = pd.read_excel(inputfile)
def check(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return bool(0)
    return bool(1)
def clickable(xpath):
    try :
        EC.element_to_be_clickable(driver.find_elements_by_xpath(xpath))
    except TimeoutException:
        return bool(0)
    return 1
def intercepted(xpath):
    try :
        driver.find_element_by_xpath(xpath).click() 
    except ElementClickInterceptedException:
        return 0 
    return 1    

for j in a['linkedin profile']:
    driver.get(j)
    temp =driver.find_elements_by_xpath("//span[@class='distance-badge separator']/span[2]")
    time.sleep(np.random.randint(1,2))
    if temp[0].text != "1st":
        if check("//button[normalize-space()='Connect']"):
            driver.find_element_by_xpath("//button[normalize-space()='Connect']").click()
            time.sleep(np.random.randint(1,2))
            driver.find_element_by_xpath("//span[normalize-space()='Add a note']").click()
            time.sleep(1)
            driver.find_element_by_xpath("//textarea[@name='message']").send_keys(open("message.txt","r").read())
            if check("//span[normalize-space()='Send']"):
                if clickable("//span[normalize-space()='Send']"):
                    if intercepted("//span[normalize-space()='Send']") == 0:
                        continue
        else:
            driver.find_element_by_xpath("//div[@class = 'pv-s-profile-actions__overflow ember-view']").click()
            time.sleep(1)
            if check("//span[normalize-space()='Connect']"):
                driver.find_element_by_xpath("//span[normalize-space()='Connect']").click()
                time.sleep(np.random.randint(1,2))
                driver.find_element_by_xpath("//span[normalize-space()='Add a note']").click()
                time.sleep(1)
                driver.find_element_by_xpath("//textarea[@name='message']").send_keys(open("message.txt","r").read())
                if check("//span[normalize-space()='Send']"):
                    if clickable("//span[normalize-space()='Send']"):
                        if intercepted("//span[normalize-space()='Send']") == 0:
                            continue
                
    driver.get("https://techfest.org/sponsors")
    time.sleep(np.random.randint(1,3))
             


    
