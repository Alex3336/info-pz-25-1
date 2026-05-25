name = "Олександр"
surname = "Шарандак"
group = "ПЗ-25-1"

module = __import__("pr_w_6_02_Sharandak_F2-25-1")
Factorial = module.Factorial
Allocation = module.Allocation
Combinations = module.Combinations

print(f"{name} {surname} \t {group} \n")

try:
    n = int(input("Укажіть загальну кількість елементів (n): "))
    
    print("Чи враховується порядок наступності у сполуці?\n 1 - так\n 2 - ні")
    question_1 = int(input("Оберіть варіант відповіді: "))


    if question_1 == 2:
        k = int(input("Укажіть кількість елементів, які використовуються (k): "))
        print(f"\nКількість комбінацій C({n}, {k}) = {Combinations(n, k)}")
    else:
        print("Чи всі елементи входять до сполуки?\n 1 - так\n 2 - ні")

        question_2 = int(input("Оберіть варіант відповіді: "))

        if question_2 == 1:
            print(f"\nКількість перестановок P({n}) = {Factorial(n)}")
        else:
            k = int(input("Укажіть кількість елементів, які використовуються (k): "))
            print(f"\nКількість розміщень A({n}, {k}) = {Allocation(n, k)}")

except ValueError:
    print("Помилка: введіть ціле число.")
except Exception as e:
    print(f"Виникла помилка: {e}")

print("\nПрограму завершено.")
