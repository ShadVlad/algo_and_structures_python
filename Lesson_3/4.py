# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint


print('                  -= Задание 4 =-')
print('Программа определяет, какое число в массиве встречается чаще всего.\n')

source_lst = [randint(-100, 101) for i in range(randint(10, 30))]
print(f'Исходный массив\n {source_lst}')
print(len(source_lst))
number = 0
max_count = 0
for num in source_lst:
    count_i = source_lst.count(num)
    
    if max_count < count_i:
        max_count = count_i
        number = num
print(f'Число {number} встречается в этом массиве {max_count} раз(a)')
