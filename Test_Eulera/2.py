"""
Задание № 2

Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""

num_one = 1
num_two = 2
num_sum = 0

for i in range(0, 4000000):
    if num_sum <= 4000000:
        if num_one % 2 == 0:
            num_sum += num_one

        if num_two % 2 == 0:
            num_sum += num_two

        num_one += num_two
        num_two += num_one
    else:
        print(num_sum) # Ответ - 4613732
        break

