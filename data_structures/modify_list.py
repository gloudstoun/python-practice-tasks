def modify_list_elements(numbers):
   
    result_numbers = []
    for number in numbers:
        if number % 2 == 0:
            number = number + 10
            result_numbers.append(number)
        else:
            number = number - 5
            result_numbers.append(number)
    return result_numbers

# Примеры вызова функции для проверки:
print("--- Изменение элементов списка ---")
print(f"[1, 2, 3, 4, 5]: {modify_list_elements([1, 2, 3, 4, 5])}")       # Ожидаем: [-4, 12, -2, 14, 0]
print(f"[10, 20, 30]: {modify_list_elements([10, 20, 30])}")           # Ожидаем: [20, 30, 40]
print(f"[1, 3, 5]: {modify_list_elements([1, 3, 5])}")                 # Ожидаем: [-4, -2, 0]
print(f"[]: {modify_list_elements([])}")                               # Ожидаем: []
print(f"[0]: {modify_list_elements([0])}")                             # Ожидаем: [10]
print(f"[-1, -2, -3]: {modify_list_elements([-1, -2, -3])}")           # Ожидаем: [-6, 8, -8]