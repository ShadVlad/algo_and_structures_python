# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print('\n                   -= Задание 6 =-')
print('Вывод символа алфавита по его номеру')
a = int(input('Введите номер символа (буквы латинского алфавита): '))

print(f'На {a}-м месте в латинском алфавите буква "{chr(a + 96)}"')
