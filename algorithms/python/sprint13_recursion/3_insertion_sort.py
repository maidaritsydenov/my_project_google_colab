def read_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr


def bubble_sort(n, arr):
    for i in range(n):
        item_to_insert = arr[i]
        j = i
        while j > 0 and item_to_insert < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
        print(*arr)


if __name__ == '__main__':
    n, arr = read_input()
    bubble_sort(n, arr)
