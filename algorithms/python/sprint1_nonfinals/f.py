import re


def is_palindrome(line: str) -> bool:
    line_1 = re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', line)
    line_2 = line_1.upper().split(' ')
    line_3 = ''.join(line_2)
    reversed = line_3[::-1]
    if line_3 == reversed:
        return True
    return False


print(is_palindrome(input().strip()))
