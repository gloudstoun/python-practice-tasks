def reverse_list_with_indices(items):
    result_items = []
    for i in range(len(items) - 1, -1, -1):
        result_items.append(items[i])
    return result_items

print("--- Обратный порядок списка (по индексам) ---")
print(f"[1, 2, 3, 4, 5]: {reverse_list_with_indices([1, 2, 3, 4, 5])}")       # Ожидаем: [5, 4, 3, 2, 1]
print(f"['a', 'b', 'c']: {reverse_list_with_indices(['a', 'b', 'c'])}")       # Ожидаем: ['c', 'b', 'a']
print(f"['hello']: {reverse_list_with_indices(['hello'])}")                 # Ожидаем: ['hello']
print(f"[]: {reverse_list_with_indices([])}")                               # Ожидаем: []
print(f"[10, 20]: {reverse_list_with_indices([10, 20])}")                   # Ожидаем: [20, 10]
print(f"[True, False, True]: {reverse_list_with_indices([True, False, True])}") # Ожидаем: [True, False, True]