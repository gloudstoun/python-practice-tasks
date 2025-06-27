
def count_vowels(text):
    all_vowels = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u'}
    text = text.lower()
    vowels_count = 0

    for char in text:
        if char in all_vowels:
            vowels_count += 1
    return vowels_count

    # 1. Определите все гласные буквы (в нижнем регистре).
    # 2. Преобразуйте входную строку text в нижний регистр.
    # 3. Инициализируйте счетчик гласных.
    # 4. Пройдитесь циклом по каждому символу в преобразованной строке.
    # 5. Проверьте, является ли текущий символ гласной.
    # 6. Увеличьте счетчик, если это гласная.
    # 7. Верните счетчик.
    

print("--- Подсчет гласных ---")
print(f"'Привет, мир!': {count_vowels('Привет, мир!')}")    # Ожидаем: 3
print(f"'Hello World': {count_vowels('Hello World')}")      # Ожидаем: 3
print(f"'Python': {count_vowels('Python')}")                # Ожидаем: 1
print(f"'aeiou': {count_vowels('aeiou')}")                  # Ожидаем: 5
print(f"'Rhythm': {count_vowels('Rhythm')}")                # Ожидаем: 0
print(f"'' : {count_vowels('')}")                            # Ожидаем: 0
print(f"'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ': {count_vowels('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')}") # Ожидаем: 9 (А, Е, И, О, У, Ы, Э, Ю, Я)