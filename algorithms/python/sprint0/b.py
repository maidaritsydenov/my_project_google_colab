from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    list = []
    for i in range(0, len(a)):
        list.append(a[i])
        list.append(b[i])
    return list

    # while True:
    #     try:
    #         list.append(a.pop(0))
    #         list.append(b.pop(0))
    #     except IndexError:
    #         break
    # return list


# Функция pop() возвращает элемент списка по индексу, а после удаляет

# Функция map(function, iterable, [iterable 2, iterable 3, ...])

# Метод str. strip() вернет копию строки str с удаленными начальными
#   и конечными символами chars.
#   Другими словами, обрежет строку str с обоих концов

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
