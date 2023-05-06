# 71876465

class EmptyDeqExc(Exception):
    pass


class MaxSizeExc(Exception):
    pass


class Deque:
    def __init__(self, m):
        self.__queue = [None] * m
        self.__max_m = m
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == self.__max_m

    def push_back(self, value):
        if self.isFull():
            raise MaxSizeExc
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_m
        self.__size += 1

    def push_front(self, value):
        if self.isFull():
            raise MaxSizeExc
        self.__queue[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_m
        self.__size += 1

    def pop_front(self):
        if self.isEmpty():
            raise EmptyDeqExc
        value = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_m
        self.__size -= 1
        return value

    def pop_back(self):
        if self.isEmpty():
            raise EmptyDeqExc
        value = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_m
        self.__size -= 1
        return value


def deque():
    # n - количество команд
    # m - максимальный размер дека
    n = int(input())
    m = int(input())
    deq = Deque(m)

    for i in range(n):
        try:
            full_command = input()
            command, *args = full_command.split(' ')
            push_command = getattr(deq, command)
            a = push_command(*args)
            if a is not None:
                print(a)
        except EmptyDeqExc:
            print('error')
        except MaxSizeExc:
            print('error')


if __name__ == '__main__':
    deque()
