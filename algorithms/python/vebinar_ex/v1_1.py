from typing import List, Tuple


def entry_secuence(arr: List[int], sec: List[int]) -> int:
    st = ''
    so = ''
    for i in range(len(arr)):
        st += str(arr[i])
    res = st
    for i in range(len(sec)):
        so += str(sec[i])
    isc = so
    print(res.count(isc))


def read_input() -> Tuple[List[int], int]:
    arr = list(map(int, input().strip().split()))
    sec = list(map(int, input().strip().split()))
    return arr, sec


arr, sec = read_input()
entry_secuence(arr, sec)
