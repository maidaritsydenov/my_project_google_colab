def binarySearch(arr, x, left, right):
    # промежуток пуст
    if right <= left:
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    # центральный элемент — искомый
    if arr[mid] == x:
        return mid
    # искомый элемент меньше центрального
    # значит следует искать в левой половине
    elif x < arr[mid]:
        return binarySearch(arr, x, left, mid)
    # иначе следует искать в правой половине
    else:
        return binarySearch(arr, x, mid + 1, right)


# изначально мы запускаем двоичный поиск на всей длине массива
index = binarySearch(arr, x, left = 0, right = len(arr))