"""
Задание № 3

Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

from collections import Counter

number = 600851475143
simple_divisor = 2
simple_divisor_list = []

# Находим простые делители числа
for i in range(1, number):
    if number == 1:
        print(max(simple_divisor_list)) # Ответ - 6857
        break

    else:
        if number % simple_divisor == 0:
            number = number / simple_divisor
            simple_divisor_list.append(int(simple_divisor))
        else:
            simple_divisor += 1

