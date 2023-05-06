
def find_a_b(n):
    max = 999999999
    res = {}
    {a:b for b in res if b < 9}



def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
 
 
while 1:
    try:
        x = int(input('a = '))
        y = int(input('b = '))
        print('НОК:', lcm(x, y))
    except ValueError:
        break

# def read_input():
#     n = int(input())
#     return n


# n = read_input()
# print(lcm(n))