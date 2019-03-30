"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import timeit
import random


def bubble_sort(source):
    n = 1
    while n < len(source):
        change = 0
        for i in range(len(source)-n):
            if source[i] > source[i+1]:
                source[i],source[i+1] = source[i+1],source[i]
                change += 1
        if change == 0:
            break
        n += 1
    return source


# замеры
source_list = [random.randint(-100, 100) for _ in range(25)]
print('Исходный массив')
print(source_list)
print('Отсортированный массив')
print(bubble_sort(source_list))

print(timeit.timeit("bubble_sort(source_list)", \
    setup="from __main__ import bubble_sort, source_list", number=10))

