# Project Description

Project for COSC 329 - Learning Analytics to scrape and analyze over 10'000 job ads

Scrape a job website (such as indeed.ca) for job postings with two or more specific job titles and one location. Then parse the text in the postings to analyze required skills. You'll need to think about how skills are defined and use existing NLP libraries to preprocess the texts. Make sure you do something beyond simple keyword or bag of words to recognize skills. Then, do some data analyses to visualize the most sought after skills for these jobs and how the skills are different between the two job titles you searched for.

Scrape 10,000+ job postings, identify 3+ NLP library functions you will use to preprocess the text, explain what each function does and why you chose them, extract skills from the text based on the output of your NLP preprocessing, explain how your extraction algorithm works (i.e., define what you consider to be skills in the text), show the top skills for each job title, compute the overlap between the skills of the two jobs (e.g., using the Bhattacharyya coefficient).

# Schedule

Week 8: planning

Week 9: setup

- Set up repository, development environment, and dependencies

- Decide on at least 3 NLP functions

- Initial setup for web scraper

Week 10 (midterm break): gather data

- Decide on job titles and location

- Finalize web scraper

- Gather data (10'000+ postings)

Week 11: Analysis

- Preprocess texts with NLP functions

- Conduct analysis to extract skills

Week 12: Finish analysis, and start video and deliverables

- Create visualizations

- Start writing conclusion, and answering questions in project description

Week 13: presentation video

Week 14: project deliverables.

# Midpoint Status - November 29

## What's here

 - Scraper framework is finished - some fine-tuning may be done
 - Data pipeline for pre-processing raw job ads is functional, but some parts are still being worked on
    - The function to add new ads for example is curently not working, so I rebuild the entire unique_ads CSV file every time a new search is ran
 - Text pre-processing is functional, but needs more testing
 - Analysis pipeline is functional but very slow, and currently the only option is to completely re-process all ads at once
    - Want to make this process more efficient
    - Want to create option to just process new ads
    - Some improvements/tweaks could be made to analysis functions with more testing

## What's not here

 - Need to manually code list of results to remove non-skills
    - I also need to re-write many to be grammatically correct as lemmatization will make many phrases sound weird (problem solve vs. problem solving for example)
 - Need to create visualizations of results
 - Need to write report on results

# NLP Functions

## Defining Skills

From case study 5 in class, we can use the 3 syntactic patterns for skills:

 1. Noun phrase (e.g., Java, ability to work independently, university degree, written communication)

 2. Verb phrase (e.g., develop web application, design software)

 3. Noun + Gerund (e.g., problem solving, web programming)

## Pre-Processing for Skill Identification

 My process is centered around [Natural Language Toolkit (NLTK) **Part-of-speech (POS) Tagging**](https://www.nltk.org/api/nltk.tag.html): This method was mentioned in the case study from class, and we can use it to tag phrases as what part of speech they are (noun, verb, etc.) to help extract the patterns above from the text to identify skills. POST tagging itself is comprised of a few steps. First, segments the text ..., it then tokenizes the text.... Finally the text is tagged as part of speech.

 After the text has been tagged, we use another function called **chunking**, which uses entity and relation detection to identify our skill patterns that we defined above. Chunking takes in the tagged text, and returns chunks of the text that match our patterns.

 After tagging and chunking, we finally pass the matching chunks to be **lemmatized**. This process is similar to stemming, but will standardize different forms of the same word. This will combine many similar results that are linguistically equivalent.

# Instructions

 1. **Scrape ads**: Modify lines 9 and 10 in `scrape-jobs.py` to be the desired search terms, then run with `python scrape_jobs.py`. You can also change line 16 to limit the number of jobs to look at (if left to `while True`, it will run until it either gets to a blank page, or the site rate-limits your IP address). Once the script is complete, it will print out a preview of the results. The full results can be seen in `data/unique_ads.csv`.
 
 2. **Pre-process ads**: The resulting text is very raw, and contains characters we don't want to remove before our analysis. We can now run `python text_preprocessing.py` to process the text. This script will output to `data/processed_ads.csv`.

 3. **Analyze ads**: Its now time to run the NLP functions on our data. This is very time-consuming, but when you're ready you can run `python analyze.py` to analyze all of our job ads. This will output to `data/skill_counts.csv`.

 4. The last step is to look at our results! More processing will come soon, but we can open the file in excel and sort by `Count` descending to see the most common skills! Do note that manual coding will be required to eliminate non-skills from this list.