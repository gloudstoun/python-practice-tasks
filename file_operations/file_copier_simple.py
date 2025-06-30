def copy_file_content(source_filepath, destination_filepath):
    try:

        with open(source_filepath, 'r', encoding='utf-8') as source_file:
            file_content = source_file.read()

        with open(destination_filepath, 'w', encoding='utf-8') as destination_file:
            destination_file.write(file_content)

        return f"Файл успешно скопирован."
    
    except FileNotFoundError:
        return f"Ошибка: Исходный файл '{source_filepath}' не найден."
    except Exception as e:
        return f"Произошла непредвиденная ошибка: {e}"
    

# --- Примеры для проверки работы функции (Testing Examples) ---

# Создаем фиктивный исходный файл, который будем копировать
source_test_file = "original_text.txt"
with open(source_test_file, "w", encoding='utf-8') as f:
    f.write("This is the original content.\n")
    f.write("It should be copied exactly.\n")
    f.write("Last line of original.")
print(f"Исходный файл '{source_test_file}' создан.\n")

print("--- Начало тестов копирования файлов ---")

# --- Тестовый случай 1: Успешное копирование ---
destination_test_file = "copied_text.txt"
copy_result = copy_file_content(source_test_file, destination_test_file)
print(f"Результат копирования (Успешное): {copy_result}")

print(f"\nСодержимое '{destination_test_file}' после копирования:")
try:
    with open(destination_test_file, "r", encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("Файл назначения не был создан или найден после копирования.")
except Exception as e:
    print(f"Ошибка при чтении файла назначения: {e}")

print("-" * 30) # Разделитель для лучшей читаемости вывода


# --- Тестовый случай 2: Исходный файл не найден ---
non_existent_source = "no_such_file.txt" # Этого файла нет
destination_for_error = "error_output.txt" # Этот файл не будет создан, так как исходный не найден
error_result = copy_file_content(non_existent_source, destination_for_error)
print(f"Результат копирования (Исходный файл не найден): {error_result}")

print("-" * 30) # Разделитель

# P.S. Обратите внимание, файл 'error_output.txt' не должен быть создан, 
# так как операция чтения из 'no_such_file.txt' прервется до попытки записи.
