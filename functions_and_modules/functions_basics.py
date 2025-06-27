# Функция без параметров и возвращаемого значения
def print_hello_message():
    """ Эта функция просто выводит на экран сообщение -
      "Hello from a function!" """
    print("Hello from a function!")
print_hello_message()

print("\n")
# Функция с параметрами и без возвращаемого значения
def display_info(name, age):
    """ Эта функция использует два параметра и выводит их через f-строку """
    print(f"Меня зовут {name}, мне {age} лет.")
display_info("Евгений", 25)

print("\n")
# Функция с параметрами и возвращаемым значением
def calculate_area(length, width):
    """ Эта функция использует два параметра и возвращает значения """
    area = length * width
    return area
rectangle_area = calculate_area(5, 3)
print(f"Площадь прямоугольника равна: {rectangle_area}")

print("\n")
# Функция со значением параметра по умолчанию
def greet_user(user_name="Гость"):
    """Приветствует указанного пользователя или "Гость" по умолчанию."""
    print(f"Привет, {user_name}!")

greet_user("Евгений")
greet_user()