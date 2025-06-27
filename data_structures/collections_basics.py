# Создание и распаковка кортежа
my_point = (10, 25, 14)
coord_x = my_point[0]
coord_y = my_point[1]
coord_z = my_point[2]
# my_point[0] = 5 Ошибка: 'tuple' object does not support item assignment
print(f"x-координата: {coord_x}, y-координата: {coord_y}, z-координата: {coord_z}" )

# Создание и манипуляция словарем
print("\n")
book_info = {
"название": "«Преступление и наказание»",
"автор": "Фёдор Достоевский",
"год": "1866"
}
print(f"Название вашей любимой книги - {book_info.get('название')}, имя автора - {book_info.get('автор')}.") # Безопасный способ получить значение через метод ".get"
book_info["жанр"] = "Роман"
book_info["год"] = "1888"
print(book_info)

# Итерация по словарю
print("\n")
for key in book_info:
    print(key)

print("\n")
for value in book_info.values():
    print(value)

print("\n")
for key, value in book_info.items():
    print(f"{key}, {value}")