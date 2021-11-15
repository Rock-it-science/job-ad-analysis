import csv
import json
import os
def compile_raw():
    '''
    Read each raw json file and put into a single csv file
    '''

    for root, dir, files in os.walk('raw_data/'):
        for file in files:
            with open(str(root) + str(file), encoding='utf-8') as json_file:
                try:
                    json_dict = json.load(json_file)
                except Exception as e:
                    json_dict = "Error loading json from file " + file + "\n" + str(e)
            with open('raw.csv', 'a', newline='') as csv_file:
                csvwriter = csv.writer(csv_file)
                # Header
                #csvwriter.writerow(['url', 'title', 'content'])

                if 'Error loading json from file' not in json_dict:
                    for search in json_dict:
                        for result in json_dict[search]:
                            # Encode job description to unicode (because HR people love their emojis 🙄)
                            result['title'] = result['title'].encode('utf-8')
                            result['content'] = result['content'].encode('utf-8')
                            # Write to csv file
                            csvwriter.writerow([result['url'], result['title'], result['content']])
                else:
                    print(json_dict)
        