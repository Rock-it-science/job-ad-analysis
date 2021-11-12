import json

from search_ads import search

# Iterate through pages until attempt to access page index returns an error
ads_dict = {}
try:
    i = 10
    while True:
        url = 'https://ca.indeed.com/jobs?q=software developer&l=Vancouver, BC&start='+str(i)
        ads_dict = search(url)
        print('Searching ', url)
        print(str(len(ads_dict)), ' pages scanned')
        i += 10
    raise Exception('Exited without exception')

except Exception as e:
    
    # Write results to file
    with open('job_ads.json', 'a') as f:
        json.dump(ads_dict, f, ensure_ascii=False, indent=4)
    
    print('Stopped with exception: \"', e, '\"')
    print('Finished, scanned ', i, ' results')