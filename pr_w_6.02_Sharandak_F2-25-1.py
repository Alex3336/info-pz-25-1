def Factorial(x):
    """Обчислення факторіала числа x."""
    P = 1
    for i in range(1, x + 1):
        P *= i
    return P

def Allocation(x, y):
    """Обчислення кількості розміщень (A)."""
    if y > x: return 0
    A = Factorial(x) / Factorial(x - y)
    return int(A)

def Combinations(x, y):
    """Обчислення кількості комбінацій (C)."""
    if y > x: return 0
    C = Factorial(x) / (Factorial(y) * Factorial(x - y))
    return int(C)
