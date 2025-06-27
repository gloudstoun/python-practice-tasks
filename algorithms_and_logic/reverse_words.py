def reverse_words(text):
  
  words = text.split()  
  reversed_text = ""
  for word in words:
    reversed_text = word + " " + reversed_text  
  return reversed_text.strip()  

# Примеры вызова функции для проверки:
print("--- Обратный порядок слов ---")
print(f"'Hello world': '{reverse_words('Hello world')}'")             # Ожидаем: 'world Hello'
print(f"'Python is fun': '{reverse_words('Python is fun')}'")         # Ожидаем: 'fun is Python'
print(f"'one': '{reverse_words('one')}'")                             # Ожидаем: 'one'
print(f"Пустая строка: '{reverse_words('')}'")                        # Ожидаем: ''
print(f"Строка из пробелов: '{reverse_words('    ')}'")               # Ожидаем: ''
print(f"'Single word example': '{reverse_words('Single word example')}'") # Ожидаем: 'example word Single'