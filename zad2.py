import string

with open('shakespire.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

text = "".join(lines)
letters = list(string.ascii_letters)
new_text = []

for i, letter in enumerate(text):
    if letter in letters:
        new_text.append(letter.lower())

new_text = "".join(new_text)

occurances = {}

for letter in new_text:
    if letter in occurances:
        occurances[letter] += 1
    else:
        occurances[letter] = 0

occurances = dict(sorted(occurances.items(), key=lambda item: item[1], reverse=True))

probability = {}

for letter, occ in occurances.items():
    probability[letter]=occ/len(new_text)

print(probability)


