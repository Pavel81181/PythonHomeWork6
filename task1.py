# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите первый элемент прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))
d = int(input('Введите разность прогрессии: '))
list_1 = []
for i in range (a,n+1):
    list_1.append(a + (i-1)*d)
print(f'Полученная прогрессия: {list_1}')


