def count_words(sentence):
    count = 0
    in_word = False

    # Вариант со split()
    #words = sentence.split()
    #for word in words:
        #count += 1
    #return count

    # Этот код без использования функций я нашел в интернете
    for char in sentence:
        if ' ' != char:  # Если текущий символ не пробел
            if not in_word:  # Если до этого не было слова
                count += 1  # Начинается новое слово
                in_word = True  # Устанавливаем флаг
        else:
            in_word = False  # Если пробел, сбрасываем флаг

    return count


# Примеры вызова функции для проверки:
print("--- Подсчет количества слов ---")
print(f"'Hello world': {count_words('Hello world')}")               # Ожидаем: 2
print(f"'Python is fun': {count_words('Python is fun')}")           # Ожидаем: 3
print(f"'One': {count_words('One')}")                               # Ожидаем: 1
print(f"': {count_words(' ')}")                                   # Ожидаем: 0
print(f"'': {count_words('')}")                                   # Ожидаем: 0
print(f"'   leading and trailing spaces   ': {count_words('   leading and trailing spaces   ')}") # Ожидаем: 4
print(f"'One Two  Three': {count_words('One Two  Three')}")         # Ожидаем: 3 (множественные пробелы)