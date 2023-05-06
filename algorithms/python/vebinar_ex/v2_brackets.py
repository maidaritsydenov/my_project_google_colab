TEST1 = '({25}) + [56 * 8a]'
TEST2 = '({24)} + [35 * 2]'
TEST3 = '(24)) [35 + 3]'
TEST4 = '(34} + [2}])'
TEST5 = ')('

dict = {')': '(', '}': '{', ']': '['}


def check_brackets(s: str) -> bool:
    stack = []
    for c in s:
        if c in dict.values():
            stack.append(c)
        elif c in dict:
            if len(stack) > 0:
                b = stack.pop()
                if b != dict[c]:
                    return False
            else:
                return False
    return True


if __name__ == '__main__':
    print(check_brackets(TEST1)) # True
    print(check_brackets(TEST2)) # False
    print(check_brackets(TEST3)) # False
    print(check_brackets(TEST4)) # False
    print(check_brackets(TEST5)) # False
