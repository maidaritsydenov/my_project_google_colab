def solution(node, elem):
    idx = 0
    while node:
        if node.value == elem:
            return idx
        else:
            idx += 1
            node = node.next_item
    else:
        return -1
