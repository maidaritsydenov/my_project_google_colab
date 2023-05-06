from typing import List
from string import ascii_uppercase as asc


def tricky_cipher(
    n: int, fio: List[set], sumbrth: List[int],
    first_letter: List[str]
) -> List:
    col = []
    d = []
    f = []
    res = []
    final = []
    too = ''
    for i in range(n):
        col.append(len(fio[i]))
        d.append((int(sumbrth[i][0])+int(sumbrth[i][1])+int(sumbrth[i][2]))*64)
        f.append((asc.find(first_letter[i]) + 1)*256)
    result = [col[i] + d[i] + f[i] for i in range(len(col))]
    for a in range(n):
        res.append(str(hex(result[a]).upper() + ' '))
    for k in range(n):
        if len(res[k]) - 1 >= 3:
            final.append(res[k][-4::])
        elif len(res[k]) - 1 == 2:
            final.append(f'{res[k]:01}')
        elif len(res[k]) - 1 == 1:
            final.append(f'{res[k]:02}')
        else:
            return 0
    for q in range(n):
        too += final[q]
    print(too)


def read_input():
    n = int(input())
    fio = []
    sumbrth = []
    first_letter = []
    for i in range(n):
        x = (input().replace(',', ''))
        y = set(list(x[:-7:]))
        z = (list(x[-7:-4:]))
        m = x[0][0][0]
        fio.append(y)
        sumbrth.append(z)
        first_letter.append(m)
    return n, fio, sumbrth, first_letter


n, fio, sumbrth, first_letter = read_input()
tricky_cipher(n, fio, sumbrth, first_letter)
