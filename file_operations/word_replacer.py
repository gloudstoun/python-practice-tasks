import re

def replace_word_in_file(filepath, old_word, new_word):
    """
    Replaces all occurrences of an old word with a new word in a specified file (case-insensitive).
    Заменяет все вхождения старого слова на новое слово в указанном файле (без учета регистра).

    Args:
        filepath (str): The path to the file.
        old_word (str): The word to be replaced.
        new_word (str): The new word to replace with.

    Returns:
        str: A message indicating success or an error.
    """
    try:
        # Read the entire content of the file
        # Читаем все содержимое файла
        with open(filepath, "r", encoding='utf-8') as file:
            file_content = file.read()

        # Perform the replacement using regular expressions for case-insensitive match
        # re.escape(old_word) handles special characters in old_word
        # Выполняем замену с использованием регулярных выражений для поиска без учета регистра
        # re.escape(old_word) обрабатывает специальные символы в old_word
        
        # Используем re.subn() вместо re.sub(), чтобы получить количество произведенных замен
        # re.subn() возвращает кортеж (новая_строка, количество_замен)
        modified_content, num_replacements = re.subn(re.escape(old_word), new_word, file_content, flags=re.IGNORECASE)

        # Check if any replacements actually occurred
        # Проверяем, были ли произведены какие-либо замены
        if num_replacements > 0:
            # Write the modified content back to the file (overwriting it)
            # Записываем измененное содержимое обратно в файл (перезаписывая его)
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            return "Замена выполнена успешно."
        else:
            return "Слово для замены не найдено."

    except FileNotFoundError:
        return f"Ошибка: Файл '{filepath}' не найден."
    except Exception as e:
        return f"Произошла ошибка при работе с файлом: {e}"
    
# Create a dummy test file
# Создаем фиктивный тестовый файл
test_file_name = "replace_test.txt"
initial_content = (
    "This is a test file.\n"
    "We will test word replacement here.\n"
    "Test, test, test!"
)
# Каждый раз создаем файл с оригинальным содержимым перед тестами
with open(test_file_name, "w", encoding='utf-8') as f:
    f.write(initial_content)
print(f"Тестовый файл '{test_file_name}' создан с исходным содержимым:\n{initial_content}\n")


print("--- Замена слова в файле ---")

# Test case 1: Replace existing word (case-insensitive)
# Тестовый случай 1: Замена существующего слова (без учета регистра)
result = replace_word_in_file(test_file_name, "test", "demo")
print(f"Результат замены: {result}")

# Verify the content after replacement
# Проверяем содержимое после замены
print(f"\nСодержимое '{test_file_name}' после замены:")
with open(test_file_name, "r", encoding='utf-8') as f:
    print(f.read())
# Expected content:
# This is a demo file.
# We will demo word replacement here.
# demo, demo, demo!


# Reset the file content for the next test case
# Сбрасываем содержимое файла для следующего тестового случая,
# чтобы гарантировать независимость тестов
with open(test_file_name, "w", encoding='utf-8') as f:
    f.write(initial_content)
print("\n--- Файл сброшен до исходного состояния для следующего теста ---")


# Test case 2: Replace a word that does not exist
# Тестовый случай 2: Замена слова, которого нет в файле
result_no_change = replace_word_in_file(test_file_name, "nonexistent", "newword")
print(f"\nРезультат попытки замены несуществующего слова: {result_no_change}") # Ожидаем: "Слово для замены не найдено."

# Test case 3: Non-existent file
# Тестовый случай 3: Несуществующий файл
error_msg = replace_word_in_file("non_existent_file.txt", "word", "new_word")
print(f"Попытка замены в несуществующем файле: {error_msg}") # Ожидаем: "Ошибка: Файл 'non_existent_file.txt' не найден."