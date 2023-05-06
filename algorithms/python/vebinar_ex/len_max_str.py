sentence = 'asdasd a dasd asd adasdasda ' \
           'sdaaaaaaaaaaaaaaaaaaaaaaaaasdadmmmmmmmmmmmmmmmmmmmmbbbbbbb' \
           'sdlkppppppppppppppx'


def len_max_for(data: str) -> int:
    max_word = 0
    for word in data.split(' '):
        if len(word) > max_word:
            max_word = len(word)
    return max_word


print(len_max_for(sentence))


def len_max_map(data: str) -> int:
    return max(map(len, data.split(' ')))


def len_max_max(data: str) -> int:
    return len(max(data.split(' '), key=len))


# def len_max_reduce(data: str) -> int:
#     return len(reduce(lambda: a, b: a if (len(a) > len(b)) else b, data.split(' ')))
