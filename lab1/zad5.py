from collections import defaultdict, Counter
import random


def build_markov_chain(text, order=1):
    markov_chain = defaultdict(Counter)

    for i in range(len(text) - order):
        n_gram = tuple(text[i:i + order])
        next_char = text[i + order]

        markov_chain[n_gram][next_char] += 1

        for n_gram, next_chars in markov_chain.items():
            total_count = sum(next_chars.values())
        for next_char, count in next_chars.items():
            markov_chain[n_gram][next_char] = count / total_count

    return markov_chain


def generate_text(markov_chain, starting_n_gram, text_length=1000):
    current_n_gram = tuple(starting_n_gram)
    generated_text = list(current_n_gram)
    for _ in range(text_length - len(current_n_gram)):
        if current_n_gram not in markov_chain:
            break

        next_char = random.choices(
            population=list(markov_chain[current_n_gram].keys()),
            weights=list(markov_chain[current_n_gram].values())
        )[0]
        generated_text.append(next_char)
        current_n_gram = current_n_gram[1:] + (next_char,)

    return "".join(generated_text)


with open('shakespire.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

text = "".join(lines)

markov_chain = build_markov_chain(text)
new_text = generate_text(markov_chain, 'e')

markov_chain_2 = build_markov_chain(text, order=3)
new_text_2 = generate_text(markov_chain_2, 'the')

markov_chain_3 = build_markov_chain(text, order=5)
new_text_3 = generate_text(markov_chain_3, 'proba')
print(new_text)
print(new_text_2)
print(new_text_3)


def count_avg_length(text):
    text = text.split(" ")
    length = len(text)
    sum_length = 0
    for word in text:
        sum_length += len(word)

    return sum_length / length

print("Średnia długość wyrazu w przybliżeniu markova 1 rzędu to ", count_avg_length(new_text))
print("Średnia długość wyrazu w przybliżeniu markova 3 rzędu to ", count_avg_length(new_text_2))
print("Średnia długość wyrazu w przybliżeniu markova 5 rzędu to ", count_avg_length(new_text_3))
