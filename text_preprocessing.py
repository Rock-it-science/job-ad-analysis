import csv
import re

def preprocess(text):

    # Replace one or more newlines with a period
    filetext = re.sub(r'\\n', r'. ', text)

    # Make all text lowercase
    filetext = filetext.lower()

    # Remove non-alphanumeric characters (keep spaces and sentence-delimiting punctuation)
    filetext = re.sub('[^a-z!?.;\s]+', ' ', filetext)

    # Unicode codes will leave random x's everywhere since we removed the number, so lets clean those up
    filetext = re.sub('\s((xe|x)\s)+', ' ', filetext)
    
    # Remove multiple spaces in a row
    filetext = re.sub('\s+', ' ', filetext)
    
    # Remove spaces before period
    filetext = re.sub('(\s\.)', '.', filetext)

    # Remove multiple periods or other sentence delimiters in a row
    filetext = re.sub('[.!?;]{2,}', '.', filetext)

    return filetext

# Preprocess all files from unique_ads.csv and output to processed_ads.csv
with open('data/unique_ads.csv') as raw_file:
    with open('data/processed_ads.csv', 'w') as processed_file:
        adreader = csv.reader(raw_file)
        i = 0 # Row index
        for row in adreader:
            if i == 0: # If first row, write header
                processed_file.write(', "url", "title", "title category", "content"')
                i = i+1
                continue
            # Also remove the b'' that got hardcoded in an earlier step, as well as other quotes
            processed_title = re.sub('(b\')|(b\")|\'|\"', '', row[2])
            processed_content = re.sub('(b\')|(b\")|\'|\"', '', preprocess(row[3][1:]))

            # Add job title category - either 'software developer' or 'manager'
            #   Using Indeed's search we get a lot of unrelated jobs, so lets narrow our data down to 
            #   jobs that have terms related to 'manager' or 'software developer' in the job title.
            #   Since software developer is a relatively narrow term, I'll define some other common
            #   related terms that we can choose to group together with software devs or not.

            title_cat = ''
            proc_title_low = processed_title.lower() # Processed title in all lowercase
            manager_words = ['manager','supervisor','director','lead']
            software_dev_words = ['software develop', 'web develop', 'back end develop', 'java develop', 'c develop', 'front end develop', 'stack develop']
            software_eng_words = ['software engineer']
            data_science_words = ['data scien', 'data analyst', 'machine learn']
            data_eng_words = ['data engineer'] # I am currently looking into data engineering roles personally, so I'll include this separately for my own research
            if any(manager_word in proc_title_low for manager_word in manager_words):
                title_cat = 'manager'
            elif any(software_dev_word in proc_title_low for software_dev_word in software_dev_words):
                title_cat = 'software developer'
            elif any(software_eng_word in proc_title_low for software_eng_word in software_eng_words):
                title_cat = 'software engineer'
            elif any(data_science_word in proc_title_low for data_science_word in data_science_words):
                title_cat = 'data scientist/analyst'
            elif any(data_eng_word in proc_title_low for data_eng_word in data_eng_words):
                title_cat = 'data engineer'

            # Write to file - Add quotes back to title and content, but now consistently
            processed_file.write(str('\n' + row[0] + ', \"' + row[1] + '\", \"' + processed_title + '\", \"' + title_cat + '\", \"' + processed_content + '\"'))
        print('Finished preprocessing')
            
