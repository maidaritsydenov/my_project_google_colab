# 73182086
import random


class Person:
    def __init__(self, name: str, points: int, fines: int) -> str:
        self.name = name
        self.points = points
        self.fines = fines

    def __repr__(self, name):
        return name

    def __gt__(self, other):
        """ "Больше", т.е. ниже в списке.
        Меньше решенных задач, больше штрафов и имя в алфавите ниже.
        """
        if self.points == other.points:
            if self.fines == other.fines:
                return self.name > other.name
            return self.fines > other.fines
        return self.points < other.points

    def __lt__(self, other):
        """ "Меньше", т.е. выше в списке.
        Больше реешнных задач, меньше штрафов и имя в алфавите выше.
        """
        if self.points == other.points:
            if self.fines == other.fines:
                return self.name < other.name
            return self.fines < other.fines
        return self.points > other.points


def quicksort(data, left, right):
    # базовый случай
    if left >= right:
        return data
    i, j = left, right
    # случайный элемент из data
    pivot = data[random.randint(left, right)]
    # сортируем
    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]
            i, j = i + 1, j - 1

    quicksort(data, left, j)
    quicksort(data, i, right)


def read_input():
    n = int(input())
    data = []
    for i in range(n):
        name, points, fines = input().split()
        data.append(Person(name, int(points), int(fines)))
    return n, data


def main(n, data):
    quicksort(data, 0, n - 1)
    for member in data:
        print(member.name)


if __name__ == '__main__':
    n, data = read_input()
    main(n, data)
