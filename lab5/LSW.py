import pickle


def compress_lzw(input_file, output_file, dict_size=2 ** 18):
    dictionary = {chr(i): i for i in range(256)}

    with open(input_file, 'rb') as f:
        data = f.read()

    w = chr(data[0])
    result = []
    for c in data[1:]:
        wc = w + chr(c)
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            if len(dictionary) < dict_size:
                dictionary[wc] = len(dictionary)
            w = chr(c)
    if w:
        result.append(dictionary[w])
    with open(output_file, 'wb') as f:
        pickle.dump(result, f)


def decompress_lzw(input_file, output_file):
    dictionary = {i: chr(i) for i in range(256)}

    with open(input_file, 'rb') as f:
        data = pickle.load(f)
    result = []
    w = chr(data.pop(0))
    result.append(w)
    for k in data:
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = w + w[0]

        result.append(entry)
        dictionary[len(dictionary)] = w + entry[0]
        w = entry
    with open(output_file, 'wb') as f:
        f.write(''.join(result).encode('latin1'))


compress_lzw('norm_wiki_sample.txt', 'norm_wiki_sample_coded.txt', dict_size=2 * 12)
compress_lzw('norm_wiki_sample.txt', 'norm_wiki_sample_coded_bigger.txt')
decompress_lzw('norm_wiki_sample_coded.txt', 'norm_wiki_sample_decoded.txt')

compress_lzw('wiki_sample.txt', 'wiki_sample_coded.txt', dict_size=2 * 12)
compress_lzw('wiki_sample.txt', 'wiki_sample_coded_bigger.txt')
decompress_lzw('wiki_sample_coded.txt', 'wiki_sample_decoded.txt')

compress_lzw('lena.bmp', 'lena_coded.bmp', dict_size=2 * 12)
compress_lzw('lena.bmp', 'lena_coded_bigger.bmp')
decompress_lzw('lena_coded.bmp', 'lena_decoded.bmp')

## skompresowane pliki z wielością słownika 2**12 są większe niż pliki bazowe, zaś gdy skorzystamy z wielkości 2**18 znacząco zmniejszamy już rozmiar pliku
