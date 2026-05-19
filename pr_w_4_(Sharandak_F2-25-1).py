import math

from datetime import date


name = input("Введіть ім'я особи: ")
day, month, year = map(
    int,
    input("Введіть день, місяць і рік народження через пробіл: ").split(),
)

birth_date = date(year, month, day)
today = date.today()
age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Ім'я особи: {name}")
print(f"Дата народження: {day:02d}.{month:02d}.{year}")
if age >= 18:
    print("Особа є повнолітньою.")
else:
    print("Особа не є повнолітньою.")


def F(x, a, b, c):
    def power_check(base, exponent):
        if base == 0 and exponent < 0:
            raise ZeroDivisionError("Нуль не можна підносити до від'ємного степеня")
        if base < 0 and not float(exponent).is_integer():
            raise ValueError("Від’ємне число у дробовому степені")
        return base**exponent

    if x < 0 and a != 0:
        denominator = 2 * x - 5
        if denominator == 0:
            raise ZeroDivisionError("Ділення на нуль у 1-й гілці")
        value = (a * x**2 + b * x + c) / denominator
        return value, "x < 0, a != 0"

    elif 0 <= x < 1:
        base = a * power_check(x, c) - 4**b
        exponent = 3 * a + c
        value = power_check(base, exponent)
        return value, "0 <= x < 1"

    elif x >= 1 and b == 0:
        radicand = x**3 + 3 ** (a + 1)
        if radicand < 0:
            raise ValueError("Від’ємне підкореневе у 3-й гілці")
        value = (4 * x + a * c) / math.sqrt(radicand)
        return value, "x >= 1, b = 0"

    elif x > 1 and a == 0 and b < 0 and c != 0:
        denominator = 2 * c**3
        if denominator == 0:
            raise ZeroDivisionError("Ділення на нуль у 4-й гілці")

        radicand = power_check(x, c) + b**2
        if radicand < 0:
            raise ValueError("Від’ємне підкореневе у 4-й гілці")

        value = math.sqrt(radicand) / denominator
        return value, "x > 1, a = 0, b < 0, c != 0"

    else:
        value = (a * x + c) * (b * x - c)
        return value, "(a * x + c) * (b * x - c)"


try:
    x = float(input("Введіть x: "))
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    value, branch = F(x, a, b, c)

    print("Обчислено при", branch)
    print("Результат:", value)

except ZeroDivisionError as e:
    print("Помилка:", e)

except ValueError as e:
    print("Помилка:", e)

except Exception as e:
    print("Невідома помилка:", e)
