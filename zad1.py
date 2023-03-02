import string
import random

letters = list(string.ascii_lowercase)
letters.append(" ")
print(letters)

random_letters = []

for i in range(1000000):
    random_letters.append(random.choice(letters))

text = "".join(random_letters)
text = text.split(" ")

sum_of_lengths = 0
non_spaces = 0
for word in text:
    if word != "":
        sum_of_lengths += len(word)
        non_spaces += 1

print(sum_of_lengths/non_spaces)