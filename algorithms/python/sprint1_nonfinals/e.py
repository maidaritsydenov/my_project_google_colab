def get_longest_word(line: str) -> str:
    list = []
    a = line.strip().split()
    if len(a) == 1:
        list.append(a[0])
        return " ".join(map(str, list))
    a.reverse()
    a.append('a')
    a.reverse()
    a.append('a')
    for i in range(len(a) - 1):
        if len(a[i]) >= len(a[i+1]):
            list.append(a[i])
    return max(list, key=len)


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
