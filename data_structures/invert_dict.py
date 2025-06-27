def invert_dictionary(original_dict):
    inverted_dict = {}

    for key, value in original_dict.items():
        if value in inverted_dict:
            # Если value уже есть как ключ в inverted_dict,
            # просто добавляем текущий key в существующий список
            # Например, если inverted_dict[value] было ['a'], то после append(key) станет ['a', 'c']
            inverted_dict[value].append(key)
        else:
            # Если value еще нет как ключа в inverted_dict,
            # создаем новую запись, где value - ключ, а значение - НОВЫЙ СПИСОК,
            # содержащий только текущий key
            inverted_dict[value] = [key] # Обратите внимание на квадратные скобки!

    # Если требуется, чтобы значения были не списками, а одиночными элементами, когда они уникальны:
    final_inverted_dict = {}
    for value_key, original_keys_list in inverted_dict.items():
        if len(original_keys_list) == 1:
            final_inverted_dict[value_key] = original_keys_list[0] # Если список из одного элемента, берем сам элемент
        else:
            final_inverted_dict[value_key] = original_keys_list # Иначе оставляем список
            
    return final_inverted_dict


# Примеры вызова функции для проверки:
print("--- Инвертирование словаря ---")
print(f"{{'a': 1, 'b': 2, 'c': 3}}: {invert_dictionary({'a': 1, 'b': 2, 'c': 3})}") # Ожидаем: {1: 'a', 2: 'b', 3: 'c'}
print(f"{{'a': 1, 'b': 2, 'c': 1}}: {invert_dictionary({'a': 1, 'b': 2, 'c': 1})}") # Ожидаем: {1: ['a', 'c'], 2: 'b'}
print(f"{{'key1': 'valueA', 'key2': 'valueB', 'key3': 'valueA', 'key4': 'valueC'}}: {invert_dictionary({'key1': 'valueA', 'key2': 'valueB', 'key3': 'valueA', 'key4': 'valueC'})}") # Ожидаем: {'valueA': ['key1', 'key3'], 'valueB': 'key2', 'valueC': 'key4'}
print(f"{{}}: {invert_dictionary({})}") # Ожидаем: {}
print(f"{{'x': 10}}: {invert_dictionary({'x': 10})}") # Ожидаем: {10: 'x'}