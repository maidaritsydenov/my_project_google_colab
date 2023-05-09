class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Выводит родителя до всех его потомков
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


# Выводит потомков, а затем родителя
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# выводит левого потомка, затем родителя, затем правого потомка
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def test():
    root1 = Node(25, None, None)
    root2 = Node(4, None, None)
    root3 = Node(21, root1, root2)
    root4 = Node(10, None, None)
    root5 = Node(20, root3, root4)
    print(pre_order(root5))


if __name__ == '__main__':
    test()
