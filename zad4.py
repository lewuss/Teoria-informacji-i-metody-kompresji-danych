import string
import random

with open('shakespire.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

text = "".join(lines)
letters = list(string.ascii_letters)
letters.append(" ")
old_text = []

for i, letter in enumerate(text):
    if letter in letters:
        old_text.append(letter.lower())

new_text = "".join(old_text)

occurances = {}

for letter in new_text:
    if letter in occurances:
        occurances[letter] += 1
    else:
        occurances[letter] = 0

occurances = dict(sorted(occurances.items(), key=lambda item: item[1], reverse=True))

probability = {}

for letter, occ in occurances.items():
    probability[letter] = occ / len(new_text)

print(probability)

random_string = ''.join(random.choices(list(probability.keys()), weights=list(probability.values()), k=10000))
sum_of_lengths = 0
non_spaces = 0
random_string = random_string.split(" ")
print(random_string)
for word in random_string:
    if word != "":
        sum_of_lengths += len(word)
        non_spaces += 1

print(sum_of_lengths / non_spaces)

most_prob = [" ", 'e']
bio_occur = {}

for i, letter in enumerate(new_text):
    if letter in most_prob and i < len(new_text):
        bio = letter + new_text[i+1]
        if bio in bio_occur:
            bio_occur[bio] += 1
        else:
            bio_occur[bio] = 0

bio_occur = dict(sorted(bio_occur.items(), key=lambda item: item[1], reverse=True))

print(bio_occur)

