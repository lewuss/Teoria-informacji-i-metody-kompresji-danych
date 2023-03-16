words = []
with open("norm_wiki_sample.txt", 'r', encoding="UTF-8") as f:
    words = f.readlines()[0]

# Step 1: Split the string into words
words = words.split()
words = list(map(lambda x: x.lower(), words))

# Step 2: Create an empty dictionary
word_counts = {}

# Step 3: Loop through each word and update the count in the dictionary
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))



text_length = len(words)
import itertools

sliced_dict = itertools.islice(sorted_word_counts.items(), 6000)
sum_6000 = 0
for key, value in sliced_dict:
    sum_6000 += value

sliced_dict = itertools.islice(sorted_word_counts.items(), 30000)
sum_30000 = 0
for key, value in sliced_dict:
    sum_30000 += value

print("6000 most common words account for the ", sum_6000*100/text_length, "% of words used")
print("30000 most common words account for the ", sum_30000*100/text_length, "% of words used")


