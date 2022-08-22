#!/usr/bin/env python
# coding: utf-8

# # Web Scraping

# In[1]:


# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pymongo
import datetime
import requests
import shutil
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd

# Create a path using chromedriver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[2]:


# Visit NASA news website
url = "https://redplanetscience.com/"
browser.visit(url)


# In[3]:


# Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")


# In[4]:


# save the most recent article, title and date
article = soup.find("div", class_="list_text")
news_p = article.find("div", class_="article_teaser_body").text
news_title = article.find("div", class_="content_title").text
news_date = article.find("div", class_="list_date").text
print(news_date)
print(news_title)
print(news_p)


# ## JPL Mars Space Images—Featured Image

# In[5]:


# Visit the Mars space images URL
url2 = "https://spaceimages-mars.com/"
browser.visit(url2)


# In[6]:


# Design an XPTH selector to grab the current featured Mars image
xpath = '/html/body/div[1]/div/a/button'
image = '/html/body/div[8]/div/div/div/div/img'


# In[7]:


# Use splinter to Click the feautured image 
# to bring up the full resolution image
results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


# In[8]:


# Scrape the browser into soup and use soup to find the full resolution image of mars
# Save the image url to a variable called `img_url`
html = browser.html
soup = bs(html, 'html.parser')

img_url = soup.find("img", {"class":"fancybox-image"})['src']
featured_img_url = url2 + img_url
featured_img_url


# In[9]:


# Use the requests library to download and save the image from the `img_url` above
response = requests.get(featured_img_url, stream=True)
with open('mars_featured_img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
    
# Display the image with IPython.display
from IPython.display import Image
Image(url='mars_featured_img.jpg')


# ## Mars Facts

# In[10]:


# Visit the Mars facts URL
url3 = "https://galaxyfacts-mars.com/"
browser.visit(url3)


# In[11]:


# create dataframe for mars information
mars_data = pd.read_html(url3)

mars_df = mars_data[0]
mars_df


# In[12]:


mars_df.columns = ["Mars", "Value","drop"]
mars_df


# In[13]:


mars_df2 = mars_df[['Mars', 'Value']]
mars_df2 = mars_df2.drop([0])
mars_df2


# In[14]:


# Convert table to HTML string
mars_facts = mars_df2.to_html()
print(mars_facts)


# ## Mars Hemispheres

# In[15]:


# Visit the Mars astrogeology site
url4 = "https://marshemispheres.com/"
browser.visit(url4)


# In[16]:


# Design an XPTH selector to grab the links
xpath_cerberus = '//*[@id="product-section"]/div[2]/div[1]/div/a'
xpath_schiaparelli = '//*[@id="product-section"]/div[2]/div[2]/div/a'
xpath_syrtis = '//*[@id="product-section"]/div[2]/div[3]/div/a'
xpath_valles = '//*[@id="product-section"]/div[2]/div[4]/div/a'


# In[17]:


# CERBERUS HEMISPHERE:
cerberus_results = browser.find_by_xpath(xpath_cerberus)
cerberus = cerberus_results[0]
cerberus.click()


# In[18]:


html = browser.html
soup = bs(html, 'html.parser')

cerberus = soup.find("img", {"class":"wide-image"})['src']
cerberus_img_url = url4 + cerberus
cerberus_img_url


# In[19]:


# Go back to homepage
home = '//*[@id="results"]/div[1]/div/div[4]/a'
go_home = browser.find_by_xpath(home)
go_home.click()


# In[20]:


# SCHIAPARELLI HEMISPHERE
schia_results = browser.find_by_xpath(xpath_schiaparelli)
schia = schia_results[0]
schia.click()


# In[21]:


html = browser.html
soup = bs(html, 'html.parser')

schia = soup.find("img", {"class":"wide-image"})['src']
schia_img_url = url4 + schia
schia_img_url


# In[22]:


# Go back to homepage
home = '//*[@id="results"]/div[1]/div/div[4]/a'
go_home = browser.find_by_xpath(home)
go_home.click()


# In[23]:


# SYRTIS HEMISPHERE
syrtis_results = browser.find_by_xpath(xpath_syrtis)
syrtis = syrtis_results[0]
syrtis.click()


# In[24]:


html = browser.html
soup = bs(html, 'html.parser')

syrtis = soup.find("img", {"class":"wide-image"})['src']
syrtis_img_url = url4 + syrtis
syrtis_img_url


# In[25]:


# Go back to homepage
home = '//*[@id="results"]/div[1]/div/div[4]/a'
go_home = browser.find_by_xpath(home)
go_home.click()


# In[26]:


# VALLES HEMISPHERE
valles_results = browser.find_by_xpath(xpath_valles)
valles = valles_results[0]
valles.click()


# In[27]:


html = browser.html
soup = bs(html, 'html.parser')

valles = soup.find("img", {"class":"wide-image"})['src']
valles_img_url = url4 + valles
valles_img_url


# In[28]:


# Close the browser after scraping
browser.quit()


# In[29]:


# Append the dictionary with the image URL string and the hemisphere title to a list
hemisphere_image_urls = [
    {"title":"Valles Marineris Hemisphere", "img_url":valles_img_url},
    {"title":"Cerberus Hemisphere", "img_url":cerberus_img_url},
    {"title":"Schiaparelli Hemisphere", "img_url":schia_img_url},
    {"title":"Syrtis Major Hemisphere", "img_url":syrtis_img_url},
]

print(*hemisphere_image_urls,sep='\n')

