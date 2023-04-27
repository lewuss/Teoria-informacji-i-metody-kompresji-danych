with open('norm_wiki_sample.txt', 'r', encoding='UTF-8') as f:
    text = f.readline()

import math
import json

characters = set(text)
print(f'number of characters {len(characters)}')
print(f'shortest amount of bits needed {math.ceil(math.log2(len(characters)))}')


def create(chars, length):
    codes = {}
    for i, char in enumerate(chars):
        code = bin(i)[2:]
        for j in range(length - len(code)):
            code = '0' + code
        codes[code] = char
    return codes


def encode(text, codes):
    encoded = ''
    for char in text:
        for key, value in codes.items():
            if value == char:
                encoded += key
                break

    return encoded


def decode(encoded, codes):
    length = len(list(codes.keys())[0])
    chunks = [encoded[i:i + length] for i in range(0, len(encoded), length)]
    decoded = ""
    for letter in chunks:
        decoded += codes[letter]
    return decoded


def save(data_dict, string, filename):
    combined_data = data_dict.copy()
    combined_data["string"] = string

    with open(filename, 'w') as json_file:
        json.dump(combined_data, json_file)


def load_from_json_file(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

    string = data.pop("string")
    data_dict = data

    return data_dict, string


codes = create(characters, math.ceil(math.log2(len(characters))))

encoded = encode(text, codes)
decoded = decode(encoded, codes)
print(encoded, decoded)

save(codes, encoded, 'encoded.json')
print(load_from_json_file('encoded.json'))

if text == decoded:
    print('Poprawnie zdekodowano')
