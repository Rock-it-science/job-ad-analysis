# job-ad-analysis

Project for COSC 329 - Learning Analytics to scrape and analyze over 10'000 job ads

## Project Description

Scrape a job website (such as indeed.ca) for job postings with two or more specific job titles and one location. Then parse the text in the postings to analyze required skills. You'll need to think about how skills are defined and use existing NLP libraries to preprocess the texts. Make sure you do something beyond simple keyword or bag of words to recognize skills. Then, do some data analyses to visualize the most sought after skills for these jobs and how the skills are different between the two job titles you searched for.

Scrape 10,000+ job postings, identify 3+ NLP library functions you will use to preprocess the text, explain what each function does and why you chose them, extract skills from the text based on the output of your NLP preprocessing, explain how your extraction algorithm works (i.e., define what you consider to be skills in the text), show the top skills for each job title, compute the overlap between the skills of the two jobs (e.g., using the Bhattacharyya coefficient).

## Schedule

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

## NLP Functions

### Defining Skills

From case study 5 in class, we can use the 3 syntactic patterns for skills:

 1. Noun phrase (e.g., Java, ability to work independently, university degree, written communication)

 2. Verb phrase (e.g., develop web application, design software)

 3. Noun + Gerund (e.g., problem solving, web programming)

### Pre-Processing for Skill Identification

 My process is centered around [Natural Language Toolkit (NLTK) Part-of-speech (POS) Tagging](https://www.nltk.org/api/nltk.tag.html): This method was mentioned in the case study, and we can use it to tag phrases as what part of speech they are (noun, verb, etc.) to help extract the patterns above from the text to identify skills.

 POS tagging makes use of another function called chunking, which ...

 After tagging the POS for each phrase, the text is the tagged POS get passed to another function: lemmatization, which will standardize different forms of the same word to make it easier for us to classify skills in the next step.
