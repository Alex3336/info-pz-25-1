name = "Олександр"
surname = "Шарандак"
group = "ПЗ-25-1"

author = f"{surname} {name} \t {group} \n"
p, q, u, v = -8, 2, 4, -1
spisok = [29, 1.47, -1.53, 0.38, -67, 96, -3.08, 5, 2, -15]


def power_check(base, exponent):
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("Помилка: нуль не можна підносити до від'ємного степеня")
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Помилка: від'ємне число у дробовому степені")
    return base**exponent

Rsult_1 = p / u + u / (2 * v) - (2 * p - q) / v + (4 * u) / p
Rsult_2 = ((2 * u) / (3 * q) - (v - 2) / p) / ((p * u) / v - (u + v) / (p + 2 * q))
Rsult_3 = (
    (3 * p**2) / 2 - (2 * q**3) + (3 * u**-3) / 8 - (4 * v**-2) / 5
)
Rsult_4 = (
    p * v / (u**2 + q**2) - (4 * v - p * q) / (1 + u**2) + q**3 / u
)
Rsult_5 = ((3 * p + q * v) ** 2 - u**4) / (u**2 + v**2 + 6)
Rsult_6 = power_check(p, 2 * u - 3 * q) - 4 ** (2 * v) + 8 * power_check(q, 3 * p + 2)
Rsult_7 = (2**q * power_check(p**2 - 3 * q**3, v)) / 3**u - (
    2**u * power_check(u, 3 * v)
) / (3 * p + 4**u)
Rsult_8 = (
    (power_check(q, 4 * u - 1) - 3 ** (2 * p)) / 5 ** (u - 2 * v)
    - (3 * p**3) / 3 ** (u + v)
    + u**2 / (v**3 + 3**v)
)
Rsult_9 = p * spisok[2] / (q * spisok[4]) - spisok[6] * spisok[8] / (
    2 * u * v * spisok[0]
)
Rsult_10 = (
    spisok[0] ** 2 / p**2
    - spisok[1] / q**-2
    + spisok[5] ** 3 / power_check(u, p)
    - spisok[9] / power_check(v, q)
)

print(author)
print(f"p = {p:<4}\tq = {q:<4}\tu = {u:<4}\tv = {v:<4}\n")
print("Rsult_1 =", Rsult_1)
print("Rsult_2 =", Rsult_2)
print("Rsult_3 =", Rsult_3)
print("Rsult_4 =", Rsult_4)
print("Rsult_5 =", Rsult_5)
print("Rsult_6 =", Rsult_6)
print("Rsult_7 =", Rsult_7)
print("Rsult_8 =", Rsult_8)
print("Rsult_9 =", Rsult_9)
print("Rsult_10 =", Rsult_10)
print(f"\nResult_1 > Result_9 \t {Rsult_1 > Rsult_9}")
print(f"Result_2 < Result_4 \t {Rsult_2 < Rsult_4}")
print(f"Result_5 < Result_7 \t {Rsult_5 < Rsult_7}")
print(f"Result_6 > Result_8 \t {Rsult_6 > Rsult_8}")
print(f"Result_3 > Result_10 \t {Rsult_3 > Rsult_10}\n")


Rsult_list = [
    Rsult_1,
    Rsult_2,
    Rsult_3,
    Rsult_4,
    Rsult_5,
    Rsult_6,
    Rsult_7,
    Rsult_8,
    Rsult_9,
    Rsult_10,
]
print(f"Rsult_list:\n{Rsult_list} \nКількість елементів: {len(Rsult_list)}\n")

Rsult_list.sort()
print(f"Сортування за зростанням:\n{Rsult_list}\n")

Rsult_list.sort(reverse=1)
print(f"Сортування за спаданням:\n{Rsult_list}\n")

print(f"Максимальне значення серед результатів:\t{round(max(Rsult_list), 3)}")
print(f"Мінімальне значення серед результатів:\t{round(min(Rsult_list), 3)}")
print(f"Сума отриманих результатів:\t{round(sum(Rsult_list), 3)}")
