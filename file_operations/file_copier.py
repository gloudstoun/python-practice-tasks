def copy_file_content(source_filepath, destination_filepath):
    '''
    Copies the content of one text file to another text file.
    Копирует содержимое одного текстового файла в другой текстовый файл.

    '''

    try:
        # Open the source file for reading
        with open(source_filepath, 'r', encoding='utf-8') as source_file:
            content = source_file.read()
            print("\n--- Содержимое файла (read()) ---")
            return content
    
        # Open the destination file for writing and write the content
        with open(destination_filepath, "w", encoding='utf-8') as destination_file:
            destination_file.write(content)
    
    except FileNotFoundError:
        return f"Ошибка: Один из файлов не найден. Проверьте пути: '{source_filepath}' или '{destination_filepath}'."
    except Exception as e:
        return f"Произошла ошибка при копировании файла: {e}"

# --- Примеры для проверки (Testing Examples) ---

# 1. Create a dummy source file for testing
# 1. Создаем фиктивный исходный файл для тестирования
source_test_filename = "source.txt"
test_content = "This is the first line.\nIt contains multiple lines for testing.\nThird line of test data."

try:
    with open(source_test_filename, "w", encoding='utf-8') as f:
        f.write(test_content)
    print(f"Тестовый файл '{source_test_filename}' создан.")
except Exception as e:
    print(f"Ошибка при создании тестового файла: {e}")

# 2. Define the destination filename
# 2. Определяем имя файла назначения
destination_test_filename = "destination.txt"

# 3. Call the function to copy the content
# 3. Вызываем функцию для копирования содержимого
copy_result = copy_file_content(source_test_filename, destination_test_filename)
print(copy_result)

# 4. Verify the content of the destination file
# 4. Проверяем содержимое файла назначения
print("\n--- Проверка содержимого 'destination.txt' ---")
try:
    with open(destination_test_filename, "r", encoding='utf-8') as f:
        copied_content = f.read()
        print(f"Содержимое 'destination.txt':\n{copied_content}")
    # Compare with original content to verify
    # Сравниваем с оригинальным содержимым для проверки
    if copied_content == test_content:
        print("\nСодержимое успешно скопировано и совпадает!")
    else:
        print("ВНИМАНИЕ: Скопированное содержимое не совпадает с оригиналом.")
except FileNotFoundError:
    print(f"Ошибка: Файл '{destination_test_filename}' не найден для проверки.")
except Exception as e:
    print(f"Ошибка при чтении файла '{destination_test_filename}' для проверки: {e}")

# Example with non-existent source file to test error handling
# Пример с несуществующим исходным файлом для проверки обработки ошибок
print("\n--- Проверка обработки ошибок (несуществующий файл) ---")
error_result = copy_file_content("non_existent_source.txt", "dummy_dest.txt")
print(error_result)
