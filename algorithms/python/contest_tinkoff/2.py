def read_input():
    x = int(input())
    return x


def cut(x):
    result = x // 2
    if x % 2 == 1:
        result += 1
    return result


if __name__ == '__main__':
    x = read_input()
    print(cut(x))