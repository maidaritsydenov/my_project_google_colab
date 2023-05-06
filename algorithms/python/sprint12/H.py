from typing import List


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def is_correct_bracket_seq(seq: List[str]) -> bool:
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    for i in seq:
        if i in brackets.keys():
            stack.push(i)
        elif len(stack.items) != 0 and brackets[stack.peek()] == i:
            stack.pop()
        else:
            stack.push(i)
            break

    if len(stack.items) == 0:
        return True
    else:
        return False


def read_input():
    seq = list(input())
    return seq


if __name__ == '__main__':
    seq = read_input()
    print(is_correct_bracket_seq(seq))
