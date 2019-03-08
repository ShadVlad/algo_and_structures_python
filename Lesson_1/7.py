"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

print('\n                        -= Задание 7 =-')
print('Программа по длинам трех отрезков, введенных пользователем, определяет возможность\n'
      '            существования треугольника, составленного из этих отрезков')
a = float(input('Введите длину стороны a: '))
b = float(input('Введите длину стороны b: '))
c = float(input('Введите длину стороны c: '))

if c >= a + b or b >= a + c or a >= b + c:          # в случае равенства точки лежат на одной прямой
    print(f'Треугольник со сторонами {a}, {b}, {c} не существует')
else:
    if a == b or b == c:
        if a == c:
            print(f'Треугольник со сторонами {a}, {b}, {c} существует и является равносторонним')
        else:
            print(f'Треугольник со сторонами {a}, {b}, {c} существует и является равнобедренным')
    else:
        print(f'Треугольник со сторонами {a}, {b}, {c} существует и является разносторонним')







