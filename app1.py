import json

data = json.load(open("data.json"))

def dictionary(word):
    if word in data:
        return data[word]
    else:
        return 'The word does not esist! Enter a new word!'
    

word = input('Enter a word: ')

print(dictionary(word))



