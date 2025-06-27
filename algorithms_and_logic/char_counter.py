def count_char_occurrences(text, char_to_find):
    text = text.lower()
    char_to_find = char_to_find.lower()
    count = 0

    for char in text:
        if char == char_to_find:
            count += 1
    return count

# Примеры вызова функции для проверки:
print("--- Подсчет вхождений символа ---")
print(f"('hello world', 'o'): {count_char_occurrences('hello world', 'o')}")       # Ожидаем: 2
print(f"('Programming is fun', 'g'): {count_char_occurrences('Programming is fun', 'g')}") # Ожидаем: 2
print(f"('Apple', 'P'): {count_char_occurrences('Apple', 'P')}")               # Ожидаем: 2
print(f"('banana', 'a'): {count_char_occurrences('banana', 'a')}")             # Ожидаем: 3
print(f"('test', 'z'): {count_char_occurrences('test', 'z')}")                 # Ожидаем: 0
print(f"('', 'a'): {count_char_occurrences('', 'a')}")                         # Ожидаем: 0
print(f"('AaBbCc', 'a'): {count_char_occurrences('AaBbCc', 'a')}")             # Ожидаем: 2