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


def sqrt_check(radicand):
    if radicand < 0:
        raise ValueError("Помилка: радіканд менше нуля")
    return sqrt(radicand)


def power_check(base, exponent):
    if base == 0 and exponent < 0:
        raise ZeroDivisionError(
            "Помилка: нуль не можна підносити до від'ємного степеня"
        )
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Помилка: від'ємне число у дробовому степені")
    return base**exponent


def tan_check(angle):
    if cos(angle) < 1e-10:
        raise ValueError("tg даного кута не існує")


g = input_check("Вкажіть значення:\ng = ")
h = input_check("Вкажіть значення:\nh = ")
u = input_check("Вкажіть значення:\nu = ")
v = input_check("Вкажіть значення:\nv = ")


def calculate_result_1(g, h):
    base = h / sqrt(7) + division_check(sqrt(5), g + h, "Помилка: g + h = 0")

    exponent = division_check(2 * g, 3 * h + 5, "Помилка: 3*h + 5 = 0")

    minuend = power_check(base, exponent)

    denominator = g**2 - 4 * h + (g - h) ** 2

    numerator = sqrt_check(sqrt(3) + abs(g + h) + g * h)

    subtrahend = division_check(
        numerator, denominator, "Помилка: знаменник другого дробу = 0"
    )

    return minuend - subtrahend


def calculate_result_2(u, v):
    numerator = sin(9 * pi + u) + tan_check(5 * pi + sqrt_check(v))

    radicand = abs(sin(7 * pi + v**2) + cos(3 * pi + u**2))

    denominator = sqrt_check(radicand)

    return division_check(
        numerator, denominator, "Помилка: знаменник другого виразу = 0"
    )


def calculate_result_3(u, v):
    cos_minuend = division_check(
        pi, u**2, "Помилка: знаменник першого дробу косинуса = 0"
    )

    cos_subtrahend = division_check(
        sqrt(3), 2 * v, "Помилка: знаменник другого дробу косинуса = 0"
    )

    minuend = cos(cos_minuend - cos_subtrahend) ** 2

    numerator = cos(sqrt(3) * pi - u**2 + v**2)

    denominator = 2 * sqrt(3) - 3 * v

    subtrahend = sqrt_check(
        division_check(numerator, denominator, "Помилка: знаменник другого дробу = 0")
    )

    return minuend - subtrahend


def calculate_result_4(g, h):
    numerator = cos(sqrt(2) * pi - g) - power_check(g, h)

    denominator = sqrt_check(power_check(h, 2 * g) + 5 * g * h)

    minuend = division_check(
        numerator, denominator, "Помилка: знаменник першого дробу = 0"
    )

    return minuend - power_check(g, h) * tan_check(pi / sqrt(5) + g**2 * h**2) ** 2


def calculate_result_5(g, h, u, v):
    augend_numerator = (
        sin(
            3 * pi
            - sqrt(
                abs(
                    division_check(g * u, 2 * v, "Помилка: знаменник першого дробу = 0")
                )
            )
        )
        ** 2
    )

    augend_denominator = (
        cos(
            5**g - division_check(pi, 2 * u * v, "Помилка: знаменник другого дробу = 0")
        )
        ** 3
    )

    augend = division_check(
        augend_numerator, augend_denominator, "Помилка: знаменник третього дробу = 0"
    )

    addend_numerator = (
        cos(
            sqrt_check(
                division_check(g, h, "Помилка: знаменник четвертого дробу = 0")
                - sqrt(5) * pi / 3
            )
        )
        ** 3
    )

    addend_denominator = sin(
        3 * pi / sqrt(5)
        - sqrt_check(division_check(u, v, "Помилка: знаменник п'ятого дробу = 0"))
    )

    addend = division_check(
        addend_numerator, addend_denominator, "Помилка: знаменник шостого дробу = 0"
    )

    return augend + addend


try:
    result_1 = calculate_result_1(g, h)
    print(f"Result_1 = {result_1}")
    result_2 = calculate_result_2(u, v)
    print(f"Result_2 = {result_2}")
    result_3 = calculate_result_3(u, v)
    print(f"Result_3 = {result_3}")
    result_4 = calculate_result_4(g, h)
    print(f"Result_4 = {result_4}")
    result_5 = calculate_result_5(g, h, u, v)
    print(f"Result_5 = {result_5}")

except ZeroDivisionError as error:
    print(error)

except ValueError as error:
    print(error)

except OverflowError:
    print("Помилка переповнення числа!")

except Exception as error:
    print(f"Невідома помилка: {error}")
