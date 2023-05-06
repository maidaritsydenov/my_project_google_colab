from typing import Tuple
import sys


def get_sum(first_number: str, second_number: str) -> str:
    if first_number == '0' and second_number == '0':
        return 0
    decimal = 0
    decimal2 = 0
    for digit in first_number:
        decimal = decimal*2 + int(digit)
    for digit in second_number:
        decimal2 = decimal2*2 + int(digit)
    n = decimal + decimal2
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return int(b)


def read_input() -> Tuple[str, str]:
    first_number = sys.stdin.readline().rstrip()
    second_number = sys.stdin.readline().rstrip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
