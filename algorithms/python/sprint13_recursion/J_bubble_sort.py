def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr


def bubble_sort(n, arr):
    check = 1
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                check = 1
        if check == 1:
            for i in arr:
                print(i, end=' ')
            print('')
            check = 0


if __name__ == '__main__':
    n, arr = read_input()
    bubble_sort(n, arr)
