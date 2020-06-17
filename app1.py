import json
import difflib 
from difflib import get_close_matches

data = json.load(open("source_file/data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        yn = input('Did you mean %s instead? Enter Y if yes, or N if no: ' % get_close_matches(word, data.keys())[0])
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return 'The word does not exist! Please check it!'
        else:
            return 'I did not understand the entry!'
    else:
        return 'The word does not exist! Please check it!'
    

word = input('Enter a word: ')

print(dictionary(word))



