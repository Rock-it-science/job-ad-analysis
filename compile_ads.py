import csv
import json
import os
import pandas as pd


def add_new_ads(filename):
    '''
    Add new ads from json file f
    Process ads into unique_ads.csv
    Remove rows with empty content and remove dupliates
    '''

    # Set the csv file for writing to (using append more here)
    with open('data/unique_ads.csv', 'a', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        with open(filename, encoding='utf-8') as f:
            try:
                # Try loading from json file
                json_dict = json.load(f)
            except Exception as e:
                json_dict = "Error loading json from file" + "\n" + str(e)

        if 'Error loading json from file' not in json_dict:
            # Iterate through JSON (we're just interesting the ads themselves)
            for search in json_dict:
                for result in json_dict[search]:
                    # Encode job description to unicode (because HR people love their emojis 🙄)
                    result['title'] = result['title'].encode('utf-8')
                    result['content'] = result['content'].encode('utf-8')
                    # Write to csv file
                    csvwriter.writerow([],[result['url'], result['title'], result['content']])

            # Read unique ads into pandas dataframe for cleaning
            df = pd.read_csv('data/unique_ads.csv')

            # Drop index read from csv column
            #df.drop(['Unnamed: 0'], axis=1, inplace=True)

            # Drop duplicates
            df = df.drop_duplicates()

            # Remove where content is empty string
            # Since b'' is hardcoded into the string for some reason, b'' is the actual string value for empty string
            df.drop(df[df['content'] == "b''"].index, inplace=True)
            
            # Reset index
            df.reset_index(drop=True,inplace=True)

            print(df)

            # Write to processed.csv
            df.to_csv('data/unique_ads.csv')

            return


def build_unique_ads():
    '''
    Looks at all json files in raw_ads, and builds/rebuild the unique_ads file
    '''

    # Set the csv file for writing to (use write mode here to clear the existing content)
    with open('data/unique_ads.csv', 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file)
        # Write header to file since we are starting from blank file
        csvwriter.writerow(['url', 'title', 'content'])

        # Iterate through all ads in raw_ads directory
        for root, dir, name in os.walk('data/raw_ads/'):
            for file in name:
                # Open JSON file
                with open(os.path.join(root, file), encoding='utf-8') as json_file:
                    try:
                        # Try loading json file
                        json_dict = json.load(json_file)
                    except Exception as e:
                        print("Error loading json from file " + file + "\n" + str(e))

                if 'Error loading json from file' not in json_dict:
                    # Iterate through JSON (we're just interesting the ads themselves)
                    for search in json_dict:
                        for result in json_dict[search]:
                            # Encode job description to unicode (because HR people love their emojis 🙄)
                            result['title'] = result['title'].encode('utf-8')
                            result['content'] = result['content'].encode('utf-8')
                            # Write to csv file
                            csvwriter.writerow([result['url'], result['title'], result['content']])
    
    # Read unique ads into pandas dataframe for cleaning
    df = pd.read_csv('data/unique_ads.csv')

    # Drop duplicates
    df = df.drop_duplicates()

    # Remove where content is empty string
    # Since b'' is hardcoded into the string for some reason, b'' is the actual string value for empty string
    df.drop(df[df['content'] == "b''"].index, inplace=True)

    # Reset index
    df.reset_index(drop=True,inplace=True)

    print(df)

    # Write to processed.csv
    df.to_csv('data/unique_ads.csv')

    return


# Testing

#build_unique_ads()
#add_new_ads('data/raw_ads/job ads-Software Developer-11-24_14_26_53.json')