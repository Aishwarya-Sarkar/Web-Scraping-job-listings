#!/usr/bin/env python
# coding: utf-8

# ### Import necessary Packages:

# In[35]:


from selenium import webdriver
import time
import pandas as pd


# ### Setup Web-Driver:

# In[37]:


search_query = 'https://www.indeed.com/q-data-scientist-jobs.html'
driver = webdriver.Chrome(executable_path='C:/Users/Aishwarya/Downloads/chromedriver.exe')

driver.get(search_query)
driver.maximize_window()

time.sleep(5)


# In[40]:


time.sleep(5)

company = driver.find_elements_by_xpath("//a[@data-tn-element ='companyName']")
title = driver.find_elements_by_xpath("//span[@title='Data Scientist']")
#print(job_company.text)
print('Done')


# In[65]:



'''
for each_job in job_list:
    # Getting job info
    job_title = each_job.find_elements_by_xpath(".//h2[@class='title']/a")[0]
    job_company = each_job.find_elements_by_xpath(".//span[@class='company']")[0]
    job_location = each_job.find_elements_by_xpath(".//span[@class='location accessible-contrast-color-location']")[0]
    job_summary = each_job.find_elements_by_xpath(".//div[@class='summary']")[0]
    job_publish_date = each_job.find_elements_by_xpath(".//span[@class='date ']")[0]
    # Saving job info 
    job_info = [job_title.text, job_company.text, job_location.text, job_summary.text, job_publish_date.text]
    # Saving into job_details
    job_details.append(job_info)
driver.quit()'''

job_details = []
job_info = []

#list of all jobs with their elements
job_list = driver.find_elements_by_xpath("//div[@class='job_seen_beacon']")
for job in job_list:
    
    #job Title
    title = job.find_elements_by_xpath(".//div/h2/span")[0]
    
    #Company Name
    company=job.find_elements_by_xpath(".//div[@class='heading6 company_location tapItem-gutter']//span")[0]
    #rating = job.find_elements_by_xpath(".//span[@class='ratingNumber']/span")[0]
    
    #Job Location
    location= job.find_elements_by_xpath(".//div[@class='companyLocation']")[0]
    
    #Job Posting Date
    posting_date = job.find_elements_by_xpath(".//span[@class='date']")[0]
    
    #Job Summary
    summary = job.find_elements_by_xpath(".//div[@class='job-snippet']")[0]
    
    job_info = [title.text, company.text, location.text, summary.text, posting_date.text]
    job_details.append(job_info)
    
''' 
    print(job_title.text)
    print(company.text)
    print(location.text)
    print(posting_date.text)
    print(summary.text)'''


# In[84]:


next_page_button = driver.find_element_by_class_name('pn')

#click on the button for next page
search.click()

time.sleep(5)


# In[85]:


#list of all jobs with their elements
job_list = driver.find_elements_by_xpath("//div[@class='job_seen_beacon']")
for job in job_list:
    
    #job Title
    title = job.find_elements_by_xpath(".//div/h2/span")[0]
    
    #Company Name
    company=job.find_elements_by_xpath(".//div[@class='heading6 company_location tapItem-gutter']//span")[0]
    #rating = job.find_elements_by_xpath(".//span[@class='ratingNumber']/span")[0]
    
    #Job Location
    location= job.find_elements_by_xpath(".//div[@class='companyLocation']")[0]
    
    #Job Posting Date
    posting_date = job.find_elements_by_xpath(".//span[@class='date']")[0]
    
    #Job Summary
    summary = job.find_elements_by_xpath(".//div[@class='job-snippet']")[0]
    
    job_info = [title.text, company.text, location.text, summary.text, posting_date.text]
    job_details.append(job_info)


# In[86]:


job_details_df = pd.DataFrame(job_details, columns= ['Job Title', 'Company', 'Location', 'Summary', 'Posting Date'])
job_details_df

