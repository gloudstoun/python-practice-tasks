def find_name(name_list, target_name): # name_list (список строк - имен) и target_name (строка - имя, которое нужно найти)
    for find in name_list:
        if find == target_name:
            print(f"Имя {target_name} найдено!")
            return True
    print(f"Имя {target_name} не найдено!")
    return False
        
names = ["Аня", "Борис", "Света", "Дима"] #Список имен для функции

# Ищем имя, которое есть
res1 = find_name(names, "Света") # В качестве атрибутов функции указываем список, в котором будет происходить поиск и искомое имя
print(f"Результат первого поиска: {res1}")
# Ищем имя, которого нет
res2 = find_name(names, "Олег")
print(f"Результат второго поиска: {res2}")

