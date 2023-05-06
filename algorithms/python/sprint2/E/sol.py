def solution(node):
    n = node
    m = n.next
    n.next = None
    n.prev = m
    while m is not None:
        m.prev = m.next
        m.next = n
        n = m
        m = m.prev
    node = n
    return node
