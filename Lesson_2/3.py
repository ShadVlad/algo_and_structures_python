"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
def number_reverse(num):
	if num == 0:
		return ''
	else:
		digits = num % 10
		num = num // 10
		return str(digits) + number_reverse(num)


print('              -= Задание 3 =-')
print('Программа формирует из введенного числа обратное по порядку входящих в него цифр\n'
      '                            и выводит на экран.')
number = int(input('Введите натуральное число: '))
a = number
reverse_number = ''
while a != 0:
	digit = a % 10
	a = a // 10
	reverse_number = reverse_number + str(digit)
print(f'{number} <===> {int(reverse_number)}')

print('\n              Рекурсия')
print(f'{number} <===> {int(number_reverse(number))}')
