def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array)/2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array)/2: len(array)])

    # заводим массив для результата сортировки
    result = [] * len(array)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
            k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        # перенеси оставшиеся элементы left в result
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        # перенеси оставшиеся элементы right в result
        result[k] = right[r]
        r += 1
        k += 1
    return result


print(merge_sort([1, 3, 5, 2, 5, 4, 7, 9, 3, 7, 9, 4, 3]))
