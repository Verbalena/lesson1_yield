# # Задачи на тему yield:
# #Задача 1: Напишите генератор, который будет возвращать квадраты чисел от 1 до n.
# #Проверьте его на небольшом наборе чисел.
# # 1.1
def squares_of_numbers(n):
    for x in range(1, n+1):
        yield x ** 2

for x in squares_of_numbers(4):
    print(x)
for x in squares_of_numbers(10):
    print(x)
# # 1.2 -----------------


import math


def squares_of_numbers2(n):
    for x in range(1, n+1):
        yield pow(x, 2)

for x in squares_of_numbers2(5):
    print(x)
for x in squares_of_numbers2(8):
    print(x)


# Задача 2: Создайте генератор для получения только четных чисел из заданного списка.
# Продемонстрируйте работу генератора на примере.

numbers = [8, 13, 45, 7, 6, 22, 56, 91]
def even_numbers():
    for x in numbers:
        if x % 2 == 0:
            yield x

for x in even_numbers():
    print(x)


# Задача 3: Напишите генератор для последовательности чисел Фибоначчи, не превышающей n.
# Проверьте генератор для первых нескольких чисел.

def fibonacci(n):
    a, b = 1, 2
    for i in range(1, n+1):
        yield a
        a, b = b, a + b

result_fib = fibonacci(9)
for i in result_fib:
    print(i)

#
# Задача 4: Реализуйте генератор, который будет вычислять и возвращать факториалы чисел от 1 до n.
#  Проверьте его на нескольких значениях n.

def factorial(n):
    for i in range(1, n):
        n = n * i
    yield n
for i in factorial(5):
    print(i)
for i in factorial(6):
    print(i)
for i in factorial(7):
    print(i)