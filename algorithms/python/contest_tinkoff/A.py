def color(x, y, z):
    lens = []
    for i in y:
        l = len(i)
        lens.append(l)

    c = 0
    words = []

    for i in range(len(y)):
        sep = z[0][c:c+lens[i]]
        words.append(sep)
        c += lens[i]
    
    c = 0
    yyy = 'YY'
    bbb = 'BB'
    res = []
    for i in words:
        if yyy in i or bbb in i:
            res.append(i)
    return len(res)



def read_input():
    x = int(input())
    y = list(map(str, input().strip().split()))
    z = list(map(str, input().strip().split()))
    return x, y, z


x, y, z = read_input()
print(color(x, y, z))
    
    