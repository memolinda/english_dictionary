import json
import difflib 
from difflib import get_close_matches

data = json.load(open("source_file/data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        return 'Did you mean %s instead?' % get_close_matches(word, data.keys())[0]
    else:
        return 'The word does not exist! Enter a new word!'
    

word = input('Enter a word: ')

print(dictionary(word))



