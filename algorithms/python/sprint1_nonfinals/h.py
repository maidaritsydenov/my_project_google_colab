from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:

    # Выравниваем длины двух чисел
    # str.zfill(str, кол-во нулей) дополняет строку нулями
    if (len(first_number) >= len(second_number)):
        len_first = len(first_number)
        second_number = second_number.zfill(len_first)
    else:
        len_second = len(second_number)
        first_number = first_number.zfill(len_second)

    first_number = list(first_number)
    second_number = list(second_number)

    for i in range(len(first_number)):
        first_number[i] = int(first_number[i])

    for i in range(len(second_number)):
        second_number[i] = int(second_number[i])

    first_number.reverse()
    second_number.reverse()
    sum = []

    last_digit = 0
    for i in range(len(first_number)):
        temp = first_number[i] + second_number[i] + last_digit
        if temp == 0:
            sum.append(0)
        elif temp == 1:
            sum.append(1)
            last_digit = 0
        elif temp == 2:
            sum.append(0)
            last_digit = 1
        else:
            sum.append(1)   # равно 3
            last_digit = 1
    if last_digit == 1:
        sum.append(1)
    sum.reverse()
    for i in range(len(sum)):
        # print(sum[i], end='')
        return int(''.join(map(str, sum)))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
