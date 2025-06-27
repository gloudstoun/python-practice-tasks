import abc # Импортируем модуль abc

# Класс Vehicle - абстрактный базовый класс
class Vehicle(abc.ABC): # Наследуемся от abc.ABC или используем @abc.ABC
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        """Обычный (конкретный) метод - имеет реализацию."""
        print(f"The {self.make} {self.model} is moving.")

    @abc.abstractmethod # Декоратор, который делает метод абстрактным
    def start_engine(self):
        """
        Абстрактный метод - не имеет реализации.
        Должен быть реализован в дочерних классах.
        """
        pass # Нет тела метода, только заглушка

# --- КОНКРЕТНЫЕ КЛАССЫ, НАСЛЕДУЮЩИЕСЯ ОТ Vehicle ---

class Car(Vehicle): # Car ОБЯЗАН реализовать start_engine()
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def start_engine(self): # Реализация абстрактного метода
        print(f"The {self.make} {self.model} car engine starts with a key.")

    def honk(self): # Дополнительный метод, специфичный для Car
        print("Beep beep!")

class Motorcycle(Vehicle): # Motorcycle ОБЯЗАН реализовать start_engine()
    def __init__(self, make, model, engine_size_cc):
        super().__init__(make, model)
        self.engine_size_cc = engine_size_cc

    def start_engine(self): # Реализация абстрактного метода
        print(f"The {self.make} {self.model} motorcycle engine roars to life.")

    def wheelie(self): # Дополнительный метод, специфичный для Motorcycle
        print("Doing a wheelie!")

# --- ТЕСТИРОВАНИЕ ---
print("--- Создание и использование конкретных классов ---")
my_car = Car("Toyota", "Camry", 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Fat Boy", 1800)

my_car.start_engine()
my_car.move()
my_car.honk()

my_motorcycle.start_engine()
my_motorcycle.move()
my_motorcycle.wheelie()

print("\n--- Попытка создать экземпляр абстрактного класса (вызовет ошибку) ---")
try:
    abstract_vehicle = Vehicle("Generic", "Vehicle")
except TypeError as e:
    print(f"ОШИБКА: {e}")

print("\n--- Попытка создать класс, который НЕ реализовал абстрактный метод (вызовет ошибку при создании объекта) ---")
class IncompleteCar(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    # Здесь нет реализации start_engine()

try:
    incomplete_car_obj = IncompleteCar("Broken", "Car")
except TypeError as e:
    print(f"ОШИБКА: {e}")