from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()

def scrape(url):
    '''
    Scrape job ad, and return ad title and job description content text
    '''
    
    resp = http.request('GET', url)
    document = resp.data.decode('utf-8')
    soup = BeautifulSoup(document, 'html.parser')
    
    # For now we will assume all ads are coming from indeed
    # Job title should be the only h1 element and description has id jobDescriptionText
    try:
        return [soup.find("h1").get_text(), soup.find(id = "jobDescriptionText").get_text()]
    except: # Sometimes there is an error finding the elements, just return empty strings if this happens
        return ['', '']