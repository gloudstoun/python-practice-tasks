def count_elements(elements_list):
    element_counts = {}

    for char in elements_list:
        if char in element_counts:
            element_counts[char] += 1
        else:
            element_counts[char] = 1

    
    # Переберите каждый элемент в elements_list
    # Если элемент уже есть в словаре, увеличьте его счетчик
    # Иначе, добавьте элемент в словарь со значением 1

    # Верните заполненный словарь
    return element_counts

# Примеры для проверки:
print("--- Подсчет элементов в списке ---")
print(f"Список ['яблоко', 'банан', 'яблоко', 'апельсин', 'банан', 'яблоко']: {count_elements(['яблоко', 'банан', 'яблоко', 'апельсин', 'банан', 'яблоко'])}")
print(f"Список [1, 2, 2, 3, 3, 3]: {count_elements([1, 2, 2, 3, 3, 3])}")
print(f"Пустой список []: {count_elements([])}")
print(f"Список ['cat', 'dog', 'cat', 'elephant']: {count_elements(['cat', 'dog', 'cat', 'elephant'])}")