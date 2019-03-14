"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

print('                  -= Задание 8 =-')
print('Программа обработки двумерного массива.\n')

row = 5
col = 4
array = []
for i in range(row):
    arr_string = []
    summa = 0
    for j in range(col):
        n = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
        summa += n
        arr_string.append(n)
    arr_string.append(summa)
    array.append(arr_string)

print('Сформированный массив:\n')
for i in range(row):
    for j in range(row):
        print(f'{array[i][j]: 5}', end='')
    print()
