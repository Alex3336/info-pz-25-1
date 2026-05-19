login_reg = "student"
password_reg = "pz-25-1"

login = input("Укажіть логін: ")
password = input("Укажіть пароль: ")

while login != login_reg or password != password_reg:
    print("Невірний логін або пароль")
    login = input("Укажіть логін: ")
    password = input("Укажіть пароль: ")

print("Вхід виконано успішно!\n")

arr = []

for i in range(1, 11):
    element = int(input(f"Введіть {i}-й елемент масиву: "))
    arr.append(element)

print("arr:", arr)

count_zero = arr.count(0)
print("Кількість нулів у масиві:", count_zero)

arr.sort()
print("Сортування за зростанням:", arr)

min_element = min(arr)
max_element = max(arr)
print("Мінімальний елемент:", min_element)
print("Максимальний елемент:", max_element)

Avg = sum(arr) / len(arr)
print("Середнє арифметичне:", Avg)

Sum_dodat = 0
Dobutok_not_par = 1

for i in arr:
    if i > 0:
        Sum_dodat += i
        # print(f"Елемент {i} > 0")
    if i % 2 != 0:
        Dobutok_not_par *= i
        # print(f"Елемент {i} не парний")

print("Сума додатніх елементів:", Sum_dodat)
print("Добуток непарних елементів:", Dobutok_not_par)