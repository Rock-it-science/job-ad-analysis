import csv

import analysis_functions

# Test analysis
# Read from processed ads csv file
with open('data/processed_ads.csv') as ads_file:
    csvreader = csv.reader(ads_file, skipinitialspace=True)
    
    # Write to job skills csv file - same as processed, but with skills column
    with open('data/job_skills.csv', 'w') as skill_file:
        csvwriter = csv.writer(skill_file, quoting=1)
        i = 0
        all_skills = {} # Keep a dict of skills per job title - each entry contains count and array of all urls that contain the skill
        for row in csvreader:
            if i == 0: # Header row
                csvwriter.writerow(['URL', 'Title', 'Title Category', 'Skill'])
            elif i > 0:
                # Pass job description to analysis functions
                job_skills = analysis_functions.pos_tagging(row[4])

                # Write all skills to job_skills.csv
                csvwriter.writerow([row[1], row[2], row[3], row[4], job_skills])

                # For every skill in this job
                for skill in job_skills:
                    # Add to all_skills dict
                    skill_job = skill + " - " + row[3] # Combine skill and job title for dict entry
                    if skill_job in all_skills: # If skill exists, increment count
                        all_skills[skill_job] = all_skills[skill_job] + 1
                        # print(skill_job + " now at count " + str(all_skills[skill_job]))
                    else: # Otherwise add it to skills
                        # print("Adding " + skill_job)
                        all_skills[skill_job] = 1

                print('Processed', i, 'ads')
               # if row[0] == '2': break # Stop after a few rows for testing
            i += 1

# Write to skill counts
with open('data/skill_counts.csv','w') as skill_file:
    print('Writing skill counts to file')
    csvwriter = csv.writer(skill_file, quoting=1)
    # Header row
    csvwriter.writerow(['Skill', 'Title Category', 'Count'])
    for skill_titlecat in all_skills:
        skill = skill_titlecat.split(' - ')[0]
        titlecat = skill_titlecat.split(' - ')[1]
        csvwriter.writerow([skill, titlecat, all_skills[skill_titlecat]])

