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


x = input_check("Вкажіть значення:\nx = ")
a = input_check("Вкажіть значення:\na = ")
b = input_check("Вкажіть значення:\nb = ")
c = input_check("Вкажіть значення:\nc = ")


def calculate_f(x, a, b, c):
    if x < 0 and b != 0:
        branch = "Гілка 1 (x < 0, b != 0)"

        result = a * (x**3) + b * (x**2)

        return result, branch

    elif x > 0 and b == 0:
        branch = "Гілка 2 (x > 0, b = 0)"

        numerator = x - a
        denominator = x - c

        return (
            division_check(numerator, denominator, "Ділення на нуль в гілці 2"),
            branch,
        )

    else:
        branch = "Гілка 3 (інакше)"

        numerator = x + 5
        denominator = c * (x - 10)

        return (
            division_check(numerator, denominator, "Ділення на нуль в гілці 3"),
            branch,
        )


try:
    result, branch = calculate_f(x, a, b, c)
    print("\nОбчислено при", branch)
    print("Результат:", result)
except ZeroDivisionError as e:
    print(f"\nПомилка обчислення: {e}")
