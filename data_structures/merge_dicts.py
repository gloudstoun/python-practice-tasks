def merge_dictionaries(dict1, dict2):
    merged_dict = {}

    
    # 1. Добавьте все пары из dict1 в merged_dict
    #for key, value in dict1.items():
        #merged_dict[key] = value

    # 2. Теперь добавьте или обновите пары из dict2 в merged_dict
    #    (ключи из dict2 перезапишут существующие, если они есть)
    #for key, value in dict2.items():
        #merged_dict[key] = value

    # Более питонячий способ
    merged_dict.update(dict1)
    merged_dict.update(dict2)   

    return merged_dict, dict1, dict2

# Примеры для проверки:
print("--- Объединение словарей ---")
print(f"Объединение {{'a': 1, 'b': 2}} и {{'c': 3, 'd': 4}}: {merge_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4})}")
print(f"Объединение {{'a': 1, 'b': 2}} и {{'b': 3, 'c': 4}}: {merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})}")
print(f"Объединение {{}} и {{'x': 10}}: {merge_dictionaries({}, {'x': 10})}")
print(f"Объединение {{'y': 20}} и {{}}: {merge_dictionaries({'y': 20}, {})}")
print(f"Объединение {{}} и {{}}: {merge_dictionaries({}, {})}")