def count_lines_in_file(filepath):
    """
    Counts the number of lines in a file using readlines().
    Подсчитывает количество строк в файле, используя readlines().

    Args:
        filename: Имя файла.

    Returns:
        Number of lines in the file.
        Количество строк в файле.
    """

    try:
        with open(filepath, "r", encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"Ошибка: Файл не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"
    

# Create a dummy test file with known lines
# Создаем фиктивный тестовый файл с известным количеством строк
test_file_name = "test_lines.txt"
with open(test_file_name, "w", encoding='utf-8') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4") # No newline at the end of the last line

# Test case 1: Existing file
# Тестовый случай 1: Существующий файл
line_count = count_lines_in_file(test_file_name)
print(f"Number of lines in '{test_file_name}': {line_count}") # Expected: 4

# Test case 2: Non-existent file
# Тестовый случай 2: Несуществующий файл
non_existent_file = "non_existent.txt"
error_message = count_lines_in_file(non_existent_file)
print(f"Number of lines in '{non_existent_file}': {error_message}") # Expected: "Файл не найден."
        
