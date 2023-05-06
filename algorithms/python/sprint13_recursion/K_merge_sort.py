def merge(arr, lf, mid, rg):
    # базовый случай рекурсии
    if len(arr) == 1:
        return arr
    # запускаем сортировку рекурсивно на левой половине
    lf = merge_sort(arr[0: len(arr)/2])
    # запускаем сортировку рекурсивно на правой половине
    rg = merge_sort(arr[len(arr)/2: len(arr)])


def merge_sort(arr, lf, rg):
    # заводим массив для результата сортировки
    result = [] * len(arr)
    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(lf) and r < len(rg):
        # выбираем, из какого массива забрать минимальный элемент
        if lf[l] <= rg[r]:
            result[k] = lf[l]
            l += 1
        else:
            result[k] = rg[r]
            r += 1
            k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(lf):
        # перенеси оставшиеся элементы lf в result
        result[k] = lf[l]
        l += 1
        k += 1
    while r < len(rg):
        # перенеси оставшиеся элементы rg в result
        result[k] = rg[r]
        r += 1
        k += 1

    return result


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
