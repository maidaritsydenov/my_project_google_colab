from itertools import groupby


def solution(f_in, f_out):
    d = []
    for _ in range(f_in):
        n_log = int(input())
        *log, = map(int, input().split())
        a = [0]*log[-1]
        for i, k in zip(log[::2], log[1::2]):
            a[i-1:k] = [1]*(k-i+1)
        d.append(a)

    asd = [sum(col) == f_in for col in zip(*d)]
    result = []
    for s, y in groupby(enumerate(asd, 1), lambda x: x[1]):
        if s:
            *lst, = y
            result.append(lst[0][0])
            result.append(lst[-1][0])
    print(len(result))
    print(*result)


if __name__ == "__main__":
    import sys
    solution(int(input()), sys.stdout)
