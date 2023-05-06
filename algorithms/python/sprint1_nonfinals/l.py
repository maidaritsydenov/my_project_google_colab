from typing import Tuple
from string import ascii_lowercase as a


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter += a
    longer += a
    p = list(a)
    result = ''
    for i in range(len(a)):
        if shorter.count(p[i]) != longer.count(p[i]):
            result += p[i]
    return result


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
