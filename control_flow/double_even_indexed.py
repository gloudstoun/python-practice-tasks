def double_even_indexed_numbers(numbers):
    result_numbers = []

    for index in range(len(numbers)):
        current_number = numbers[index]

        if index % 2 == 0:
            current_number = current_number * 2
            result_numbers.append(current_number)
        else:
            result_numbers.append(current_number)

    return result_numbers

# Примеры вызова функции для проверки:
print("--- Удвоение чисел на четных позициях ---")
print(f"[1, 2, 3, 4, 5]: {double_even_indexed_numbers([1, 2, 3, 4, 5])}")       # Ожидаем: [2, 2, 6, 4, 10]
print(f"[10, 20, 30]: {double_even_indexed_numbers([10, 20, 30])}")           # Ожидаем: [20, 20, 60]
print(f"[1, 1, 1, 1]: {double_even_indexed_numbers([1, 1, 1, 1])}")           # Ожидаем: [2, 1, 2, 1]
print(f"[]: {double_even_indexed_numbers([])}")                               # Ожидаем: []
print(f"[5]: {double_even_indexed_numbers([5])}")                             # Ожидаем: [10]
print(f"[2, 4, 6]: {double_even_indexed_numbers([2, 4, 6])}")                 # Ожидаем: [4, 4, 12]