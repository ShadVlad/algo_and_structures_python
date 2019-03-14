# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint


print('                    -= Задание 3 =-')
print('Программа меняет местами минимальный и максимальный элементы в массиве случайных целых чисел.\n')


source_lst = [randint(0, 51) for i in range(randint(10, 20))]
print('Исходный массив A\n', source_lst)

max_of_lst = max(source_lst)
min_of_lst = min(source_lst)
index_max = source_lst.index(max_of_lst)
index_min = source_lst.index(min_of_lst)

print(f'Максимальное число - A[{index_max: 3}] = {max_of_lst: 3}')
print(f'Минимальное число -  A[{index_min: 3}] = {min_of_lst: 3}')

source_lst[index_max], source_lst[index_min] = min_of_lst, max_of_lst
index_max, index_min = index_min, index_max

print('Измененный массив A\n', source_lst)

print(f'Максимальное число - A[{index_max: 3}] = {max_of_lst: 3}')
print(f'Минимальное число -  A[{index_min: 3}] = {min_of_lst: 3}')
