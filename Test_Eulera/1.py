"""
Задание № 1

Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def search_short_number(num_1: int, num_2: int, num_max: int) -> int:
    num_sum = 0

    for i in range(1, num_max):
        if (i % num_1 == 0.0) or (i % num_2 == 0.0):
            num_sum += i

    # Правильный ответ - 233168
    return num_sum

if __name__ == "__main__":
    print(search_short_number(3, 5, 1000))