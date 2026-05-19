name = "Олександр"
surname = "Шарандак"
group = "ПЗ-25-1"
a = -8
b = 2
c = 4.98
d = -1.2
x, y = 1.6, 2
data = [29, 1.47, -1.53, 0.38, -67, 96, -3.08, 5, 2, -35]


def power_check(base, exponent):
    if base == 0 and exponent < 0:
        raise ZeroDivisionError("Помилка: нуль не можна підносити до від'ємного степеня")
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Помилка: від'ємне число у дробовому степені")
    return base**exponent

print(name, surname, group)
print("a =", a, type(a))
print("b =", b, type(b))
print("c =", c, type(c))
print("d =", d, type(d))
print("x =", x, type(x))
print("y =", y, type(y))
print("data =", data, type(data))

print("\nКількість елементів об'єкту data:", len(data))
print("1-й елемент об'єкту data:", data[0], type(data[0]))
print("3-й елемент об'єкту data:", data[2], type(data[2]))
print("Останній елемент об'єкту data:", data[-1], type(data[-1]))

print("\nМінімальне значення серед елементів data:", min(data))
print("Максимальне значення серед елементів data:", max(data))

print("\nСума елементів data:", sum(data))
print("Середнє арифметичне елементів data:", sum(data) / len(data))


Sum_1 = a + b
Sum_2 = b + a
Dif_1 = a - b
Dif_2 = b - a
Mult_1 = a * b
Mult_2 = b * a
Quot_1 = a / b
Quot_2 = b / a
Exp_1 = a**b
Exp_2 = b**a

print("\na + b =", Sum_1, type(Sum_1))
print("b + a =", Sum_2, type(Sum_2))
print("a - b =", Dif_1, type(Dif_1))
print("b - a =", Dif_2, type(Dif_2))
print("a * b =", Mult_1, type(Mult_1))
print("b * a =", Mult_2, type(Mult_2))
print("a / b =", Quot_1, type(Quot_1))
print("aᵇ =", Exp_1, type(Exp_1))
print("bᵃ =", Exp_2, type(Exp_2))

Result_1 = x - y * b
Result_2 = (x + y) * b
print("\nResult_1 =", Result_1)
print("Result_2 =", Result_2)
print("Result_1 = Result_2 \t", Result_1 == Result_2)

Result_3 = c + x / d + y
Result_4 = (c + x) / (d + y)
print("\nResult_3 =", Result_3)
print("Result_4 =", Result_4)
print("Result_3 = Result_4\t", Result_3 == Result_4)

Result_5 = a * b / x
Result_6 = (a * b) / x
print("\nResult_5 =", Result_5)
print("Result_6 =", Result_6)
print("Result_5 = Result_6\t", Result_5 == Result_6)

Result_7 = a / b * x
Result_8 = a / (b * x)
print("\nResult_7 =", Result_7)
print("Result_8 =", Result_8)
print("Result_7 = Result_8\t", Result_7 == Result_8)

Result_9 = b ** power_check(a, y)
Result_10 = b ** (power_check(a, y))
print("\nResult_9 =", Result_9)
print("Result_10 =", Result_10)
print("Result_9 = Result_10\t", Result_9 == Result_10)

print("\nResult_1 > Result_2", Result_1 > Result_2)
print("Result_3 < Result_4", Result_3 < Result_4)
print("Result_5 # Result_6", Result_5 != Result_6)
print("Result_7 < Result_8", Result_7 < Result_8)
print("Result_9 > Result_10", Result_9 >= Result_10)

Result_11 = 3 * data[2] + data[4] / data[6]
Result_12 = power_check(data[0], data[5]) + power_check(data[7], data[8])
Result_13 = (data[1] + data[6]) / (data[2] * data[4] - data[7])
Result_14 = data[3] // data[4]
Result_15 = data[3] % 4

print("\nResult_11 =", Result_11)
print("Result_12 =", Result_12)
print("Result_13 =", Result_13)
print("Result_14 =", Result_14)
print("Result_15 =", Result_15)

Result_data = [
    round(Result_1, 2),
    round(Result_2, 2),
    round(Result_3, 2),
    round(Result_4, 2),
    round(Result_5, 2),
    round(Result_6, 2),
    round(Result_7, 2),
    round(Result_8, 2),
    round(Result_9, 2),
    round(Result_10, 2),
    round(Result_11, 2),
    round(Result_12, 2),
    round(Result_13, 2),
    round(Result_14, 2),
    round(Result_15, 2),
]
print(f"\nResult_data = {Result_data} \nКількість елементів: {len(Result_data)}")

Result_data.sort()
print(f"\nСортування за зростанням: \nResult_data =  {Result_data}")

Result_data.sort(reverse=1)
print(f"Сортування за спаданням: \nResult_data = {Result_data}")

conclusion = (
    "Практичну роботу №1"
    + "\n"
    + "виконав(ла) студент(ка) "
    + group
    + "\n"
    + surname
    + " "
    + name
)
print(conclusion)
