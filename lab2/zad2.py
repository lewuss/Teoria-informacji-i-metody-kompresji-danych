words = []
with open("norm_wiki_sample.txt", 'r', encoding="UTF-8") as f:
    words = f.readlines()[0]

words = words.split()
words = list(map(lambda x: x.lower(), words))
text_length = len(words)


def count_occurances(words):
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))


def get_words_prob(sorted_word_counts):
    words_prob = {}
    for word, occur in sorted_word_counts.items():
        words_prob[word] = occur / text_length
    return words_prob


import random


def generate_text(word_probabilities, text_length=10000):
    words = list(word_probabilities.keys())
    probabilities = list(word_probabilities.values())
    generated_text = []

    while len(generated_text) < text_length:
        chosen_word = random.choices(words, probabilities)[0]
        generated_text.append(chosen_word)

        # If the generated text is too long, truncate it to the exact length.
        if len(generated_text) > text_length:
            generated_text = generated_text[:text_length]

    return ' '.join(generated_text)


base_words_occur = count_occurances(words)
base_words_prob = get_words_prob(base_words_occur)
new_text = generate_text(base_words_prob, 1000)
print(count_occurances(new_text.split()))
