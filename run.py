import csv
from datetime import datetime
import json
import pandas as pd

from search_ads import search
from compile import compile_raw
from process import process_data

search_term = "Manager"
location = "Vancouver, BC"

# Iterate through pages until attempt to access page index returns an error
ads_dict = {}
try:
    i = 0
    while True:
        url = 'https://ca.indeed.com/jobs?q=' + search_term + '&l=' + location + '&radius=1000&sort=date&limit=50&filter=0&start='+str(i)
        ads_dict = search(url)
        print('Searching ', url)
        print(str(len(ads_dict)), ' pages scanned')
        i += 50
    raise Exception('Exited without exception')

except Exception as e:
    # Write results raw data to file
    with open('raw_data/job ads-' + search_term + '-' + datetime.today().strftime('%Y-%m-%d_%H_%M') + '.json', 'a', encoding='utf-8') as f:
        json.dump(ads_dict, f, ensure_ascii=False, indent=4)
    
    # Get number of jobs before we add new ones
    df = pd.read_csv("processed.csv")
    prior_size = len(df.index)

    # Compile and process all results
    print('Stopped with exception: \"', e, '\"')
    print('Finished gathering data, now updating raw.csv')
    compile_raw()
    print('Updated raw.csv, now updating processed.csv')
    process_data()

    # Get size number of jobs after we have added new ones
    df = pd.read_csv("processed.csv")
    new_size = len(df.index)

    print(new_size - prior_size, " new jobs added to processed.csv")

    print('Finished')
