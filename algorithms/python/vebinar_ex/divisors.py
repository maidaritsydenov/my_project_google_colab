def divisors_for(n: int) -> set:
    divisors = set()
    if n <= 3:
        return divisors
    for num in range(2, n):
        if n % num == 0:
            divisors.add(num)
    return divisors


# Можно улучшить алгоритм, взяв границу range до корня n

def divisors_sqrt(n: int) -> set:
    divisors = set()
    if n <= 3:
        return divisors
    for num in range(2, int(n**0.5) + 1):
        if n % num == 0:
            divisors.update([num, n // num])
    return divisors


print(divisors_for(123))
print(divisors_sqrt(123))
