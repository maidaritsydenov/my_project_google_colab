def zero_distance(n):
    zero_index = [i for i in range(len(n)) if n[i] == 0]
    z=0
    if zero_index[0] != 0:
        for i in range(zero_index[z]):
            n[i] = zero_index[0]-i
    if zero_index[-1] != len(n)-1:
        for i in range(zero_index[-1], len(n)):
            n[i] = i-zero_index[-1]
    while z<len(zero_index)-1:
        for i in range(zero_index[z], zero_index[z+1]):
            n[i] = min([abs(i-x) for x in zero_index[z:z+2]])
        z += 1
    return n

print(zero_distance([5, 0, 1, 4, 9, 0]))