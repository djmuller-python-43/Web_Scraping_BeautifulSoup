#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import time
from bs4 import BeautifulSoup

#This is the response variable referencing the get(url) method from requests
#for the website that you are going to scrape.
print('Put some skill that you are not familiar with!')
unfamiliar_skill = input('> ')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    timesjobs_url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=#'
    response = requests.get(timesjobs_url).text # After adding .text to the response produces html output
    #response # printing the response variable return 200 OK status, we have connection!
    soup = BeautifulSoup(response,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        job_posted = job.find('span', class_ = "sim-posted").span.text
        if 'few' in job_posted:
            company_name = job.find('h3', class_ = "joblist-comp-name").text
            skills = job.find('span', class_ = "srp-skills").text.replace(' ', '').split()[-1]
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt", 'w') as file:
                    file.write(f'''Company Name: {company_name.strip()}\n''')
                    file.write(f'''Required Skills: {skills.strip()}\n''')
                    file.write(f'''More Info: {more_info}''')
                    print(f'File saved: {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 60
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait*60)


# In[ ]:




