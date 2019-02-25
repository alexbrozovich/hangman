import json
import string 

f = open('words_dictionary.json')
j = json.load(f)
words = []
for item in j.keys():
    words.append(item)

length = 7
reqs = []
reqs.append([0, 'a'])
reqs.append([1, 'p'])
matches = []
for word in words:
    score = 0
    for req in reqs:
        if len(word) == length:
            if word[req[0]] == req[1]:
                score += 1
    if score == len(reqs):
        matches.append(word)
letter_counts = dict.fromkeys(string.ascii_lowercase, 0)
for word in matches:
    for letter in word:
        letter_counts[letter] += 1
for req in reqs:
    letter_counts[req[1]] = 0
print(sorted(letter_counts.items(), key=lambda kv: kv[1],reverse=True))