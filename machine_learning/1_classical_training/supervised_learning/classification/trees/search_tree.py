# функция find_node(root, value):
#   # Если мы пришли в поддерево, а его не существует, значит нужного элемента в дереве поиска нет
#   если root == None, то верни "Значение {value} не найдено"
#   если value < root.value, то верни find_node(root.left, value)
#   если value = root.value, то верни root 
#   если value > root.value, то верни find_node(root.right, value)
#   верни результат