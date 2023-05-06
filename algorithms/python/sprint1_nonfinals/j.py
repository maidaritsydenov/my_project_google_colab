from typing import List


def factorize(number: int) -> List[int]:

    list = []
    divisor = 2
    while divisor <= (number ** 0.5):
        if number % divisor == 0:
            list.append(divisor)
            number //= divisor
        else:
            divisor += 1
    list.append(number)
    return list


result = factorize(int(input()))
print(" ".join(map(str, result)))
