from typing import List


# n - кол-во домов
# k - кол-во денег
# prices - стоимость каждого из n домов
def max_quantity(n: int, k: int, prices: List[int]) -> int:
    max_q = 0
    # if


def read_input():
    n1 = list(map(int, input().split()))
    n = n1[0]
    k = n1[1]
    prices = list(map(int, input().split()))
    return n, k, prices


if __name__ == '__main__':
    n, k, prices = read_input()
    print(max_quantity(n, k, prices))
