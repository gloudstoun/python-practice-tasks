def count_char_frequency(text):

    text = text.lower()
    cleaned_chars = []

    for char in text: 
        if char.isalnum(): cleaned_chars.append(char)

    cleaned_text = "".join(cleaned_chars)
    char_counts = {}

    for char in cleaned_text: 
        if char in char_counts: char_counts[char] += 1 
        else: char_counts[char] = 1

    for char, count in char_counts.items(): print(f"{char}: {count}")

print("--- Частота символов ---")
count_char_frequency("Hello World!")
print("---")
count_char_frequency("А роза упала на лапу Азора.")
print("---")
count_char_frequency("Python 3.10")
print("---")
count_char_frequency("")
print("---")
count_char_frequency("Мама мыла раму.")
print("---")
count_char_frequency("123abcABC")