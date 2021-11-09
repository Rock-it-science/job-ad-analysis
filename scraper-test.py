'''
This file is a demo of the http client web scraper libraries 
'''

# For an HTTP client we will use urllib3. This will allow us to request documents from URLs
import urllib3
# To interpret the HTML document we will use Beautiful Soup
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
url = 'http://webcode.me'
resp = http.request('GET', url)
document = resp.data.decode('utf-8')

soup = BeautifulSoup(document, 'html.parser')
print(soup.prettify())