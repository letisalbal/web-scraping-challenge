# Import Dependencies
!pip install bs4
!pip install splinter
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint

def init_browser():
#Initialize Browser for Windows Users
# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)

# Initialize Browser for Mac User
executable_path = {'executable_path': '/Users/letiix3/Desktop/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


def scrape_nasa_news():
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

    return (news_title, news_p)


def scrape_jpl_image():
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

    return (featured_image_url)



def scrape_mars_weather_twitter():
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

    return (weather_tweet)




def scrape_mars_facts():
# Scrape the table of Mars facts
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
df = tables[0]
df

#Convert HTML table string
df.to_html()

    return (df.to_html)




def scrape_hemispheres():
# URL of page to be scraped
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
hemi_soup = BeautifulSoup(html, 'html.parser')

#Populate links
hemisphere_desc = hemi_soup.find_all('div', class_='description')

link = "https://astrogeology.usgs.gov"
link_collection = []

for desc in hemisphere_desc:
    link_desc = desc.a['href']
    link_collection.append(link + link_desc)
    
print(link_collection)

# Initialize hemisphere_image_urls list
hemisphereurl_collection =[]

# Loop through the hemisphere links to obtain the images
for link in link_collection:

    # Click on the link with the corresponding text
    browser.visit(link)
    
    hemisphereimg_html = browser.html
    hemisphereimg_soup = BeautifulSoup(hemisphereimg_html, 'html.parser')
    hemisphereimg_url = hemisphereimg_soup.find('li').a['href']
    hemisphereimg_title = hemisphereimg_soup.find('h2', class_='title').text.strip()
    hemisphere_dict = {"title": hemisphereimg_title, "url": hemisphereimg_url}
    hemisphereurl_collection.append(hemisphere_dict)

hemisphereurl_collection    

    return (hemisphereurl_collection)