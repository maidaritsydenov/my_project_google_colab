# 71876831
from typing import List


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(int(item))

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError('Пустой стек')


def read_input():
    seq = input().split()
    return seq


def calc(seq: List[str]) -> int:
    dictionary = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x,
        '*': lambda x, y: x*y,
        '/': lambda x, y: y//x
    }
    stack = Stack()
    for i in seq:
        try:
            stack.push(int(i))
        except Exception:
            stack.push(dictionary[i](stack.pop(), stack.pop()))
    return stack._items[len(stack._items) - 1]


if __name__ == '__main__':
    seq = read_input()
    print(calc(seq))
