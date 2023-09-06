#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
def retrive_data_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title of the web page
        title = soup.title.string if soup.title else ''

        # Use more specific selectors to target <div> and <p> elements
        div_element = soup.select_one('div.td-post-content.tagdiv-type')
        if div_element:
            # Find <p> elements within the specified <div> element
            paragraphs = div_element.find_all('p', class_=lambda x: x != 'tdm-descr')

            # Extract and join the text from selected paragraphs
            text = ' '.join([p.text.strip() for p in paragraphs])
        else:
            text = ''

        return title, text
    except Exception as e:
        print(f"Error retrieving data from {url}: {str(e)}")
        return '', ''
    
   


# In[5]:


import pandas as pd
url = 'https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/'
title,text = pd.Series(retrive_data_url(url))
print(title)
print(text)


# In[ ]:




