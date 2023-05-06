from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    a = ''
    result = []
    for i in range(len(number_list)):
        a += str(number_list[i])

    x = int(a) + k
    while x > 0:
        result.append(x % 10)
        x //= 10

    result.reverse()
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
