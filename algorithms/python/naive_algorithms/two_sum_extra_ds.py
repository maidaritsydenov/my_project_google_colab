def twosum_extra_ds(numbers, X):
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    # set() - Множество в python - "контейнер",
    # содержащий не повторяющиеся элементы в случайном порядке
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле,
    # значит, нужной пары элементов в массиве нет.
    return None, None
