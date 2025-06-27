def remove_duplicates(items):
    result = []
    for i in items:
        if i not in result:
            result.append(i)
    return result

# Примеры вызова функции для проверки:
print("--- Удаление дубликатов ---")
print(f"[1, 2, 2, 3, 1, 4]: {remove_duplicates([1, 2, 2, 3, 1, 4])}")               # Ожидаем: [1, 2, 3, 4]
print(f"['apple', 'banana', 'apple', 'orange']: {remove_duplicates(['apple', 'banana', 'apple', 'orange'])}") # Ожидаем: ['apple', 'banana', 'orange']
print(f"[5, 5, 5, 5]: {remove_duplicates([5, 5, 5, 5])}")                           # Ожидаем: [5]
print(f"[]: {remove_duplicates([])}")                                             # Ожидаем: []
print(f"[1, 2, 3]: {remove_duplicates([1, 2, 3])}")                               # Ожидаем: [1, 2, 3]
print(f"[True, False, True, False]: {remove_duplicates([True, False, True, False])}") # Ожидаем: [True, False]