class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        else:
            return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return None
        else:
            return max(self.items)


stack = StackMax()
amount = int(input())
result = []
for i in range(amount):
    full_command = input()
    command, *args = full_command.split(' ')
    if command == 'push':
        stack.push(*args)
    if command == 'pop':
        if stack.pop() == 'error':
            result.append('error')
    if command == 'get_max':
        result.append(stack.get_max())
for i in result:
    print(i)
