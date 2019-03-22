"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexNumber:
    def __init__(self, c=''):
        self.list = list(c)
        self.mod = c

    def __add__(self, obj):
        self.sum = list(hex(int(self.mod, 16) + int(obj.mod, 16))[2:])

    def __mul__(self, obj):
        self.multy = list(hex(int(self.mod, 16) * int(obj.mod, 16))[2:])


x = input('Введите шестнадцатиричное число А: ')
y = input('Введите шестнадцатиричное число В: ')
a = HexNumber(x)
b = HexNumber(y)
a + b
a * b

print(f'{a.list} + {b.list} = {a.sum}')
print(f'{a.list} * {b.list} = {a.multy}')
