def read_input():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    x = int(input())
    return arr, x


def binarySearch(arr, x, left, right):
    if (right <= left and left != 0):
        return -1
    mid = (left + right) // 2
    if (arr[mid] >= x and (arr[mid - 1] < x or mid == 0)):
        return mid + 1
    elif x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


if __name__ == '__main__':
    arr, x = read_input()
    print(binarySearch(arr, x, left=0, right=len(arr)), end=' ')
    print(binarySearch(arr, x * 2, left=0, right=len(arr)), end=' ')
