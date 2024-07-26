"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20? 232792560
"""


def decision() -> int:
    """
    Функция выполнят перебор чисел от 1 до 300млн и каждое число делит от 1 до 20 и если все операции деления без
    остатка, были выполнены успешно то заносит число в лист, который на выходе показывает минимальное значение
    """
    number = []

    for i in range(1,300000000):
        for x in range(1, 20 + 1):
            if i % x == 0:
                continue
            else:
                break

        else:
            number.append(i)

    return int(min(number)) # Ответ - 232792560, однако программа выполняется довольно долго


if __name__ == "__main__":
    print(decision())