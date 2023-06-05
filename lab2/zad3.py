from collections import defaultdict, Counter
import random


def build_markov_chain(text, order=1, delimiter=' '):
    words = text.split(delimiter)
    markov_chain = defaultdict(Counter)

    for i in range(len(words) - order):
        n_gram = tuple(words[i:i + order])
        next_word = words[i + order]

        markov_chain[n_gram][next_word] += 1

    for n_gram, next_words in markov_chain.items():
        total_count = sum(next_words.values())
        for next_word, count in next_words.items():
            markov_chain[n_gram][next_word] = count / total_count

    return markov_chain


def generate_text(markov_chain, starting_n_gram, text_length=10000, delimiter=' '):
    current_n_gram = tuple(starting_n_gram.split(delimiter))
    generated_text = list(current_n_gram)
    for _ in range(text_length - len(current_n_gram)):
        if current_n_gram not in markov_chain:
            break

        next_word = random.choices(
            population=list(markov_chain[current_n_gram].keys()),
            weights=list(markov_chain[current_n_gram].values())
        )[0]
        generated_text.append(next_word)
        current_n_gram = current_n_gram[1:] + (next_word,)

    return delimiter.join(generated_text)


with open("../lab6/norm_wiki_sample.txt", 'r', encoding="UTF-8") as f:
    text = f.readlines()[0]

markov_chain = build_markov_chain(text)
new_text = generate_text(markov_chain, random.choice(text))

markov_chain_2 = build_markov_chain(text, order=2)
new_text_2 = generate_text(markov_chain_2, random.choice(text) + random.choice(text))

markov_chain_3 = build_markov_chain(text, order=2)
new_text_3 = generate_text(markov_chain_3, 'probability that')
print(new_text)
print(new_text_2)
print(new_text_3)
