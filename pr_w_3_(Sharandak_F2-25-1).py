import datetime
from math import *


def division_check(numerator, denominator, message):
    if abs(denominator) < 1e-10:
        raise ZeroDivisionError(message)
    return numerator / denominator


def sqrt_check(radicand):
    if radicand < 0:
        raise ValueError(f"Помилка обчислення кореня: від'ємний аргумент ({radicand})")
    return sqrt(radicand)


def input_check(text):
    while True:
        try:
            value = float(input(text))
            return value
        except ValueError:
            print("Помилка: введіть число!\n")


current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

user_year = int(input("Введіть рік народження: "))
user_month = int(input("Введіть місяць народження: "))
user_day = int(input("Введіть день народження: "))

user_age = current_year - user_year

while user_age > 120 or user_day > 31 or user_month > 12:
    print("Введені некоректні дані. Спробуйте ще раз.\n")
    user_year = int(input("Введіть рік народження: "))
    user_month = int(input("Введіть місяць народження: "))
    user_day = int(input("Введіть день народження: "))
    user_age = current_year - user_year



print(f"{user_day:02d}.{user_month:02d}.{user_year}")

if (current_month, current_day) < (user_month, user_day):
    user_age -= 1

print(f"Повних років: {user_age}")

k = input_check("Вкажіть значення:\nk = ")
n = input_check("Вкажіть значення:\nn = ")


def F(k, n):
    if k > 0:
        numerator = sqrt_check(n**2 + 2 * n + 3)
        denominator = 7 * n**4 + 3 * k
        print("k>0")
    else:
        numerator = (5**n - 2**k) ** 3
        denominator = 8 * k**2 + 3 ** (k + 1)
        print("k<=0")
    return division_check(numerator, denominator, "Ділення на нуль")


try:
    result = F(k, n)
    print(f"Result = {result}")

except ZeroDivisionError as error:
    print(error)

except ValueError as error:
    print(error)

except OverflowError:
    print("Помилка переповнення числа!")

except Exception as error:
    print(f"Невідома помилка: {error}")
