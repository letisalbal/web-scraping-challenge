#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Dependencies
get_ipython().system('pip install bs4')
get_ipython().system('pip install splinter')
from splinter import Browser
from bs4 import BeautifulSoup

import pandas as pd
import requests
from selenium import webdriver


# In[2]:


#Initialize Browser for Windows Users
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Initialize Browser for Mac User
executable_path = {'executable_path': '/Users/letiix3/Desktop/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


#NASA MARS NEWS

#Visit the NASA news url
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

#html 
html = browser.html

#BeautifulSoup Object
soup = BeautifulSoup(html, 'html.parser')

#Extract title and paragraph from NASA site
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text

#Print title and paragraph
print(news_title)
print(news_p)


# In[5]:


#JOL MARS SPACE IMAGES

#Visit the JPL url
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(featured_image_url)

#html
html_jpl_image = browser.html

#BeautifulSoup Object
soup = BeautifulSoup(html_jpl_image, 'html.parser')

#Obtain image
featured_image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

#Url
jpl_url ='https://www.jpl.nasa.gov'

#Link url with scrape route
featured_image_url = jpl_url + featured_image_url

#Print featured image
featured_image_url


# In[6]:


#MARS WEATHER

#Visit Mars Weather Twitter
mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)

#html
html_mars_weather = browser.html

#BeautifulSoup Object
soup = BeautifulSoup(html_mars_weather, 'html.parser')

#Find Tweets
current_tweets = soup.find_all('div', class_='js-tweet-text-container')

#Retrieve the elements that have the news title
#Display wthe latest Mars weather tweet
for tweet in current_tweets: 
    weather_tweet = tweet.find('p').text
    if 'Sol' and 'pressure' in weather_tweet:
        print(weather_tweet)
        break
    else: 
        pass


# In[7]:


#MARS FACTS

# Visit Mars facts url 
facts_url = 'http://space-facts.com/mars/'

# Use Panda's `read_html` to parse the url
mars_facts = pd.read_html(facts_url)

# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
mars_df = mars_facts[0]

# Assign the columns `['Description', 'Value']`
mars_df.columns = ['Description','Value']

# Set the index to the `Description` column without row indexing
mars_df.set_index('Description', inplace=True)

# Save html code to folder Assets
mars_df.to_html()

data = mars_df.to_dict(orient='records')  # Here's our added param..

# Display mars_df
mars_df


# In[8]:


#MARS HEMISPHERES

#Visit url
mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(mars_hemispheres_url)


# In[9]:


#html
html_mars_hemispheres = browser.html

#BeautifulSoup
soup = BeautifulSoup(html_mars_hemispheres, 'html.parser')

#Get all the information within mars hemispheres
info = soup.find_all('div', class_='info')

#Create empty lists for hemisphere urls
hemisphere_image_urls=[]

#Store the main url
hemispheres_main_url = 'https://astrogeology.usgs.gov'

#For Loop for the information previously stored
for i in info:
    #Title
    title = i.find('h3').text
    
    #Store link that leads to the image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    #Visit link with full image website
    browser.visit(hemispheres_main_url + partial_img_url)
    
    #HTML Object
    partial_img_html = browser.html
    
    #BeauifulSoup for every individual hemisphere information on the website
    soup = BeautifulSoup( partial_img_html, 'html.parser')
    
    #Obtain Full Image Source
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
    #Obtain information into a list of dictionaries
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
    
#Print image urls
hemisphere_image_urls


