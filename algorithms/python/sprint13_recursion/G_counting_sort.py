def read_input():
    n = int(input())
    arr = input().split()
    return n, arr


def wardrobe(n, arr):
    pink = []
    yellow = []
    crimson = []
    for i in range(n):
        if arr[i] == '0':
            pink.append(arr[i])
        elif arr[i] == '1':
            yellow.append(arr[i])
        else:
            crimson.append(arr[i])
    print(*(pink + yellow + crimson))


if __name__ == '__main__':
    n, arr = read_input()
    wardrobe(n, arr)
