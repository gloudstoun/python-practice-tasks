
def sum_elements_between_zeros(numbers):
    result_sum = 0
    first_zero_index = None
    second_zero_index = None

    for i, numer in enumerate(numbers):
        if numer == 0:
            first_zero_index = i
            break
    if first_zero_index == None:
        return 0

    for i in range(first_zero_index + 1, len(numbers)):
        if numbers[i] == 0:
            second_zero_index = i
            break
    if second_zero_index == None:
        return 0
        
    for i in range(first_zero_index + 1, second_zero_index):
        result_sum += numbers[i]

    return result_sum



''' Вариант решения через флаг
    counting_active = False
    for number in numbers:
            if number == 0:
                if counting_active:
                    return result_sum
                else:
                     counting_active = True
            elif counting_active:
                 result_sum += number
    return 0

'''

# Примеры вызова функции для проверки:
print("--- Сумма элементов между нулями ---")
print(f"[1, 0, 5, 2, 0, 8]: {sum_elements_between_zeros([1, 0, 5, 2, 0, 8])}")     # Ожидаем: 7
print(f"[0, 10, 20, 0, 30]: {sum_elements_between_zeros([0, 10, 20, 0, 30])}")   # Ожидаем: 30
print(f"[1, 2, 3]: {sum_elements_between_zeros([1, 2, 3])}")                     # Ожидаем: 0
print(f"[0, 1, 2]: {sum_elements_between_zeros([0, 1, 2])}")                     # Ожидаем: 0
print(f"[0, 0, 5]: {sum_elements_between_zeros([0, 0, 5])}")                     # Ожидаем: 0
print(f"[0, -1, 0]: {sum_elements_between_zeros([0, -1, 0])}")                   # Ожидаем: -1
print(f"[0, 1, 0, 2, 0, 3]: {sum_elements_between_zeros([0, 1, 0, 2, 0, 3])}")   # Ожидаем: 1
print(f"[5, 0, 1, 2, 3, 0, 4]: {sum_elements_between_zeros([5, 0, 1, 2, 3, 0, 4])}") # Ожидаем: 6