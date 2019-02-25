import json
f = open('words_dictionary.json')
j = json.load(f)
words = []
for item in j.keys():
    words.append(item)
print(len(words))