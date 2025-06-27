
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    pass

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Файл не найден."
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"
    pass
    


# --- Примеры для проверки ---
test_filename = "my_test_file.txt"
test_content = "Это тестовый файл.\nОн содержит несколько строк.\nТретья строка."
non_existent_file = "non_existent.txt"

print("--- Работа с файлами ---")

# Проверка записи
print(f"Запись в файл '{test_filename}'...")
write_to_file(test_filename, test_content)
print("Запись завершена.")

# Проверка чтения существующего файла
print(f"\nЧтение из файла '{test_filename}':")
content_read = read_from_file(test_filename)
print(content_read)

# Проверка чтения несуществующего файла
print(f"\nЧтение из файла '{non_existent_file}':")
content_read_non_existent = read_from_file(non_existent_file)
print(content_read_non_existent) # Ожидаем: Файл не найден.

# Запишем что-то новое, чтобы показать перезапись
print(f"\nПерезапись файла '{test_filename}'...")
write_to_file(test_filename, "Новое содержимое файла.")
print("Перезапись завершена.")

# Проверим, что содержимое изменилось
print(f"\nЧтение из файла '{test_filename}' после перезаписи:")
content_re_read = read_from_file(test_filename)
print(content_re_read)
