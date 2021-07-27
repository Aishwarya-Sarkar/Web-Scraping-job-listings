from selenium import webdriver
import time
import pandas as pd

search_query = 'https://www.indeed.com/q-data-scientist-jobs.html'
driver = webdriver.Chrome(executable_path='C:/Users/Aishwarya/Downloads/chromedriver.exe')

driver.get(search_query)
driver.maximize_window()

time.sleep(5)

job_details = []

driver.get(search_query)
time.sleep(5)
#job_list = driver.find_elements_by_xpath("//div[@class='job_seen_beacon']")
company = driver.find_elements_by_xpath("//a[@data-tn-element ='companyName']")
title = driver.find_elements_by_xpath("//span[@title='Data Scientist']")
#print(job_company.text)
print('Done')
