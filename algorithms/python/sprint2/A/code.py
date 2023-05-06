def transpose(a):
    if not a:
        return []
    rows_count = len(a)
    colums_count = len(a[0])
    new_matrix = []
    for j in range(colums_count):
        tmp = []
        for i in range(rows_count):
            tmp.append(a[i][j])
        new_matrix.append(tmp)
    return new_matrix


if __name__ == '__main__':
    rows = int(input().strip())
    colums = int(input().strip())
    if rows != 0 and colums != 0:
        a = [[0] * colums for _ in range(rows)]
        for i in range(rows):
            a[i] = [int(j) for j in input().strip().split(" ")]
    elif rows == 0 and colums != 0:
        a = [[0 for _ in range(colums)]]
    elif rows != 0 and colums == 0:
        a = [[0] for _ in range(rows)]
    else:
        a = []
    for row in transpose(a):
        print(*row)
