def add_line_numbers(source_filepath, destination_filepath):
    """
    Adds line numbers to each line of a source file and writes them to a destination file.

    Args:
        source_filepath (str): The path to the source file to read from.
        destination_filepath (str): The path to the destination file to write to.

    Returns:
        str: A message indicating success or an error.
    """
    try:
        # Открываем файл назначения для записи ('w') первым
        with open(destination_filepath, 'w', encoding='utf-8') as destination_file:
            # Затем открываем исходный файл для чтения ('r')
            with open(source_filepath, 'r', encoding='utf-8') as source_file:
                line_number = 1  # Инициализируем счетчик строк с 1
                for line in source_file:
                    # Формируем новую строку: номер, двоеточие, пробел, и сама строка.
                    # 'line' уже содержит '\n' в конце, поэтому новая строка тоже будет с '\n'.
                    numbered_line = f"{line_number}: {line}"
                    
                    # Записываем пронумерованную строку в файл назначения
                    destination_file.write(numbered_line)
                    
                    # Увеличиваем счетчик для следующей строки
                    line_number += 1
        
        # Если все прошло успешно, возвращаем сообщение об успехе
        return f"Строки из '{source_filepath}' успешно пронумерованы и сохранены в '{destination_filepath}'."

    except FileNotFoundError:
        # Перехватываем ошибку, если исходный файл не найден
        return f"Ошибка: Исходный файл '{source_filepath}' не найден."
    except Exception as e:
        # Перехватываем любые другие неожиданные ошибки
        return f"Произошла непредвиденная ошибка: {e}"


# --- Примеры использования (тесты) ---

print("--- Начало тестов нумерации строк ---")

# --- Тестовый сценарий 1: Успешная нумерация ---
print("\n--- Тестовый сценарий 1: Успешная нумерация ---")

# 1. Создаем временный исходный файл
source_file_scenario1 = "test_source_numbered_1.txt"
destination_file_scenario1 = "test_numbered_output_1.txt"

with open(source_file_scenario1, "w", encoding='utf-8') as f:
    f.write("Это первая строка.\n")
    f.write("Это вторая строка.\n")
    f.write("\n") # Пустая строка
    f.write("Это четвертая строка.\n")
    f.write("Пятая строка (без переноса в конце).") # Строка без \n в конце
print(f"Исходный файл '{source_file_scenario1}' создан.")

# 2. Вызываем функцию
result_scenario1 = add_line_numbers(source_file_scenario1, destination_file_scenario1)
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


# --- Тестовый сценарий 2: Пустой исходный файл ---
print("\n--- Тестовый сценарий 2: Пустой исходный файл ---")

# 1. Создаем пустой исходный файл
source_file_scenario2 = "test_source_empty.txt"
destination_file_scenario2 = "test_numbered_output_empty.txt"

with open(source_file_scenario2, "w", encoding='utf-8') as f:
    pass # Файл будет создан, но останется пустым
print(f"Исходный файл '{source_file_scenario2}' создан (пустой).")

# 2. Вызываем функцию
result_scenario2 = add_line_numbers(source_file_scenario2, destination_file_scenario2)
print(f"Результат функции: {result_scenario2}")

# 3. Проверяем содержимое файла назначения (ожидаем пустой файл)
print(f"\nСодержимое '{destination_file_scenario2}':")
try:
    with open(destination_file_scenario2, "r", encoding='utf-8') as f:
        content = f.read()
        if not content:
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

# 1. Не создаем исходный файл
non_existent_source_file = "non_existent_source_for_numbering.txt"
destination_file_scenario3 = "test_numbered_output_error.txt"

# 2. Вызываем функцию
result_scenario3 = add_line_numbers(non_existent_source_file, destination_file_scenario3)
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