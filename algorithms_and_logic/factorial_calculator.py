def calculate_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    sum_n = 1
    for i in range(sum_n, n + 1):
        sum_n = sum_n * i
    return sum_n

# Примеры вызова функции для проверки:
print("--- Вычисление факториала ---")
print(f"Факториал 0: {calculate_factorial(0)}")    # Ожидаем: 1
print(f"Факториал 1: {calculate_factorial(1)}")    # Ожидаем: 1
print(f"Факториал 3: {calculate_factorial(3)}")    # Ожидаем: 6
print(f"Факториал 5: {calculate_factorial(5)}")    # Ожидаем: 120
print(f"Факториал -1: {calculate_factorial(-1)}")   # Ожидаем: None
print(f"Факториал 4: {calculate_factorial(4)}")    # Ожидаем: 24
