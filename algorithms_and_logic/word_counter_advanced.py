
def count_words(text):
   
    text = text.split()
    count_word = 0

    for word in text:
        count_word += 1
    
    return count_word

print("--- Подсчет слов ---")
print(f"'Hello World': {count_words('Hello World')}")                  # Ожидаем: 2
print(f"'  Python is fun  ': {count_words('  Python is fun  ')}")      # Ожидаем: 3
print(f"'OneWord': {count_words('OneWord')}")                          # Ожидаем: 1
print(f"'' : {count_words('')}")                                       # Ожидаем: 0
print(f"'  ': {count_words('  ')}")                                     # Ожидаем: 0
print(f"'Это тестовая строка для подсчета слов': {count_words('Это тестовая строка для подсчета слов')}") # Ожидаем: 6
print(f"'Слова   с    разным     количеством   пробелов': {count_words('Слова   с    разным     количеством   пробелов')}") # Ожидаем: 6