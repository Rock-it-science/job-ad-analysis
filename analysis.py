from nltk import pos_tag, RegexpParser, sent_tokenize, Tree, word_tokenize

def pos_tagging(text):
    """
    List of all tag codes available here: https://www.guru99.com/pos-tagging-chunking-nltk.html
    Docs: https://www.nltk.org/book/ch05.html
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

    # Step 2: Chunking (entity detection -> relation detection)
    # Start with just noun phrases
    noun_phrases = []
    noun_phrase_pattern = "Noun Phrase: {(<V\w+>|<NN\w?>)+.*<NN\w?>}"
    verb_phrase_pattern = "Verb Phrase: {<VB.*><DT>?<JJ>*<NN><RB.?>?}" # Source: https://www.codecademy.com/courses/natural-language-processing/lessons/nlp-regex-parsing-intro/exercises/chunking-verb-phrases
    noun_gerund_phrase_pattern = "Noun Gerund: {<NN><VBG>}"

    noun_phrases = chunk(sentences, noun_phrase_pattern)
    verb_phrases = chunk(sentences, verb_phrase_pattern)
    noun_gerund_phrases = chunk(sentences, noun_gerund_phrase_pattern)
    
    print("Noun Phrases:")
    for np in noun_phrases:
        print(np)

    print("\n\nVerb Phrases:")
    for vp in verb_phrases:
        print(vp)

    print("\n\nNoun Gerund Phrases:")
    for ng in noun_gerund_phrases:
        print(ng)

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

pos_tagging("Every year, we welcome thousands of university students from every corner of the world to join Microsoft. You bring your aspirations, talent, potential and excitement for the journey ahead. At Microsoft, Interns work on real-world projects in collaboration with teams across the world, while having fun along the way. You willll be empowered to build community, explore your passions and achieve your goals. This is your chance to bring your solutions and ideas to life while working on cutting-edge technology. The internship is designed not only for you to do great work with the opportunity to learn and grow, but to experience our culture full of diverse community connection, executive engagement, and memorable events. Were a company of learn-it-alls rather than know-it-alls and our culture is centered around embracing a growth mindset, a theme of inspiring excellence, and encouraging teams and leaders to bring their best each day. Does this sound like you? Learn more about our cultural attributes. Are you ready to join us and create the future? Come as you are, do what you love. Start your journey with us today! Responsibilities. Software engineers (SWEs) work with teammates to solve problems and build innovative software solutions. You are passionate about customers and product quality, and you provide technical guidance to Program Managers as they consider user needs and product requirements. You will also be expected to demonstrate an ability to learn and adopt relevant new technologies, tools, methods, and processes to leverage in your solutions. As a SWE, you are dedicated to design, development, and testing of next-generation software which will empower every person and organization on the planet to achieve more. Applies engineering principles to solve complex problems through sound and creative engineering. Quickly learns new engineering methods and incorporates them into his or her work processes. Seeks feedback and applies internal or industry best practices to improve his or her technical solutions. Demonstrates skill in time management and completing software projects in a cooperative team environment. Qualifications. Pursuing a bachelor's or master's degree in engineering, computer science or related field. Must have at least one additional quarter/semester of school remaining following the completion of the internship. One year of programming experience in an object-oriented language. Ability to demonstrate an understanding of computer science fundamentals, including data structures and algorithms. Visit our Careers FAQ Page to learn more about the interview process and answers to commonly asked questions. Microsoft is an equal opportunity employer. All qualified applicants will receive consideration for employment without regard to age, ancestry, color, family or medical care leave, gender identity or expression, genetic information, marital status, medical condition, national origin, physical or mental disability, political affiliation, protected veteran status, race, religion, sex (including pregnancy), sexual orientation, or any other characteristic protected by applicable laws, regulations and ordinances. We also consider qualified applicants regardless of criminal histories, consistent with legal requirements. If you need assistance and/or a reasonable accommodation due to a disability during the application or the recruiting process, please send a request via the Accommodation request form. Benefits/perks listed below may vary depending on the nature of your employment with Microsoft and the country where you work.")