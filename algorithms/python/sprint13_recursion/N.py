def read_input():
    n = int(input())
    if n >= 1:
        xys = []
        for i in range(n):
            xys.append(list(map(int, input().split())))
    return n, xys


def asd(n, xys):
    xys.sort()
    newData = []
    start = xys[0][0]
    end = xys[0][1]
    for i in range(n-1):
        if end < xys[i+1][0]:
            newData.append('{} {}'.format(start, end))
            start = xys[i+1][0]
            end = xys[i+1][1]
        elif xys[i+1][1] > end:
            end = xys[i+1][1]
    newData.append('{} {}'.format(start, end))
    return newData


if __name__ == '__main__':
    n, xys = read_input()
    print('\n'.join(asd(n, xys)), end='')
