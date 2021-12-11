from nltk import pos_tag, RegexpParser, sent_tokenize, Tree, word_tokenize, WordNetLemmatizer
#from pprint import pprint

def pos_tagging(text):
    """
    List of all tag codes available here: https://www.guru99.com/pos-tagging-chunking-nltk.html
    Docs: https://www.nltk.org/book/ch05.html, https://www.nltk.org/book/ch07.html
    Chunking help from here: https://stackoverflow.com/questions/49564176/python-nltk-more-efficient-way-to-extract-noun-phrases

    From the class reading, we will identify skills as:
    1. noun phrase (e.g., Java, ability to work independently, university degree, written communication)
    2. verb phrase (e.g., develop web application, design software)
    3. noun + gerund (e.g., problem solving, web programming)

    To identify these phrases, we need to tag each word as a part of speech and then use chunking to 
    identify patterns in the text that represent the phrase types.
    """

    # Step 1: Segmentation, Tokenization, and Tagging
    sentences = sent_tokenize(text)
    sentences = [word_tokenize(sentence) for sentence in sentences]
    sentences = [pos_tag(sentence) for sentence in sentences]
    #pprint(sentences)

    # Step 2: Chunking (entity detection -> relation detection)
    # Start with just noun phrases
    noun_phrases = []
    noun_phrase_pattern = "Noun Phrase: {<DT|PP\$>?<JJ>*<NN>}"
    verb_phrase_pattern = "Verb Phrase: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"
    noun_gerund_phrase_pattern = "Noun Gerund: {<NN><VBG>}"

    noun_phrases = chunk(sentences, noun_phrase_pattern)
    verb_phrases = chunk(sentences, verb_phrase_pattern)
    noun_gerund_phrases = chunk(sentences, noun_gerund_phrase_pattern)
    
    skills = []

    #print("Noun Phrases:\n")
    for sentence in noun_phrases:
        #print(sentence)
        for np in sentence:
            #print('\n noun phrase:' + np)
            #print('\n lemmatized: '.join(lemmatization(np)))
            skills.append(' '.join(lemmatization(np)))

    #print("Verb Phrases:\n")
    for sentence in verb_phrases:
        #print(sentence)
        for vp in sentence:
            #print('\n verb phrase:' + vp)
            #print('\n lemmatized: '.join(lemmatization(vp)))
            skills.append(' '.join(lemmatization(vp)))

    #print("Noun Gerund Phrases:\n")
    for sentence in noun_gerund_phrases:
        #print(sentence)
        for ng in sentence:
            #print('\n noun gerund phrase:' + ng)
            #print('\n lemmatized: '.join(lemmatization(ng)))
            skills.append(' '.join(lemmatization(ng)))
        
    return skills

# Chunking
# Credit: https://stackoverflow.com/questions/49564176/python-nltk-more-efficient-way-to-extract-noun-phrases
def chunk(sentences, pattern):
    results = []

    chunker = RegexpParser(pattern)

    for sentence in sentences:
        sentence = chunker.parse(sentence)
        continuous_chunk = []
        current_chunk = []

        for subtree in sentence:
            if type(subtree) == Tree:
                current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                continue
        
        results.append(continuous_chunk)
    
    return results


# Lemmatization
def lemmatization(text):
    lemmatizer = WordNetLemmatizer()

    # Tokenize
    tokenized = word_tokenize(text)

    # Apply pos tagging on each individual word
    tagged = pos_tag(tokenized)

    # Separate words and tags
    words = [token[0] for token in tagged]
    tags = [token[1] for token in tagged]

    # Convert pos tags to simple tags for lemmatization (lem. only knows noun, verb, adjective, adverb, and satellite adjective)
    simple_tags = []
    for tag in tags:
        if tag.startswith('J'):
            simple_tags.append('a')
        elif tag.startswith('V'):
            simple_tags.append('v')
        elif tag.startswith('N'):
            simple_tags.append('n')
        elif tag.startswith('R') or tag.startswith('WR'):
            simple_tags.append('r')
        else:
            simple_tags.append('n') # default to noun

    lemmatized = []
    for i in [0, len(words)-1]:
        lemmatized.append(lemmatizer.lemmatize(words[i], pos=simple_tags[i]))
    
    return lemmatized
