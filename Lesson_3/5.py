# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint


print('                  -= Задание 5 =-')
print('Программа находит максимальный отрицательный элемент массива и выводит на экран его значение и позицию.\n')

source_lst = [randint(-100, 101) for i in range(randint(10, 30))]
print(f'Исходный массив\n {source_lst}')

max_number = -100
position = 0
for num in source_lst:
    if (num < 0) and (max_number < num):
        max_number = num
        position = source_lst.index(num)
        
print(f'Максимальный отрицательный элемент в данном массиве [{position}] = {max_number}')
