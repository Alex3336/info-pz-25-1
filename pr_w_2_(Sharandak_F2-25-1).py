from math import *

name = "Олександр"
surname = "Шарандак"
group = "ПЗ-25-1"

author = f"{name} {surname} \t {group} \n"
print(author)


R = float(input("Вкажіть радіус кола: "))
S_circle = pi * R**2
L_circle = 2 * pi * R

print("S_circle:", S_circle)
print("L_circle:", L_circle)

a = float(input("Вкажіть сторони трикутника:\na = "))
b = float(input("b = "))
c = float(input("c = "))

while a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Трикутник не існує, введіть коректні значення")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

p_triangle = (a + b + c) / 2
S_triangle = sqrt(p_triangle * (p_triangle - a) * (p_triangle - b) * (p_triangle - c))
R_described = (a * b * c) / (4 * S_triangle)
R_incribed = S_triangle / p_triangle

print("Периметр трикутника: \nP = ", p_triangle * 2)
print("S_triangle:", S_triangle)
print("R_described:", R_described)
print("R_incribed:", R_incribed)

sin_alpha = a / (2 * R_described)
alpha_rad = asin(sin_alpha)
alpha_deg = round(degrees(alpha_rad))

cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)
gamma_rad = acos(cos_gamma)
gamma_deg = round(degrees(gamma_rad))

beta_deg = 180 - alpha_deg - gamma_deg

print("alpha_deg:", alpha_deg)
print("gamma_deg:", gamma_deg)
print("beta_deg:", beta_deg)

x_1 = float(input("Вкажіть абсцису початкової точки вектора:\nx₁ = "))
y_1 = float(input("Вкажіть ординату початкової точки вектора:\ny₁ = "))
x_2 = float(input("Вкажіть абсцису кінцевої точки вектора:\nx₂ = "))
y_2 = float(input("Вкажіть ординату кінцевої точки вектора:\ny₂ = "))

a_1 = x_2 - x_1
a_2 = y_2 - y_1
len_vector_a = sqrt(a_1**2 + a_2**2)

print(f"координати вектора а: {a_1, a_2}\nДовжина вектора а: {len_vector_a}")
