LEVEL_TEST_QUESTIONS = [
    # --- A0-A1 (Начальный) - 10 вопросов ---
    {
        'id': 1, 'type': 'multiple_choice', 'difficulty_level': 'A0', 'points': 1,
        'text': 'What is your name?',
        'answers': [
            {'id': 101, 'text': 'My name is John.', 'is_correct': True},
            {'id': 102, 'text': 'I am from London.', 'is_correct': False},
            {'id': 103, 'text': 'I like apples.', 'is_correct': False},
        ]
    },
    {
        'id': 2, 'type': 'multiple_choice', 'difficulty_level': 'A0', 'points': 1,
        'text': 'How old are you?',
        'answers': [
            {'id': 201, 'text': 'I am happy.', 'is_correct': False},
            {'id': 202, 'text': 'I am ten years old.', 'is_correct': True},
            {'id': 203, 'text': 'I live in a house.', 'is_correct': False},
        ]
    },
    {
        'id': 3, 'type': 'text_input', 'difficulty_level': 'A0', 'points': 2,
        'text': 'Translate: "Привет, как дела?"',
        'keywords': ['hello', 'hi', 'how are you', 'how is it going']
    },
    {
        'id': 4, 'type': 'multiple_choice', 'difficulty_level': 'A1', 'points': 1,
        'text': 'Choose the correct form: "She ___ to school every day."',
        'answers': [
            {'id': 401, 'text': 'go', 'is_correct': False},
            {'id': 402, 'text': 'goes', 'is_correct': True},
            {'id': 403, 'text': 'going', 'is_correct': False},
        ]
    },
    {
        'id': 5, 'type': 'multiple_choice', 'difficulty_level': 'A1', 'points': 1,
        'text': 'Which one is a fruit?',
        'answers': [
            {'id': 501, 'text': 'Table', 'is_correct': False},
            {'id': 502, 'text': 'Apple', 'is_correct': True},
            {'id': 503, 'text': 'Car', 'is_correct': False},
        ]
    },
    {
        'id': 6, 'type': 'text_input', 'difficulty_level': 'A1', 'points': 2,
        'text': 'Describe your favorite color in one sentence.',
        'keywords': ['is', 'my favorite color', 'red', 'blue', 'green', 'yellow', 'black', 'white']
    },
    {
        'id': 7, 'type': 'multiple_choice', 'difficulty_level': 'A1', 'points': 1,
        'text': 'The opposite of "hot" is:',
        'answers': [
            {'id': 701, 'text': 'Warm', 'is_correct': False},
            {'id': 702, 'text': 'Cold', 'is_correct': True},
            {'id': 703, 'text': 'Sunny', 'is_correct': False},
        ]
    },
    {
        'id': 8, 'type': 'multiple_choice', 'difficulty_level': 'A1', 'points': 1,
        'text': 'I have two _____.',
        'answers': [
            {'id': 801, 'text': 'cat', 'is_correct': False},
            {'id': 802, 'text': 'cats', 'is_correct': True},
            {'id': 803, 'text': 'cating', 'is_correct': False},
        ]
    },
    {
        'id': 9, 'type': 'text_input', 'difficulty_level': 'A0', 'points': 2,
        'text': 'Write your first name and last name.',
        'keywords': ['my name is']
    },
    {
        'id': 10, 'type': 'multiple_choice', 'difficulty_level': 'A0', 'points': 1,
        'text': 'What is this? (Imagine a picture of a sun)',
        'answers': [
            {'id': 1001, 'text': 'Moon', 'is_correct': False},
            {'id': 1002, 'text': 'Star', 'is_correct': False},
            {'id': 1003, 'text': 'Sun', 'is_correct': True},
        ]
    },

    # --- A2 (Предпороговый) - 10 вопросов ---
    {
        'id': 11, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'Choose the correct preposition: "I am interested ____ learning English."',
        'answers': [
            {'id': 1101, 'text': 'in', 'is_correct': True},
            {'id': 1102, 'text': 'on', 'is_correct': False},
            {'id': 1103, 'text': 'at', 'is_correct': False},
        ]
    },
    {
        'id': 12, 'type': 'text_input', 'difficulty_level': 'A2', 'points': 3,
        'text': 'Form a question: "He lives in New York."',
        'keywords': ['where does he live', 'does he live in new york']
    },
    {
        'id': 13, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'Complete the sentence: "I ____ a good time at the party last night."',
        'answers': [
            {'id': 1301, 'text': 'have', 'is_correct': False},
            {'id': 1302, 'text': 'had', 'is_correct': True},
            {'id': 1303, 'text': 'am having', 'is_correct': False},
        ]
    },
    {
        'id': 14, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'Which word means "very big"?',
        'answers': [
            {'id': 1401, 'text': 'Small', 'is_correct': False},
            {'id': 1402, 'text': 'Huge', 'is_correct': True},
            {'id': 1403, 'text': 'Tiny', 'is_correct': False},
        ]
    },
    {
        'id': 15, 'type': 'text_input', 'difficulty_level': 'A2', 'points': 3,
        'text': 'Describe your daily routine using 2-3 simple sentences.',
        'keywords': ['i wake up', 'i have breakfast', 'i go to work', 'i go to school']
    },
    {
        'id': 16, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'He doesn\'t ____ coffee.',
        'answers': [
            {'id': 1601, 'text': 'drinks', 'is_correct': False},
            {'id': 1602, 'text': 'drink', 'is_correct': True},
            {'id': 1603, 'text': 'drinking', 'is_correct': False},
        ]
    },
    {
        'id': 17, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'What time ____ the train leave?',
        'answers': [
            {'id': 1701, 'text': 'do', 'is_correct': False},
            {'id': 1702, 'text': 'does', 'is_correct': True},
            {'id': 1703, 'text': 'is', 'is_correct': False},
        ]
    },
    {
        'id': 18, 'type': 'text_input', 'difficulty_level': 'A2', 'points': 3,
        'text': 'What did you do yesterday? (One sentence)',
        'keywords': ['i went', 'i saw', 'i played']
    },
    {
        'id': 19, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'My brother is ____ than me.',
        'answers': [
            {'id': 1901, 'text': 'taller', 'is_correct': True},
            {'id': 1902, 'text': 'tall', 'is_correct': False},
            {'id': 1903, 'text': 'tallest', 'is_correct': False},
        ]
    },
    {
        'id': 20, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'We are ____ to the cinema tonight.',
        'answers': [
            {'id': 2001, 'text': 'go', 'is_correct': False},
            {'id': 2002, 'text': 'goes', 'is_correct': False},
            {'id': 2003, 'text': 'going', 'is_correct': True},
        ]
    },

    # --- B1 (Пороговый) - 10 вопросов ---
    {
        'id': 21, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'If I ____ a lot of money, I would buy a big house.',
        'answers': [
            {'id': 2101, 'text': 'had', 'is_correct': True},
            {'id': 2102, 'text': 'have', 'is_correct': False},
            {'id': 2103, 'text': 'will have', 'is_correct': False},
        ]
    },
    {
        'id': 22, 'type': 'text_input', 'difficulty_level': 'B1', 'points': 4,
        'text': 'Explain the difference between "borrow" and "lend".',
        'keywords': ['borrow means to take', 'lend means to give', 'money']
    },
    {
        'id': 23, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'I\'ve been learning English ____ five years.',
        'answers': [
            {'id': 2301, 'text': 'since', 'is_correct': False},
            {'id': 2302, 'text': 'for', 'is_correct': True},
            {'id': 2303, 'text': 'during', 'is_correct': False},
        ]
    },
    {
        'id': 24, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'He suggested ____ to the park.',
        'answers': [
            {'id': 2401, 'text': 'to go', 'is_correct': False},
            {'id': 2402, 'text': 'going', 'is_correct': True},
            {'id': 2403, 'text': 'go', 'is_correct': False},
        ]
    },
    {
        'id': 25, 'type': 'text_input', 'difficulty_level': 'B1', 'points': 4,
        'text': 'Describe your ideal weekend.',
        'keywords': ['relax', 'friends', 'travel', 'hobby']
    },
    {
        'id': 26, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'She looks ____ her mother.',
        'answers': [
            {'id': 2601, 'text': 'like', 'is_correct': True},
            {'id': 2602, 'text': 'as', 'is_correct': False},
            {'id': 2603, 'text': 'for', 'is_correct': False},
        ]
    },
    {
        'id': 27, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'The book ____ by John was a bestseller.',
        'answers': [
            {'id': 2701, 'text': 'wrote', 'is_correct': False},
            {'id': 2702, 'text': 'was written', 'is_correct': True},
            {'id': 2703, 'text': 'writing', 'is_correct': False},
        ]
    },
    {
        'id': 28, 'type': 'text_input', 'difficulty_level': 'B1', 'points': 4,
        'text': 'What are the pros and cons of learning a new language?',
        'keywords': ['pros', 'cons', 'benefits', 'challenges']
    },
    {
        'id': 29, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'I wish I ____ fly.',
        'answers': [
            {'id': 2901, 'text': 'can', 'is_correct': False},
            {'id': 2902, 'text': 'could', 'is_correct': True},
            {'id': 2903, 'text': 'will', 'is_correct': False},
        ]
    },
    {
        'id': 30, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'She avoided ____ him about the problem.',
        'answers': [
            {'id': 3001, 'text': 'to tell', 'is_correct': False},
            {'id': 3002, 'text': 'telling', 'is_correct': True},
            {'id': 3003, 'text': 'tell', 'is_correct': False},
        ]
    },

    # --- B2 (Выше порогового) - 10 вопросов ---
    {
        'id': 31, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'Hardly had I arrived ____ it started raining.',
        'answers': [
            {'id': 3101, 'text': 'when', 'is_correct': True},
            {'id': 3102, 'text': 'than', 'is_correct': False},
            {'id': 3103, 'text': 'then', 'is_correct': False},
        ]
    },
    {
        'id': 32, 'type': 'text_input', 'difficulty_level': 'B2', 'points': 5,
        'text': 'Discuss the importance of renewable energy sources (2-3 sentences).',
        'keywords': ['renewable energy', 'solar', 'wind', 'environment', 'sustainable', 'future']
    },
    {
        'id': 33, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'He managed to ____ the difficult situation.',
        'answers': [
            {'id': 3301, 'text': 'get over', 'is_correct': True},
            {'id': 3302, 'text': 'get off', 'is_correct': False},
            {'id': 3303, 'text': 'get up', 'is_correct': False},
        ]
    },
    {
        'id': 34, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'It\'s high time you ____ studying for your exams.',
        'answers': [
            {'id': 3401, 'text': 'start', 'is_correct': False},
            {'id': 3402, 'text': 'started', 'is_correct': True},
            {'id': 3403, 'text': 'had started', 'is_correct': False},
        ]
    },
    {
        'id': 35, 'type': 'text_input', 'difficulty_level': 'B2', 'points': 5,
        'text': 'What are some common challenges faced by students learning English?',
        'keywords': ['pronunciation', 'grammar', 'vocabulary', 'fluency', 'confidence']
    },
    {
        'id': 36, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'She would rather ____ a quiet evening at home than go out.',
        'answers': [
            {'id': 3601, 'text': 'have', 'is_correct': True},
            {'id': 3602, 'text': 'to have', 'is_correct': False},
            {'id': 3603, 'text': 'having', 'is_correct': False},
        ]
    },
    {
        'id': 37, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'Much as I like him, I cannot agree with his opinion.',
        'answers': [
            {'id': 3701, 'text': 'Even though', 'is_correct': True},
            {'id': 3702, 'text': 'Because', 'is_correct': False},
            {'id': 3703, 'text': 'In order to', 'is_correct': False},
        ]
    },
    {
        'id': 38, 'type': 'text_input', 'difficulty_level': 'B2', 'points': 5,
        'text': 'Discuss the role of technology in modern education.',
        'keywords': ['technology', 'education', 'online learning', 'digital tools', 'access to information']
    },
    {
        'id': 39, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'If only I ____ more time, I would visit you.',
        'answers': [
            {'id': 3901, 'text': 'had', 'is_correct': True},
            {'id': 3902, 'text': 'have', 'is_correct': False},
            {'id': 3903, 'text': 'will have', 'is_correct': False},
        ]
    },
    {
        'id': 40, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'He denied ____ the money.',
        'answers': [
            {'id': 4001, 'text': 'to steal', 'is_correct': False},
            {'id': 4002, 'text': 'stealing', 'is_correct': True},
            {'id': 4003, 'text': 'steal', 'is_correct': False},
        ]
    },

    # --- C1 (Профессиональное владение) - 10 вопросов ---
    {
        'id': 41, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'Complete the idiom: "It\'s raining ____ and dogs."',
        'answers': [
            {'id': 4101, 'text': 'cats', 'is_correct': True},
            {'id': 4102, 'text': 'mice', 'is_correct': False},
            {'id': 4103, 'text': 'birds', 'is_correct': False},
        ]
    },
    {
        'id': 42, 'type': 'text_input', 'difficulty_level': 'C1', 'points': 6,
        'text': 'Write a short paragraph (3-4 sentences) on the societal impact of artificial intelligence.',
        'keywords': ['artificial intelligence', 'impact', 'society', 'automation', 'ethics', 'jobs', 'future']
    },
    {
        'id': 43, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'He finally decided to ____ his dream of becoming a writer.',
        'answers': [
            {'id': 4301, 'text': 'pursue', 'is_correct': True},
            {'id': 4302, 'text': 'chase', 'is_correct': False},
            {'id': 4303, 'text': 'follow', 'is_correct': False},
        ]
    },
    {
        'id': 44, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'The company is facing a ____ of challenges.',
        'answers': [
            {'id': 4401, 'text': 'plethora', 'is_correct': True},
            {'id': 4402, 'text': 'few', 'is_correct': False},
            {'id': 4403, 'text': 'lack', 'is_correct': False},
        ]
    },
    {
        'id': 45, 'type': 'text_input', 'difficulty_level': 'C1', 'points': 6,
        'text': 'Discuss the role of media in shaping public opinion. Provide examples.',
        'keywords': ['media', 'public opinion', 'social media', 'news', 'propaganda', 'influence']
    },
    {
        'id': 46, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'She was so ____ by his behavior that she decided to leave.',
        'answers': [
            {'id': 4601, 'text': 'appalled', 'is_correct': True},
            {'id': 4602, 'text': 'happy', 'is_correct': False},
            {'id': 4603, 'text': 'amused', 'is_correct': False},
        ]
    },
    {
        'id': 47, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': '____ the fact that he was tired, he continued working.',
        'answers': [
            {'id': 4701, 'text': 'Despite', 'is_correct': True},
            {'id': 4702, 'text': 'Although', 'is_correct': False},
            {'id': 4703, 'text': 'Because', 'is_correct': False},
        ]
    },
    {
        'id': 48, 'type': 'text_input', 'difficulty_level': 'C1', 'points': 6,
        'text': 'Analyze the potential benefits and drawbacks of globalization.',
        'keywords': ['globalization', 'benefits', 'drawbacks', 'economy', 'culture', 'interconnectedness']
    },
    {
        'id': 49, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'The project was ____ with numerous obstacles.',
        'answers': [
            {'id': 4901, 'text': 'fraught', 'is_correct': True},
            {'id': 4902, 'text': 'filled', 'is_correct': False},
            {'id': 4903, 'text': 'packed', 'is_correct': False},
        ]
    },
    {
        'id': 50, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'His argument was so ____ that nobody could refute it.',
        'answers': [
            {'id': 5001, 'text': 'cogent', 'is_correct': True},
            {'id': 5002, 'text': 'weak', 'is_correct': False},
            {'id': 5003, 'text': 'vague', 'is_correct': False},
        ]
    },

    # --- C2 (Владение в совершенстве) - 10 вопросов ---
    {
        'id': 51, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'Choose the word that best completes the sentence: "The new policy proved to be ____ to the overall economic growth."',
        'answers': [
            {'id': 5101, 'text': 'conducive', 'is_correct': True},
            {'id': 5102, 'text': 'detrimental', 'is_correct': False},
            {'id': 5103, 'text': 'irrelevant', 'is_correct': False},
        ]
    },
    {
        'id': 52, 'type': 'text_input', 'difficulty_level': 'C2', 'points': 8,
        'text': 'Critically evaluate the implications of quantum computing for cybersecurity.',
        'keywords': ['quantum computing', 'cybersecurity', 'encryption', 'vulnerability', 'threats', 'post-quantum cryptography']
    },
    {
        'id': 53, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'He has a ____ grasp of complex theoretical concepts.',
        'answers': [
            {'id': 5301, 'text': 'profound', 'is_correct': True},
            {'id': 5302, 'text': 'superficial', 'is_correct': False},
            {'id': 5303, 'text': 'shallow', 'is_correct': False},
        ]
    },
    {
        'id': 54, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'The speaker\'s rhetoric was so ____ that it swayed public opinion.',
        'answers': [
            {'id': 5401, 'text': 'persuasive', 'is_correct': True},
            {'id': 5402, 'text': 'dull', 'is_correct': False},
            {'id': 5403, 'text': 'ambiguous', 'is_correct': False},
        ]
    },
    {
        'id': 55, 'type': 'text_input', 'difficulty_level': 'C2', 'points': 8,
        'text': 'Discuss the ethical dilemmas presented by autonomous vehicles.',
        'keywords': ['ethical dilemmas', 'autonomous vehicles', 'trolley problem', 'liability', 'safety', 'moral choices']
    },
    {
        'id': 56, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'The jury remained ____ despite overwhelming evidence.',
        'answers': [
            {'id': 5601, 'text': 'unmoved', 'is_correct': True},
            {'id': 5602, 'text': 'convinced', 'is_correct': False},
            {'id': 5603, 'text': 'swayed', 'is_correct': False},
        ]
    },
    {
        'id': 57, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'To ____ the matter, he then accused her of lying.',
        'answers': [
            {'id': 5701, 'text': 'compound', 'is_correct': True},
            {'id': 5702, 'text': 'simplify', 'is_correct': False},
            {'id': 5703, 'text': 'alleviate', 'is_correct': False},
        ]
    },
    {
        'id': 58, 'type': 'text_input', 'difficulty_level': 'C2', 'points': 8,
        'text': 'Formulate an argument for or against universal basic income.',
        'keywords': ['universal basic income', 'UBI', 'pros', 'cons', 'poverty', 'economy', 'work ethic']
    },
    {
        'id': 59, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'His ____ understanding of the subject allowed him to teach it effectively.',
        'answers': [
            {'id': 5901, 'text': 'comprehensive', 'is_correct': True},
            {'id': 5902, 'text': 'partial', 'is_correct': False},
            {'id': 5903, 'text': 'fragmented', 'is_correct': False},
        ]
    },
    {
        'id': 60, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'The author\'s writing style is notoriously ____, making it difficult to grasp.',
        'answers': [
            {'id': 6001, 'text': 'arcane', 'is_correct': True},
            {'id': 6002, 'text': 'lucid', 'is_correct': False},
            {'id': 6003, 'text': 'accessible', 'is_correct': False},
        ]
    },

    # --- Дополнительные 10 вопросов для достижения 70 (смесь C1/B2/B1/A2) ---
    {
        'id': 61, 'type': 'multiple_choice', 'difficulty_level': 'C1', 'points': 5,
        'text': 'The new regulations are ____ to hinder economic growth.',
        'answers': [
            {'id': 6101, 'text': 'bound', 'is_correct': True},
            {'id': 6102, 'text': 'free', 'is_correct': False},
            {'id': 6103, 'text': 'likely', 'is_correct': False},
        ]
    },
    {
        'id': 62, 'type': 'text_input', 'difficulty_level': 'C1', 'points': 6,
        'text': 'Discuss the concept of "cultural appropriation" and its implications.',
        'keywords': ['cultural appropriation', 'culture', 'respect', 'misappropriation', 'identity']
    },
    {
        'id': 63, 'type': 'multiple_choice', 'difficulty_level': 'B2', 'points': 4,
        'text': 'She was on the ____ of tears.',
        'answers': [
            {'id': 6301, 'text': 'verge', 'is_correct': True},
            {'id': 6302, 'text': 'edge', 'is_correct': False},
            {'id': 6303, 'text': 'brink', 'is_correct': False},
        ]
    },
    {
        'id': 64, 'type': 'text_input', 'difficulty_level': 'B2', 'points': 5,
        'text': 'What are the main characteristics of a good leader?',
        'keywords': ['leadership', 'qualities', 'communication', 'vision', 'empathy']
    },
    {
        'id': 65, 'type': 'multiple_choice', 'difficulty_level': 'C2', 'points': 6,
        'text': 'The novel is a ____ of the author\'s philosophical views.',
        'answers': [
            {'id': 6501, 'text': 'culmination', 'is_correct': True},
            {'id': 6502, 'text': 'beginning', 'is_correct': False},
            {'id': 6503, 'text': 'digression', 'is_correct': False},
        ]
    },
    {
        'id': 66, 'type': 'text_input', 'difficulty_level': 'C2', 'points': 8,
        'text': 'Critically examine the philosophical underpinnings of utilitarianism.',
        'keywords': ['utilitarianism', 'philosophy', 'ethics', 'greatest good', 'consequences']
    },
    {
        'id': 67, 'type': 'multiple_choice', 'difficulty_level': 'B1', 'points': 3,
        'text': 'I look forward to ____ from you.',
        'answers': [
            {'id': 6701, 'text': 'hear', 'is_correct': False},
            {'id': 6702, 'text': 'hearing', 'is_correct': True},
            {'id': 6703, 'text': 'to hear', 'is_correct': False},
        ]
    },
    {
        'id': 68, 'type': 'text_input', 'difficulty_level': 'B1', 'points': 4,
        'text': 'What is your favorite type of music and why?',
        'keywords': ['music', 'genre', 'because', 'relax', 'energy']
    },
    {
        'id': 69, 'type': 'multiple_choice', 'difficulty_level': 'A2', 'points': 2,
        'text': 'He has ____ money than I do.',
        'answers': [
            {'id': 6901, 'text': 'less', 'is_correct': True},
            {'id': 6902, 'text': 'few', 'is_correct': False},
            {'id': 6903, 'text': 'many', 'is_correct': False},
        ]
    },
    {
        'id': 70, 'type': 'text_input', 'difficulty_level': 'A2', 'points': 3,
        'text': 'Where do you usually go on weekends? (One sentence)',
        'keywords': ['i go to the park', 'i stay at home', 'i visit friends']
    },
]