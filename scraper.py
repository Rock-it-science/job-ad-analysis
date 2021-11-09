from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()

def scrape(url):
    '''
    Scrape job ad, and return job description text
    '''
    
    resp = http.request('GET', url)
    document = resp.data.decode('utf-8')
    soup = BeautifulSoup(document, 'html.parser')
    
    # For now we will assume all ads are coming from indeed
    # Get ad description element
    return soup.find(id = "jobDescriptionText").get_text()