import string # Можете использовать string.punctuation для списка всех знаков препинания

def count_unique_words(text):

    # 1. Предварительная обработка строки:
    #    а) Привести к нижнему регистру.
    text = text.lower()
    result_text = []

    #    б) Удалить знаки препинания (можно заменить их на пробелы, или отфильтровать).
    for char in text:
        if char not in string.punctuation: result_text.append(char)
    cleaned_text = "".join(result_text)

    #    в) Разбить строку на список слов (используйте split() без аргументов).
    cleaned_text = cleaned_text.split()

    # 2. Инициализация словаря для хранения частоты слов.
    word_counts = {}

    # 3. Подсчет частоты слов.
    for word in cleaned_text: 
        if word in word_counts: word_counts[word] += 1 
        else: word_counts[word] = 1

    # 4. Вывод результатов.
    for word, count in word_counts.items(): print(f"{word}: {count}")
    

# Примеры вызова функции для проверки:
print("--- Частота уникальных слов ---")
count_unique_words("Привет, мир! Привет всем!")
print("---")
count_unique_words("Это просто тест. Простой тест.")
print("---")
count_unique_words("Один. Два. Три.")
print("---")
count_unique_words("Мама мыла раму, раму мыла Мама.")
print("---")
count_unique_words("Hello, hello! World world.")