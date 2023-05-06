class Fox:
    def __init__(self):
        self.items = []

    def say(self):
        print('TATATATATA')


fox = Fox()
fox_say = getattr(fox, 'say')
# Теперь в переменной fox_say лежит ссылка на метод экземпляра класса.
print(fox_say)
#  <bound method Fox.say of <__main__.Fox object at 0x7f7498618a90>>
# Чтобы функция запустилась, нужно, как обычно, вызвать её со скобками
fox_say()
# Напечатает "TATATATATA"
