import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_started = False

    def display_info(self):
        print(f"Это машина бренда: {self.brand}, модель: {self.model}, год выпуска: {self.year}")

    def get_age(self):
        current_year = datetime.date.today().year
        cars_age = current_year - self.year
        return cars_age 
    
    def start_engine(self):
        if self.is_started:
            print("Двигатьель уже заведен.")
        else:
            self.is_started = True
            print(f"Двигатель заведен. {self.brand} {self.model} готова к поездке.")

    def stop_engine(self):
        if not self.is_started:
            print("Двигатель уже заглушен.")
        else:
            self.is_started = False
            print("Двигатель заглушен.")



car1 = Car("Toyota", "Camry", 2011)
car2 = Car("Honda", "Civic", 2015)
car3 = Car("Ford", "Focus", 2018)


car1.display_info()
car2.display_info()
car3.display_info()

car2_age = car2.get_age()
print(f"Возраст {car2.brand} {car2.model}: {car2_age} лет.")

print("\n--- Тестирование car1 ---")
car1.start_engine()
car1.start_engine() # Повторный вызов
car1.stop_engine()
car1.stop_engine()  # Повторный вызов