"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def sum_digit(number):
    sum = 0
    for char in number:
        sum += int(char)
    return sum


print('              -= Задание 9 =-')
print(' Программа вычисляет число с максимальной суммой цифр в введенной последовательности чисел.\n')

count_number = int(input('Количество вводимых чисел: '))
max_sum = 0
max_number = ''

for i in range(1, count_number + 1):
    numbers = input(f'Введите {i}-е число: ')
    sum_digits = sum_digit(numbers)

    if sum_digits > max_sum:
        max_sum = sum_digits
        max_number = numbers

print(f'Максимальную сумму цифр {max_sum} содержит число {max_number}')
