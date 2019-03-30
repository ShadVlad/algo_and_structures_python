"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import timeit
import random

def merge_sort(source):
    if len(source) > 1:
        center = len(source) // 2
        left = source[:center]
        right = source[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                source[k] = left[i]
                i += 1
            else:
                source[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            source[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            source[k] = right[j]
            j += 1
            k += 1
        return source



# замеры
source_list = [random.randint(0, 50) for _ in range(25)]

print('Исходный массив')
print(source_list)
print('Отсортированный массив')
print(merge_sort(source_list))

print(timeit.timeit("merge_sort(source_list)", \
    setup="from __main__ import merge_sort, source_list", number=10))


