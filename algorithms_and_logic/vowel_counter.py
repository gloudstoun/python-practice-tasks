def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Примеры вызова функции для проверки:
print("--- Подсчет гласных ---")
print(f"'hello': {count_vowels('hello')}")                           # Ожидаем: 2
print(f"'Programming is fun': {count_vowels('Programming is fun')}") # Ожидаем: 5
print(f"'AEIOU': {count_vowels('AEIOU')}")                           # Ожидаем: 5
print(f"'Rhythm': {count_vowels('Rhythm')}")                         # Ожидаем: 0
print(f"Пустая строка: {count_vowels('')}")                          # Ожидаем: 0
print(f"'Python': {count_vowels('Python')}")                         # Ожидаем: 1
print(f"'aAbBcCdDeE': {count_vowels('aAbBcCdDeE')}")                 # Ожидаем: 4