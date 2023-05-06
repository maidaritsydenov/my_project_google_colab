def cost(list1):
    a = list1[0]
    b = list1[1]
    c = list1[2]
    d = list1[3]
        
    if d >= b:
        x = d - b
        answer = x * c + a
    else:
        answer = a
    return answer


def read_input():
    list1 = list(map(int, input().strip().split()))
    return list1


if __name__ == "__main__":
    list1 = read_input()
    print(cost(list1))