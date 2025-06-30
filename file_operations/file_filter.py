# file_filter.py

def filter_lines_by_keyword(source_filepath, destination_filepath, keyword):
    '''
    Reads a text file and writes to a new file only those lines that contain a specific keyword (case-insensitive).

    Args:
        source_filepath (str): The path to the source file for reading.
        destination_filepath (str): The path to the destination file for writing filtered lines.
        keyword (str): The keyword to filter lines by.

    Returns:
        str: A message indicating success or an error.
    '''
    try:
        # Открываем файл назначения ОДИН РАЗ, в режиме записи ('w')
        # Это также гарантирует, что файл назначения будет очищен или создан.
        with open(destination_filepath, 'w', encoding='utf-8') as destination_file:
            # Открываем исходный файл для чтения
            with open(source_filepath, 'r', encoding='utf-8') as source_file:
                # Итерируем по строкам исходного файла
                for line in source_file:
                    # Проверяем, содержит ли строка ключевое слово (без учета регистра)
                    if keyword.lower() in line.lower():
                        # Если условие выполнено, записываем эту строку в destination_file
                        # 'line' уже содержит символ переноса строки '\n' в конце.
                        destination_file.write(line)
        
        # После того как оба файла обработаны и закрыты (благодаря 'with'),
        # можно вернуть сообщение об успехе.
        return f"Строки, содержащие '{keyword}', успешно отфильтрованы в '{destination_filepath}'."

    except FileNotFoundError:
        # Перехватываем ошибку, если исходный файл не найден
        return f"Ошибка: Исходный файл '{source_filepath}' не найден."
    except Exception as e:
        # Перехватываем любые другие неожиданные ошибки
        return f"Произошла непредвиденная ошибка: {e}"


# --- Примеры использования (тесты) ---

print("--- Начало тестов фильтрации файлов ---")

# --- Тестовый сценарий 1: Успешная фильтрация ---
print("\n--- Тестовый сценарий 1: Успешная фильтрация ---")

# 1. Создаем временный исходный файл
source_file_scenario1 = "test_source_1.txt"
destination_file_scenario1 = "test_filtered_1.txt"
keyword_scenario1 = "python"

with open(source_file_scenario1, "w", encoding='utf-8') as f:
    f.write("This line talks about Python.\n")
    f.write("Java is also a programming language.\n")
    f.write("Learning PYTHON is fun.\n")
    f.write("Another line without keywords.\n")
    f.write("Python is very versatile.")
print(f"Исходный файл '{source_file_scenario1}' создан.")

# 2. Вызываем функцию
result_scenario1 = filter_lines_by_keyword(source_file_scenario1, destination_file_scenario1, keyword_scenario1)
print(f"Результат функции: {result_scenario1}")

# 3. Проверяем содержимое файла назначения
print(f"\nСодержимое '{destination_file_scenario1}':")
try:
    with open(destination_file_scenario1, "r", encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print(f"Ошибка: Файл '{destination_file_scenario1}' не был создан.")
except Exception as e:
    print(f"Произошла ошибка при чтении '{destination_file_scenario1}': {e}")

print("-" * 30) # Разделитель


# --- Тестовый сценарий 2: Ключевое слово не найдено ни в одной строке ---
print("\n--- Тестовый сценарий 2: Ключевое слово не найдено ---")

# 1. Создаем временный исходный файл (можно использовать тот же, что и в сценарии 1)
source_file_scenario2 = "test_source_2.txt"
destination_file_scenario2 = "test_filtered_2.txt"
keyword_scenario2 = "nonexistentword" # Ключевое слово, которого нет

with open(source_file_scenario2, "w", encoding='utf-8') as f:
    f.write("Hello world.\n")
    f.write("This is a test.\n")
    f.write("No keywords here.")
print(f"Исходный файл '{source_file_scenario2}' создан.")

# 2. Вызываем функцию
result_scenario2 = filter_lines_by_keyword(source_file_scenario2, destination_file_scenario2, keyword_scenario2)
print(f"Результат функции: {result_scenario2}")

# 3. Проверяем содержимое файла назначения (ожидаем пустой файл)
print(f"\nСодержимое '{destination_file_scenario2}':")
try:
    with open(destination_file_scenario2, "r", encoding='utf-8') as f:
        content = f.read()
        if not content: # Проверяем, пуст ли файл
            print("(Файл пуст, как и ожидалось.)")
        else:
            print(f"Неожиданное содержимое:\n{content}")
except FileNotFoundError:
    print(f"Ошибка: Файл '{destination_file_scenario2}' не был создан.")
except Exception as e:
    print(f"Произошла ошибка при чтении '{destination_file_scenario2}': {e}")

print("-" * 30) # Разделитель


# --- Тестовый сценарий 3: Исходный файл не существует ---
print("\n--- Тестовый сценарий 3: Исходный файл не существует ---")

# 1. Не создаем исходный файл, чтобы вызвать FileNotFoundError
non_existent_source_file = "non_existent_source.txt"
destination_file_scenario3 = "test_filtered_3_error.txt"
keyword_scenario3 = "anyword"

# 2. Вызываем функцию
result_scenario3 = filter_lines_by_keyword(non_existent_source_file, destination_file_scenario3, keyword_scenario3)
print(f"Результат функции: {result_scenario3}")

# 3. Проверяем, что файл назначения НЕ был создан
print(f"\nПопытка прочитать '{destination_file_scenario3}' (ожидаем FileNotFoundError):")
try:
    with open(destination_file_scenario3, "r", encoding='utf-8') as f:
        print(f"Неожиданное содержимое:\n{f.read()}")
except FileNotFoundError:
    print(f"Файл '{destination_file_scenario3}' не был создан, как и ожидалось.")
except Exception as e:
    print(f"Произошла ошибка при чтении '{destination_file_scenario3}': {e}")

print("-" * 30) # Разделитель