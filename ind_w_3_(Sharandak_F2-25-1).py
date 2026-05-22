from math import sqrt, sin, cos, tan, pi

name = "Олександр"
surname = "Шарандак"
group = "ПЗ-25-1"

author = f"{name} {surname} \t {group} \n"
print(author)


def input_check(text):
    while True:
        try:
            value = float(input(text))
            return value
        except ValueError:
            print("Помилка: введіть число!\n")


def division_check(numerator, denominator, message):
    if abs(denominator) < 1e-10:
        raise ZeroDivisionError(message)
    return numerator / denominator


def sqrt_check(radicand, index):
    if radicand < 0:
        raise ValueError(f"Помилка обчислення кореня: від'ємний аргумент ({radicand})")
    return radicand ** (1 / index)


s = input_check("Вкажіть значення:\ns = ")
f = input_check("Вкажіть значення:\nf = ")
k = input_check("Вкажіть значення:\nk = ")
h = input_check("Вкажіть значення:\nh = ")


def g_calculate(f, k, s, h):
    if s == 0:
        numerator = f - k
        denominator = f + k
        return division_check(numerator, denominator, "Ділення на нуль")
    elif s != 0:
        radicand = (2 * h,)
        return f - sqrt_check(radicand, 3)
    else:
        return error(Exception, "невідоме число s")


try:
    result = g_calculate(f, k, s, h)
    print(f"Result = {result}")

except ZeroDivisionError as error:
    print(error)

except ValueError as error:
    print(error)

except OverflowError:
    print("Помилка переповнення числа!")

except Exception as error:
    print(f"Невідома помилка: {error}")
