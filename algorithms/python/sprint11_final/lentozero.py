# ID 71085161
from typing import List


def lentozero(n: int, numbers: List[int]) -> str:
    count = n
    for i in range(n):
        if numbers[i] == 0:
            count = 0
        numbers[i] = count
        count += 1

    for i in range(n - 1, -1, -1):
        if numbers[i] == 0:
            count = 1
        else:
            numbers[i] = min(numbers[i], count)
            count += 1
    return numbers


def read_input():
    n = int(input())
    numbers = [int(i) for i in input().split()]
    return n, numbers


if __name__ == '__main__':
    n, numbers = read_input()
    print(*lentozero(n, numbers))
