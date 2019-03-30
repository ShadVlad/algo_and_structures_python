"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random
import timeit


def arr_mediana(source):
    for i in range(len(source)):
        count_min = 0
        count_max = 0
        for j in range(len(source)):
            if source[j] != source[i]:
                if source[j] > source[i]:
                    count_min += 1
                else:
                    count_max += 1
        if  count_min == count_max:
            print(f'{i}-й элемент {source[i]} медиана')
            break


k = 11
source_list = [random.randint(-100, 100) for _ in range(2 * k + 1)]
print('Исходный массив')
print(source_list)
arr_mediana(source_list)
print('Проверка:')                  # для наглядности вывел отсортированный массив
print(sorted(source_list))

# print(timeit.timeit("arr_mediana(source_list)", \
#     setup="from __main__ import arr_mediana, source_list", number=10))

