def sequense(s, t):
    p = -1
    for i in s:
        p = t.find(i, p + 1)
        if p == -1:
            return False
    return True


def read_input():
    s = input()
    t = input()
    return s, t


if __name__ == '__main__':
    s, t = read_input()
    print(sequense(s, t))
