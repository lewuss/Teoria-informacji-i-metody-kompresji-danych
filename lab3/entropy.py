import re
from collections import Counter, defaultdict
from math import log2


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    return text


def calc_entropy(tokens, ngram_len):
    ngrams = get_ngrams(tokens, ngram_len)
    ngram_counter = Counter(ngrams)
    ngram_probs = [count / len(ngrams) for count in ngram_counter.values()]
    return calculate_entropy_from_probs(ngram_probs)


def get_ngrams(text, ngram_length):
    return [tuple(text[index:index + ngram_length]) for index in range(len(text) - ngram_length)]


def calculate_entropy_from_probs(probabilities):
    return -sum([p * log2(p) for p in probabilities if p > 0])


def conditional_entropy(entropy):
    return [ent - prev_ent for ent, prev_ent in zip(entropy, [0] + entropy[:-1])]


if __name__ == "__main__":
    file_paths = {
        'english': 'norm_wiki_en.txt',
        'latin': 'norm_wiki_la.txt',
        'esperanto': 'norm_wiki_eo.txt',
        'estonian': 'norm_wiki_et.txt',
        'somali': 'norm_wiki_so.txt',
        'haitian': 'norm_wiki_ht.txt',
        'navajo': 'norm_wiki_nv.txt'
    }
    file_paths = {
        '0': 'sample0.txt',
        '1': 'sample1.txt',
        '2': 'sample2.txt',
        '3': 'sample3.txt',
        '4': 'sample4.txt',
        '5': 'sample5.txt',
    }
    for lang, path in file_paths.items():
        text = read_file(path)
        text = preprocess_text(text)

        for is_word in [False, True]:
            print(f"{lang.capitalize()} {'word' if is_word else 'character'} entropy:")
            entropies =[]
            for n in range(1, 6):
                tokens = text.split() if is_word else text
                entropy = calc_entropy(tokens, n)
                entropies.append(entropy)
            print(entropies)
            print(conditional_entropy(entropies))
