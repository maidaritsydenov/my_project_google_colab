def happy_children(factors, sizes):
    happy_child = 0
    for i in range(len(factors)):
        if sizes and factors[i] <= sizes[-1]:
            sizes.pop()
            happy_child += 1
    return happy_child


def read_input():
    n = int(input())
    factors = sorted(list(map(int, input().split())), reverse=True)
    m = int(input())
    sizes = sorted(list(map(int, input().split())))
    return factors, sizes


if __name__ == '__main__':
    factors, sizes = read_input()
    print(happy_children(factors, sizes))
