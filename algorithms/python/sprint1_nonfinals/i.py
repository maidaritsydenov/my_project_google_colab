def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True
    list = []
    n = 1
    a = 1
    b = 4
    while n < 10000:
        n = b**a
        a += 1
        list.append(n)
    aw = list
    if number in aw:
        return True
    return False


print(is_power_of_four(int(input())))
