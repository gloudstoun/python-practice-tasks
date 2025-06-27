print("\n")
# Создание и добавление

my_hobbies = []
while len(my_hobbies) <=2: # С помощью цикла немного автоматизировал задачу, ограничил список до 3 элементов
    user_hobbies = input("Введите свое хобби: ") 
    my_hobbies.append(user_hobbies) # Присваиваю каждый элемент введенный пользователем в список

print(f"Все ваши хобби: {my_hobbies}")

print("\n")
# Доступ и изменение

planets = ["Меркурий", "Венера", "Земля", "Марс", "Юпитер"]
print(f"Наша планета: {planets[2]}.")
planets[3] = "Красная планета"
print(planets)

print("\n")
#Перебор и сортировка

random_numbers = [42, 7, 13, 99, 5]
for num in random_numbers:
    print(num * 2)
random_numbers.sort()
print(random_numbers)
