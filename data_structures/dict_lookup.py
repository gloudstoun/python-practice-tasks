def lookup_contact(phone_book, search_name):
    if not phone_book:
        return f"Поиск значения '{search_name}' не удался. Словарь пуст."
    return phone_book.get(search_name, "Контакт не найден")

my_book = {"Анна": "111-2233", "Виктор": "555-1212", "Галина": "777-8899"}

print("--- Поиск контактов ---")
print(f"Поиск 'Анна': {lookup_contact(my_book, 'Анна')}")
print(f"Поиск 'Виктор': {lookup_contact(my_book, 'Виктор')}")
print(f"Поиск 'Борис': {lookup_contact(my_book, 'Борис')}")
print(f"Поиск 'Максим': {lookup_contact(my_book, 'Максим')}")
print(f"Поиск в пустом словаре 'Тест': {lookup_contact({}, 'Тест')}")