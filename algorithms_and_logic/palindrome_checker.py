def is_palindrome(text):
    text = text.lower()
    result_text = []

    for char in text:
        if char.isalpha():
            result_text.append(char)
    
    cleaned_text = ''.join(result_text)
    left_index = 0
    right_index = len(cleaned_text) - 1

    while left_index < right_index:
        if cleaned_text[left_index] != cleaned_text[right_index]:
            return False
        else:
            left_index += 1
            right_index -= 1
    return True

print("--- Проверка на палиндром ---")
print(f"'казак': {is_palindrome('казак')}")                                     # Ожидаем: True
print(f"'А роза упала на лапу Азора': {is_palindrome('А роза упала на лапу Азора')}") # Ожидаем: True
print(f"'level': {is_palindrome('level')}")                                     # Ожидаем: True
print(f"'Привет': {is_palindrome('Привет')}")                                 # Ожидаем: False
print(f"'Дед': {is_palindrome('Дед')}")                                       # Ожидаем: True
print(f"'No lemon, no melon': {is_palindrome('No lemon, no melon')}")         # Ожидаем: True
print(f"'' : {is_palindrome('')}")                                            # Ожидаем: True
print(f"'A': {is_palindrome('A')}")                                            # Ожидаем: True
print(f"'racecar': {is_palindrome('racecar')}")                               # Ожидаем: True
print(f"'Was it a car or a cat I saw?': {is_palindrome('Was it a car or a cat I saw?')}") # Ожидаем: True