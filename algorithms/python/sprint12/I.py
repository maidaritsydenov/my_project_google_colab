class MyQueueSized():
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return None
        else:
            return 'error'

    def pop(self):
        if self.isEmpty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.isEmpty():
            return None
        x = self.queue[self.head]
        return x


result = []
amount = int(input())
max_size = int(input())
q = MyQueueSized(max_size)

for i in range(amount):
    full_command = input()
    command, *args = full_command.split(' ')
    if command == 'push':
        a = q.push(*args)
        if a == 'error':
            result.append(a)
    elif command == 'pop':
        result.append(q.pop())
    elif command == 'peek':
        result.append(q.peek())
    else:
        result.append(q.size)

for i in result:
    print(i)
