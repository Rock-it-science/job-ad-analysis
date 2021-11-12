from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()

from scraper import scrape

def search(search_url, ads_dict={}):
    '''
    Define a search url on indeed, and pass the individual job ads to the scraper, then write data to dict
    '''

    resp = http.request('GET', search_url)
    document = resp.data.decode('utf-8')
    soup = BeautifulSoup(document, 'html.parser')

    job_links = []
    # For every result in search
    for job_a in soup.find_all('a', {"class":"result"}):
        # Only care about links that begin with 'rc/clk'
        job_link = job_a.get('href')
        if '/rc/clk' in job_link:
            # Append link
            job_links.append('https://ca.indeed.com/viewjob' + job_link[7:])
    
    # If no jobs found, raise exception (likely got rate-limited)
    if len(job_links) == 0:
        raise Exception('No jobs in page')
    
    # For every item in job_links, pass to scraper and save results in a dict
    ads_dict[search_url] = []
    for link in job_links:
        results = scrape(link)
        ads_dict[search_url].append({
            'url': link,
            'title': results[0],
            'content': results[1]
        })

    return ads_dict