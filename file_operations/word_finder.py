def find_word_in_file(filepath, search_word):
    """
    Finds a given word in a text file and returns the line numbers where it appears.
    Ищет заданное слово в текстовом файле и возвращает номера строк, в которых оно встречается.

    Args:
        filepath (str): Path to the source file.
        search_word (str): The word to search for.

    Returns:
        list: A list of line numbers where the word was found.
              Returns an empty list if the word is not found.
              Returns a string error message if the file is not found or other error occurs.
    """

    result_lines = []
    # Convert search_word to lowercase once for case-insensitive search
    # Преобразуем искомое слово в нижний регистр один раз для поиска без учета регистра
    search_word_lower = search_word.lower()

    try:
        with open(filepath, "r", encoding='utf-8') as file:
            for line_number, line_content in enumerate(file, 1):
                if search_word in line_content.lower():
                    result_lines.append(line_number)
            return result_lines
        
    except FileNotFoundError:
        return f"Ошибка: Файл '{filepath}' не найден."
    except Exception as e:
        return f"Произошла ошибка при чтении файла: {e}"
    
# Create a dummy test file
# Создаем фиктивный тестовый файл
test_file_name = "sample_text.txt"
test_content = (
    "This is the first line.\n"
    "Python is a great programming language.\n"
    "Hello Python world.\n"
    "python is versatile.\n"
    "End of file."
)
with open(test_file_name, "w", encoding='utf-8') as f:
    f.write(test_content)

print("--- Поиск слова в файле ---")

# Test case 1: Word found (case-insensitive)
# Тестовый случай 1: Слово найдено (без учета регистра)
lines_found = find_word_in_file(test_file_name, "python")
print(f"Слово 'python' найдено в строках: {lines_found}") # Ожидаем: [2, 3, 4]

# Test case 2: Word not found
# Тестовый случай 2: Слово не найдено
lines_found_no_match = find_word_in_file(test_file_name, "java")
print(f"Слово 'java' найдено в строках: {lines_found_no_match}") # Ожидаем: []

# Test case 3: Non-existent file
# Тестовый случай 3: Несуществующий файл
error_msg = find_word_in_file("non_existent_file.txt", "any_word")
print(f"Поиск в несуществующем файле: {error_msg}") # Ожидаем: "Файл не найден."