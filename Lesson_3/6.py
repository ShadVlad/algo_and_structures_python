"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint

print('                  -= Задание 6 =-')
print('Программа находит сумму элементов, находящихся между минимальным и максимальным элементами.\n')

source_lst = [randint(-50, 50) for i in range(randint(10, 30))]
print(f'Исходный массив\n {source_lst}')

max_index = source_lst.index(max(source_lst)) 
min_index = source_lst.index(min(source_lst))

interval = sorted((max_index, min_index))
lst = source_lst[interval[0] + 1: interval[1]]
print(f'Элементы в искомом интервале {lst}')
summa = sum(lst)
print(f'Искомая сумма: {summa}')
