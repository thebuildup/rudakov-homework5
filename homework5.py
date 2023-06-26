# Roman Rudakov
# Homework-5
# 21-06-2023
# Grodno-IT-Academy-Python 3.10
# import re
import phonenumbers
import math


# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  #  "0-4, 7-8, 10"
# get_ranges([4,7,10])  # "4, 7, 10"
# get_ranges([2, 3, 8, 9])  # "2-3, 8-9"
def get_ranges(input_list):
    result = ""
    start = input_list[0]
    end = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] == end + 1:
            end = input_list[i]
        else:
            if start == end:
                result += str(start) + ", "
            else:
                result += str(start) + "-" + str(end) + ", "
            start = end = input_list[i]

    if start == end:
        result += str(start)
    else:
        result += str(start) + "-" + str(end)

    return result


# Напсать функцию standardise_phones которая принимает любое
# количество нестандартизированных телефонных номеров и возвращает
# список стандартизированных номеров в том порядке в котором они были
# введены. А если число не является номером - возвращает пустой список
# standardise_phones("298884455") # ["+375298884455"]
# standardise_phones("(29)888-44-55","8029 8885555","+375299998877","375299998867") # ["+375298884455","+375298885555","+375299998877","+375299998867"]
# standardise_phones("298884asd45") # []


def standardise_phones(*args):
    result = []
    for phone in args:
        try:
            parsed_number = phonenumbers.parse(str(phone), "BY")
            if phonenumbers.is_valid_number(parsed_number):
                formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                result.append(formatted_number)
        except phonenumbers.phonenumberutil.NumberParseException:
            pass
    return result


# Создайте функцию rope_product, которая берёт позитивный цельный номер,
# который представляет собой длину верёвки. Длина этой
# верёвки может быть разделена на любое количество более
# малых цельных чисел. Верните максимальный продукт умножения
# малых цельных чисел. Решение не должно пользоваться циклами!

# rope_product(1) -> 1
# rope_product(4) -> 4
# rope_product(5) -> 6
# rope_product(6) -> 9
# rope_product(7) -> 12
# rope_product(11) -> 54

def rope_product(n):
    if n <= 2:
        return n
    max_product = 0
    for i in range(1, n):
        max_product = max(max_product, i * (n - i), i * rope_product(n - i))
    return max_product


# Создайте декоратор handle_multiples который позволит функции rope_product
# вернуть лиш один ответ если задано одно число и много ответов списком если
# введённых значений будет несколько! И добавьте его к функции rope_product
# не меняя решения из предыдущего решения!
# rope_product(8) -> 18
# rope_product(7,11,23,45,32) -> [12, 54, 4374, 14348907, 118098]
# для решения скопируйте функцию из предыдущей задачи сюда, добавьте к ней декоратор
# здесь можно пользоваться циклами

def handle_multiples(func):
    def wrapper(*args):
        if len(args) == 1:
            return func(*args)
        else:
            return [func(n) for n in args]

    return wrapper


@handle_multiples
def rope_product(n):
    if n <= 2:
        return n
    max_product = 0
    for i in range(1, n):
        max_product = max(max_product, i * (n - i), i * rope_product(n - i))
    return max_product
