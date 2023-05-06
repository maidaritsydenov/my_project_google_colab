def scores_sum(k: int, matrix: str) -> int:
    k = k*2
    train_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = {e: matrix.count(e) for e in matrix if (e in train_keys)}
    return sum(numbers[key] <= k for key in numbers)


def read_input():
    k = int(input())
    keys = ''
    for i in range(4):
        keys += input()
    matrix = keys.replace('.', '')
    return k, matrix


if __name__ == '__main__':
    k, matrix = read_input()
    print(scores_sum(k, matrix))