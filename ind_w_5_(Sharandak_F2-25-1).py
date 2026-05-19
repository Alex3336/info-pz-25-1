from math import factorial, log


def power_check(base, exponent):
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("Помилка: нуль не можна підносити до від'ємного степеня")
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Помилка: від'ємне число у дробовому степені")
    return base**exponent

text = [
    "Мета. Ознайомлення з основними поняттями циклів",
    "for та while у мові Python. Використання циклів",
    "для виконання одного й того ж блоку даних n-разів.",
]

print("Індивідуальне завдання 5")
print("Тема. Застосування циклів у процесі розробки алгоритмів мовою Python.")
print(text[0])
for line in text[1:]:
    print("   " + line)
print("Варіант №18\n")
print("а) Обчислення добутку ряду")

P = 1

for i in range(2, 10):
    ch = (i + 1) * factorial(i) + log(i)
    zn = i**2 - factorial(i + 1)
    term = power_check(-1, i) * (ch / zn)
    P *= term
    print(
        f"Крок {i - 1}: i = {i}, чисельник = {ch:.6f}, "
        f"знаменник = {zn:.6f}, множник = {term:.6f}, P = {P:.6f}"
    )

print("Добуток P =", P)

print("\nб) Сума нескінченного ряду: x + x^3/3 + x^5/5 + ...")

x = float(input("Введіть x: "))
eps = float(input("Введіть точність eps: "))
max_iter = int(input("Введіть максимальну кількість ітерацій: "))

S = 0
n = 0

while n < max_iter:
    power = 2 * n + 1
    term = power_check(x, power) / power

    S += term

    print(
        f"Ітерація {n + 1}: член x^{power}/{power} = {term:.6f}, "
        f"поточна сума S = {S:.6f}"
    )

    n += 1

    if abs(term) < eps:
        break

print("\nСума ряду S =", S)
print("Ітерацій виконано:", n)
