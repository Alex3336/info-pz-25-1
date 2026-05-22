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

if s == 0:
    while k == f:
        print("k не може дорівнювати f. Будь ласка, введіть інше значення для k та f.")
        k = input_check("Вкажіть значення:\nk = ")
        f = input_check("Вкажіть значення:\nf = ")
elif s != 0:
    while h < 0:
        print("Помилка: значення h не може бути від'ємним для обчислення кореня. Будь ласка, введіть невід'ємне число.")
        h = input_check("Вкажіть значення:\nh = ")

print(f"\ns = {s}\nf = {f}\nk = {k}\nh = {h}")


def g_calculate(f, k, s, h):
    if s == 0:
        numerator = f - k
        denominator = f + k
        return division_check(numerator, denominator, "Ділення на нуль"), "s = 0"
    else:
        return f - sqrt_check(2 * h, 3), "s != 0"


try:
    result = g_calculate(f, k, s, h)
    print(result[1])
    print(f"g({f}, {k}, {s}, {h}) = {result[0]}")

except ZeroDivisionError as error:
    print(error)

except ValueError as error:
    print(error)

except OverflowError:
    print("Помилка переповнення числа!")

except Exception as error:
    print(f"Невідома помилка: {error}")
