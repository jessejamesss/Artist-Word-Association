import nltk
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer

import json

# may or may not have to run this again if close folder/project/etc
# nltk.download("stopwords")

# nltk corpus doesn't have stopword files for the commented languages
languages = [
    'arabic', 
    'azerbaijani', 
    'bengali', 
    'catalan', 
    'chinese',
    # 'croatian', 
    'danish', 
    'dutch', 
    'english', 
    'finnish', 
    'french',
    'german', 
    'greek', 
    'hebrew', 
    # 'hindi', 
    'hungarian', 
    'indonesian',
    # 'irish', 
    'italian', 
    # 'japanese', 
    'kazakh', 
    'nepali', 
    'norwegian',
    # 'persian', 
    # 'polish', 
    'portuguese', 
    'romanian', 
    'russian', 
    # 'sinhala',
    'spanish', 
    'swedish', 
    # 'tagalog', 
    # 'tamil', 
    # 'tatar', 
    # 'telugu', 
    # 'thai',
    'turkish', 
    # 'ukrainian', 
    # 'urdu', 
    # 'vietnamese'
]

# adding list of list of stopwords for every non-commented language
t = []
for language in languages:
    t.append(stopwords.words(language))

# combining all lists into one list
swords = [j for i in t for j in i]

# with statement makes sure the file is closed at the end so we don't have to worry about closing it manually
with open("data.json", "r", encoding="utf8") as inFile, open("output.json", "w") as outFile:

    # returns python dict
    data = json.load(inFile)

    # future list of all json objs from data.json
    total_data = []

    for obj in data:
        # getting tweet
        text = obj["text"]

        # tokenizing tweet (splitting it up by whitespace)
        text_tokens = ToktokTokenizer().tokenize(text)

        # filtering tokens to not have stopwords
        tokens_without_sw = [word for word in text_tokens if not word.lower() in swords and len(word) > 1]
        
        # combining list of whitespace separated words back into a sentence and updating "text" field in obj
        obj["text"] = " ".join(tokens_without_sw)
        
        # converting python object into json string
        json_obj = json.dumps(obj, indent=2)
        
        # converting json string into python dictionary
        actual = json.loads(json_obj)
        
        # adding modified python dict to array
        total_data.append(actual)
        
    # writing all modified objects into output file
    json.dump(total_data, outFile, indent=4)