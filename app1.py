import json

data = json.load(open("source_file/data.json"))

def dictionary(word):
    if word in data:
        return data[word]
    else:
        return 'The word does not exist! Enter a new word!'
    

word = input('Enter a word: ')

print(dictionary(word))



