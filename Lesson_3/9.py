# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint


print('                  -= Задание 8 =-')
print('Поиск максимального элемента среди минимальных элементов столбцов матрицы.\n')

row = int(input('Введите количество строк матрицы: '))
col = int(input('Введите количество столбцов матрицы: '))
array = []
for i in range(row):
    arr_string = []
    summa = 0
    for j in range(col):
        n = randint(0, 50)
        arr_string.append(n)
        print(f'{arr_string[j]: 4}', end='')

    array.append(arr_string)
    print()

print()
# print('Сформированный массив:\n')
min_list = []
for i in range(col):
    min_col = array[0][i]
    for j in range(row):
        if min_col > array[j][i]:
            min_col = array[j][i]
    min_list.append(min_col)

max_min = max(min_list)
print('Минимальные значения по стобцам:')
print(min_list)
print('Максимальное из них: ', max_min)
