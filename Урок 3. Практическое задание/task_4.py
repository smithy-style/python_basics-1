"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    z = 1
    while y < 0:
        z = x * z
        y = y + 1
    d = 1 / z
    print(d)


x = int(input('Введите число больше 0:'))
y = int(input('Введите отрицательное число:'))
my_func(x, y)
