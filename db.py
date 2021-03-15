from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from numpy import random  
username = input("username ")
password = input("password ")
number = int(input("no of google pages to search "))
inputfile = input("input sheet name with .xlsx ")
driver = webdriver.Chrome()
action = ActionChains(driver) 
driver.maximize_window()
driver.get("https://in.linkedin.com/")
driver.find_element_by_xpath("//input[@id='session_key']").send_keys(username)
driver.find_element_by_xpath("//input[@id='session_password']").send_keys(password)
driver.find_element_by_xpath("//input[@id='session_key']").send_keys(Keys.ENTER)
a = pd.read_excel(inputfile)
for comp in range(a.shape[1]):
    df = pd.DataFrame()
    temp = 'site:linkedin.com/in/ AND "' + a.iloc[0,comp] + '" AND "India" AND '
    temp2 =""
    linklist = []
    for i in a.iloc[1:(a.shape[0]-1),comp]:
        
        temp2 = temp2 +  '"' + i +'" OR '
    temp2 = temp2 + '"' + a.iloc[-1,comp] + '"'
    search = temp + temp2
    driver.get("https://www.google.com/")
    driver.find_element_by_xpath("//input[@name='q']").send_keys(search)
    driver.find_element_by_xpath("//input[@name='q']").send_keys(Keys.ENTER)
    def check(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return bool(1)
        return bool(0)
    for i in range(number):
        for j in driver.find_elements_by_xpath("//div[@class='yuRUbf']/a"):
            linklist.append(j.get_attribute('href'))
        temp3 = "//a[@aria-label='Page " +str(i+2)+ "']"
        driver.find_element_by_xpath(temp3).click()
    name =[]
    position =[]
    company =[]
    link =[]
    for j in linklist:
        driver.get("http://techfest.org/contact")
        time.sleep(random.randint(3))
        driver.get(j)
        if check("//span[@class='t-16 t-black t-normal']"):
            continue
        k = driver.find_element_by_xpath("//span[@class='t-16 t-black t-normal']").text.split()
        temp = 0
        if k[0] == "500+":
            temp = temp + 1
        else:
            countvalue = 0
            try:
                int(k[0])
            except ValueError:
                countvalue = 1
                
            if countvalue == 0:
                if int(k[0])>=100:
                    temp = temp + 1
        if temp == 1:
            name.append(driver.find_element_by_xpath("//li[@class='inline t-24 t-black t-normal break-words']").text)    
            position.append(driver.find_element_by_xpath("//h2[@class='mt1 t-18 t-black t-normal break-words']").text)
            company.append(driver.find_element_by_xpath("//ul[@class='pv-top-card--experience-list']").text)
            link.append(j)
    df['name'] = name
    df['position'] = position
    df['company name'] = company
    df['linkedin profile'] = link 
    df.to_excel(a.iloc[0,comp] +".xlsx")
