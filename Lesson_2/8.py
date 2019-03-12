"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def count_digit(number, digit):
      count = 0
      for char in number:
            if char == digit:
                  count += 1
      return count

print('              -= Задание 8 =-')
print(' Программа считает сколько раз встречается определенная цифра в введенной последовательности чисел.\n')

count_number = int(input('Количество вводимых чисел: '))
digit = int(input('Искомая цифра: '))

quantity_digits = 0

for i in range(1, count_number + 1):
      number = input(f'Введите {i}-е число: ')
      quantity = count_digit(number, str(digit))
      print(f'В числе {number} содержится {quantity} цифр(ы) {digit}')
      quantity_digits += quantity

print(f'В введенных числах содержится {quantity_digits} цифр(ы) {digit}')

