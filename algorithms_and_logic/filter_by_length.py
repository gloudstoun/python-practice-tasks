
def filter_strings_by_length(strings, min_length):
    
    result_strings = []

    for str in strings:
        if len(str) >= min_length:
            result_strings.append(str)
    return result_strings

# Примеры вызова функции для проверки:
print("--- Фильтрация строк по длине ---")
print(f"(['apple', 'banana', 'cat', 'dog'], 5): {filter_strings_by_length(['apple', 'banana', 'cat', 'dog'], 5)}") # Ожидаем: ['apple', 'banana']
print(f"(['a', 'bb', 'ccc'], 2): {filter_strings_by_length(['a', 'bb', 'ccc'], 2)}")           # Ожидаем: ['bb', 'ccc']
print(f"(['one', 'two', 'three'], 10): {filter_strings_by_length(['one', 'two', 'three'], 10)}") # Ожидаем: []
print(f"([], 3): {filter_strings_by_length([], 3)}")                                         # Ожидаем: []
print(f"(['python'], 6): {filter_strings_by_length(['python'], 6)}")                         # Ожидаем: ['python']
print(f"([''], 0): {filter_strings_by_length([''], 0)}")                                     # Ожидаем: ['']
print(f"(['Hello', 'hi', 'a'], 3): {filter_strings_by_length(['Hello', 'hi', 'a'], 3)}")     # Ожидаем: ['Hello']