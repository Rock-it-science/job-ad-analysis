from datetime import datetime
import json

from search_ads import search

search_term = "Software Developer"
location = "Vancouver, BC"

# Iterate through pages until attempt to access page index returns an error
ads_dict = {}
try:
    i = 700
    while True:
        url = 'https://ca.indeed.com/jobs?q=' + search_term + '&l=' + location + '&limit=50&start='+str(i)
        ads_dict = search(url)
        print('Searching ', url)
        print(str(len(ads_dict)), ' pages scanned')
        i += 50
    raise Exception('Exited without exception')

except Exception as e:
    
    # Write results to file
    with open('job ads-' + search_term + '-' + datetime.today().strftime('%Y-%m-%d_%H_%M') + '.json', 'a', encoding='utf-8') as f:
        json.dump(ads_dict, f, ensure_ascii=False, indent=4)
    
    print('Stopped with exception: \"', e, '\"')
    print('Finished')