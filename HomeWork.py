# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(n, m):
    if m < 3:
        exp = n * n
    else:
        exp = exponentiation(n, m-1) * n
    return exp

a = int(input('Введите число: '))
b = int(input('Введите его степень: '))
print(exponentiation(a, b))


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(n, m):
    if m < 2:
        res = n + 1
    else:
        res = sum(n, m-1) + 1
    return res

a = int(input('Введите слогаемое: '))
b = int(input('Введите слогаемое: '))
print(sum(a, b))
