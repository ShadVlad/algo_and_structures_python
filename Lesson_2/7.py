"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
def sum(m):                             # Рекурсивная функция
    if m == 1:
        return 1
    else:
        return sum(m - 1) + m


print('              -= Задание 7 =-')
print(' Программа проверяет, что для множества натуральных чисел выполняется равенство:\n'
      ' 1+2+...+n = n(n+1)/2, где n - любое натуральное число')

n = int(input('Введите количество членов ряда (n): '))
summa = sum(n)
formula = n * (n + 1) / 2
print(f'Сумма ряда 1 + 2 + ... + {n} = {summa}')
print(f'По формуле {n} * ({n} + 1) / 2 = {int(formula)}')




