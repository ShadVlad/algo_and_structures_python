"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
from functools import wraps
import cProfile
import time

def sum(m):
    if m == 1:
        return 1
    else:
        return sum(m - 1) + m

# print(timeit.timeit("sum(m)", setup="from __main__ import sum, m", number=10))

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

@memorize
def sum_m(m):
    if m == 1:
        return 1
    else:
         return sum(m - 1) + m
# m = 25


def memorize(func):
    @wraps(func)
    def g(n, memory={1: 1}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

@memorize
def decorated_sum(n):
    return decorated_sum(n - 1) + n

def f(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def main():
    s = f(m)
    print('Сумма = ', s)

m = 25

print('Рекурсия')
print(timeit.timeit("sum(m)", setup="from __main__ import sum, m", number=10))
print('Меморизация')
print(timeit.timeit("sum_m(m)", setup="from __main__ import sum_m, m", number=10))
print('Декорирование')
print(timeit.timeit("decorated_sum(m)", setup="from __main__ import decorated_sum, m", number=10))
print('Циклический')
print(timeit.timeit("f(m)", setup="from __main__ import f, m",  number=10))
print('\n')
cProfile.run('main()')