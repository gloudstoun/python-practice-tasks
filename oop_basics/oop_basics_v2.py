class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def say_hello(self):
        print(f"Привет меня зовут - {self.name}, и мне {self.age} лет(года).") 

person1 = Human("Анна", 31)
person2 = Human("Борис", 25)
person1.age = 32
person2.age = 28

print(f"Имя: {person1.name}, возраст: {person1.age}")
print(f"Имя: {person2.name}, возраст: {person2.age}")
person1.say_hello()
person2.say_hello()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return (2 * (self.width + self.height))
    
    def display_info(self):
        print(f"Прямоугольник: Ширина = {self.width}, Высота = {self.height}, Площадь = {self.calculate_area()}, Периметр = {self.calculate_perimeter()}.")

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3.5, 7.2)
rect1.display_info()
rect2.display_info()
