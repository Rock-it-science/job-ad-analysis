from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()

from scraper import scrape

def search(search_url):
    '''
    Define a search url on indeed, and pass the individual job ads to the scraper
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
    
    # For every item in job_links, pass to scraper and write results to files
    dir = 'job_descriptions/'
    for link in job_links:
        # Name of file as unique part of url
        f = open(dir + link[33:49] + '.txt', 'a')
        f.write(scrape(link))
        f.close()

    return 'Done'

print(search("https://ca.indeed.com/jobs?q=Data%20Engineer&l=Canada&vjk=799da35d885ad16b"))