"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    sqr_numbers = []
    for nums in args:
        sqr_numbers.append(nums ** 2)

    return sqr_numbers


"""
функция, которая принимает N целых чисел,
 и возвращает список квадратов этих чисел
>>> power_numbers(1, 2, 5, 7)
<<< [1, 4, 25, 49]
"""

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    i = 2
    simple = True
    while i < n:
        if n % i == 0:
            simple = False
        i += 1
    return simple


def filter_numbers(numbers, attribute):
    list_numbers = []
    for num in numbers:
        if attribute == EVEN and num % 2 == 0:
            list_numbers.append(num)
        elif attribute == ODD and num % 2 != 0:
            list_numbers.append(num)
        elif attribute == PRIME:
            if is_prime(num) is True:
                list_numbers.append(num)
    return list_numbers


"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
