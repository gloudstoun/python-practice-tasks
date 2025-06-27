
def find_max_number(numbers):
    

    if not numbers:
        return None
    
    max_num = numbers[0]

    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
    

# Примеры вызова функции для проверки:
print("--- Поиск максимального числа ---")
print(f"[1, 5, 2, 8, 3]: {find_max_number([1, 5, 2, 8, 3])}")     # Ожидаем: 8
print(f"[10, 2, 30, 5]: {find_max_number([10, 2, 30, 5])}")       # Ожидаем: 30
print(f"[-1, -5, -2]: {find_max_number([-1, -5, -2])}")           # Ожидаем: -1
print(f"[7]: {find_max_number([7])}")                             # Ожидаем: 7
print(f"[]: {find_max_number([])}")                               # Ожидаем: None
print(f"[0, 0, 0]: {find_max_number([0, 0, 0])}")                 # Ожидаем: 0
print(f"[-10, -1, -5]: {find_max_number([-10, -1, -5])}")         # Ожидаем: -1