import csv
from datetime import datetime
import json
import pandas as pd

from search_ads import search
from compile_ads import add_new_ads

search_term = "Manager"
location = "Vancouver, BC"

# Iterate through pages until attempt to access page index returns an error
ads_dict = {}
try:
    i = 0
    while True:
        # Can add: '&sort=date' to get most recent ads
        url = 'https://ca.indeed.com/jobs?q=' + search_term + '&l=' + location + '&radius=100&limit=50&filter=0&start='+str(i)
        ads_dict = search(url)
        print('Searching ', url)
        print(str(len(ads_dict)), ' pages scanned')
        i += 50
    raise Exception('Exited without exception')

except Exception as e: # Compile and process all results
    print('Stopped with exception: \"', e, '\"')

    # Write raw scraped data to file
    filename = 'raw_ads/job ads-' + search_term + '-' + datetime.today().strftime('%m-%d_%H_%M_%S') + '.json'
    with open(filename, 'a', encoding='utf-8') as f:
        json.dump(ads_dict, f, ensure_ascii=False, indent=4)
        
        # Get number of jobs before we add new ones
        df = pd.read_csv("unique_ads.csv")
        prior_size = len(df.index)
        
    add_new_ads(filename)

    # Get size number of jobs after we have added new ones
    df = pd.read_csv("unique_ads.csv")
    new_size = len(df.index)

    print(new_size - prior_size, " new jobs added to unique_ads.csv")

    print('Finished')
