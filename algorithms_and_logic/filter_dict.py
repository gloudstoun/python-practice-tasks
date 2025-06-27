def filter_by_value(original_dict, min_value):
    filtered_dict = {}

    for key, value in original_dict.items():
        if value >= min_value:
            filtered_dict[key] = value

    return filtered_dict

# Примеры для проверки:
grades1 = {"Аня": 85, "Борис": 92, "Вика": 78, "Саша": 95, "Маша": 100}
print("--- Фильтрация словаря ---")
print(f"Исходный: {grades1}")
print(f"Фильтр >= 90: {filter_by_value(grades1, 90)}")
print(f"Фильтр >= 80: {filter_by_value(grades1, 80)}")
print(f"Фильтр >= 100: {filter_by_value(grades1, 100)}")
print(f"Фильтр пустого словаря: {filter_by_value({}, 50)}")