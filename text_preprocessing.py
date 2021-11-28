import csv
import re

def preprocess(text):

    # TODO Remove Unicode references
    
    # Replace newline with space
    filetext = text.replace('\\n', ' ')

    # Remove non-alphanumeric characters (keep spaces and sentence-delimiting punctuation)
    filetext = re.sub('[^A-Z a-z ]+', '', filetext)
    
    # Remove multiple spaces in a row
    while '  ' in filetext:
        filetext = filetext.replace('  ', ' ')
    
    return filetext

# Preprocess all files from unique_ads.csv and output to processed_ads.csv
with open('unique_ads.csv') as raw_file:
    with open('processed_ads.csv', 'w') as processed_file:
        adreader = csv.reader(raw_file)
        for row in adreader:
            # Also remove the b'' that got hardcoded in an earlier step, as well as other quotes
            processed_title = re.sub('(b\')|(b\")|\'|\"', '', row[2])
            processed_content = re.sub('(b\')|(b\")|\'|\"', '', preprocess(row[3][1:]))
            # Write to file - Add quotes back to title and content, but now consistently
            processed_file.write(str("\n" + row[0] + ', ' + row[1] + ', \"' + processed_title + '\", \"' + processed_content + '\"'))
        print('Finished preprocessing')
            
