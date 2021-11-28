import csv

import analysis_functions

# Test analysis
with open('processed_ads.csv') as ads_file:
    csvreader = csv.reader(ads_file, skipinitialspace=True)
    i = 0
    all_skills = {} # Keep a dict of skills and their count
    for row in csvreader:
        if i == 0: # Header row
            pass
        if i > 0:
            new_skills = analysis_functions.pos_tagging(row[3])
            for skill in new_skills:
                if skill in all_skills: # If skill exists, increment count
                    all_skills[skill] += 1
                else: # Otherwise add it to skills
                    all_skills[skill] = 1

            print('Processed', i, 'ads')
            #break # Just analyze 1 row for now
        i += 1

with open('skill_counts.csv','w') as skill_file:
    print('Writing skills to file')
    csvwriter = csv.writer(skill_file)
    for skill in all_skills:
        csvwriter.writerow([skill, all_skills[skill]])
