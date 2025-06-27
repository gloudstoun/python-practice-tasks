import math 

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0: 
        return False
    else:
        for i in range(3, math.isqrt(number) + 1, 2):
            if number % i == 0:
                return False
        return True

print("--- Проверка на простое число ---")
print(f"Число 1: {is_prime(1)}")   # Ожидаем False
print(f"Число 2: {is_prime(2)}")   # Ожидаем True
print(f"Число 3: {is_prime(3)}")   # Ожидаем True
print(f"Число 4: {is_prime(4)}")   # Ожидаем False
print(f"Число 7: {is_prime(7)}")   # Ожидаем True
print(f"Число 11: {is_prime(11)}") # Ожидаем True
print(f"Число 13: {is_prime(13)}") # Ожидаем True
print(f"Число 15: {is_prime(15)}") # Ожидаем False
print(f"Число 17: {is_prime(17)}") # Ожидаем True
print(f"Число 29: {is_prime(29)}") # Ожидаем True
print(f"Число 100: {is_prime(100)}") # Ожидаем False
print(f"Число 97: {is_prime(97)}") # Ожидаем True
print(f"Число -5: {is_prime(-5)}") # Ожидаем False