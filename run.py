from datetime import datetime
from compile import compile_raw
from process import process_data
import json

from search_ads import search

search_term = "Software Developer"
location = "Vancouver, BC"

# Iterate through pages until attempt to access page index returns an error
ads_dict = {}
try:
    i = 1850
    while True:
        url = 'https://ca.indeed.com/jobs?q=' + search_term + '&l=' + location + '&radius=1000&limit=50&filter=0&start='+str(i)
        ads_dict = search(url)
        print('Searching ', url)
        print(str(len(ads_dict)), ' pages scanned')
        i += 50
    raise Exception('Exited without exception')

except Exception as e:
    
    # Write results to file
    with open('raw_data/job ads-' + search_term + '-' + datetime.today().strftime('%Y-%m-%d_%H_%M') + '.json', 'a', encoding='utf-8') as f:
        json.dump(ads_dict, f, ensure_ascii=False, indent=4)
    
    print('Stopped with exception: \"', e, '\"')
    print('Finished gathering data, now updating raw.csv')
    compile_raw()
    print('Updated raw.csv, now updating processed.csv')
    process_data()
    print('Finished')
