from math import sqrt, cos, tan

def input_check(text):
    while True:
        try:
            value = float(input(text))
            return value
        except ValueError:
            print("Помилка: введіть число!\n")


def division_check(numerator, denominator):
    if abs(denominator) < 1e-10:
        raise ZeroDivisionError(f"Помилка ділення: ділення на нуль ({round(denominator,3)})")
    return numerator / denominator


def sqrt_check(radicand):
    if radicand < 0:
        raise ValueError(f"Помилка обчислення кореня: від'ємний аргумент ({round(radicand,3)})")
    return sqrt(radicand)


def power_check(base, exponent):
    if base == 0 and exponent < 0:
        raise ZeroDivisionError(
            f"Помилка степеня: нуль не можна підносити до від'ємного степеня{round(exponent,3)}"
        )
    if base < 0 and not float(exponent).is_integer():
        raise ValueError(f"Помилка степеня: від'ємне число у дробовому степені {round(exponent,3)}")
    return base**exponent


def tan_check(angle):
    if abs(cos(angle)) < 1e-10:
        raise ValueError(
            "Помилка: тангенс не визначений (косинус кута близький до нуля)"
        )
    return tan(angle)