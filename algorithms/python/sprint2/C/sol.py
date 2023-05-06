def solution(node, idx):
    def get_node_by_index(node, index):
        while index:
            node = node.next_item
            index -= 1
        return node
    if idx == 0:
        head = node.next_item
        return head
    previos_node = get_node_by_index(node, idx-1)
    next_node = get_node_by_index(node, idx+1)
    previos_node.next_item = next_node
    return node
