def filter_even_numbers(numbers):
    counter = []
    for i in numbers:
        if i % 2 == 0:
            counter.append(i)
    return counter

print("--- Фильтрация четных чисел ---")
print(f"[1, 2, 3, 4, 5, 6]: {filter_even_numbers([1, 2, 3, 4, 5, 6])}")     # Ожидаем: [2, 4, 6]
print(f"[10, 11, 12, 13]: {filter_even_numbers([10, 11, 12, 13])}")         # Ожидаем: [10, 12]
print(f"[1, 3, 5, 7]: {filter_even_numbers([1, 3, 5, 7])}")                 # Ожидаем: []
print(f"[]: {filter_even_numbers([])}")                                     # Ожидаем: []
print(f"[-2, 0, 5, -8]: {filter_even_numbers([-2, 0, 5, -8])}")             # Ожидаем: [-2, 0, -8]
print(f"[42]: {filter_even_numbers([42])}")                                 # Ожидаем: [42]
print(f"[43]: {filter_even_numbers([43])}")                                 # Ожидаем: []