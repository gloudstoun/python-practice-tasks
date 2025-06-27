class Car:
    # Принимает make (марка, строка), model (модель, строка), year (год выпуска, число),
    # license_plate (госномер, строка, уникальный идентификатор).
    def __init__(self, make, model, year, license_plate): 
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.is_parked = True # По умолчанию автомобиль ПРИПАРКОВАН при создании

    def display_car_info(self):
        status = "Припаркован" if self.is_parked else "В пути"
        print(f"Марка: {self.make}, Модель: {self.model}, Год: {self.year}, Госномер: {self.license_plate}. Статус: {status}.")

class Garage:
    # Принимает self и name (название гаража, строка).
    def __init__(self, name):
        self.name = name
        self.cars = []
        self.capacity = 2 # Уменьшил для более легкого тестирования лимита

    # Принимает self и car_object (объект класса Car).
    def add_car(self, car_object):
        # Проверка на дубликаты по license_plate
        for car in self.cars:
            if car.license_plate == car_object.license_plate:
                print(f"Ошибка: Автомобиль с госномером {car_object.license_plate} уже существует в гараже.")
                return False

        if len(self.cars) < self.capacity:
            self.cars.append(car_object)
            print(f"Автомобиль {car_object.make} {car_object.model} с номером {car_object.license_plate} добавлен в гараж '{self.name}'.")
            return True
        else:
            print(f"Гараж '{self.name}' полон. Невозможно добавить автомобиль {car_object.make} {car_object.model}.")
            return False
        
    # Выводит список всех автомобилей в гараже, если они там есть.
    def list_all_cars(self):
        print(f"\n--- Автомобили в гараже '{self.name}': ---")
        if not self.cars:
            print("В гараже пока нет автомобилей.")
        else:
            for car in self.cars:
                car.display_car_info()
    
    # Принимает self и license_plate_to_park (строка, госномер автомобиля для парковки).
    def park_car(self, license_plate_to_park):
        for car in self.cars:
            if car.license_plate == license_plate_to_park: # Нашли машину по госномеру
                if not car.is_parked: # Если она НЕ припаркована (т.е. в пути), то паркуем
                    car.is_parked = True
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} успешно припаркован.")
                    return True
                else: # Если она уже припаркована
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} уже припаркован.")
                    return False
        # Если цикл завершился, значит, машина с таким номером не найдена
        print(f"Автомобиль с госномером {license_plate_to_park} не найден в гараже.") 
        return False
    
    # Аналогичен park_car, но для выезда (снятия с парковки).
    def unpark_car(self, license_plate_to_unpark):
        for car in self.cars:
            if car.license_plate == license_plate_to_unpark: # Нашли машину по госномеру
                if car.is_parked: # Если она припаркована, то снимаем с парковки (отправляем "в путь")
                    car.is_parked = False
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} выехал из гаража.")
                    return True
                else: # Если она уже не припаркована (уже в пути)
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} уже не в гараже (в пути).")
                    return False
        # Если цикл завершился, значит, машина с таким номером не найдена
        print(f"Автомобиль с госномером {license_plate_to_unpark} не найден в гараже.")
        return False

#ТЕСТИРОВАНИЕ
auto1 = Car("Киа", "Рио", 2012, "AH2345B")
auto2 = Car("Ниссан", "Жук", 2010, "ОМ2065B")
auto3 = Car("Мицубиши", "Лансер", 2015, "ОД9041А") # Будет лишней для capacity = 2

my_garage = Garage("ООО Драйв")

print("\n--- Добавляем машины в гараж (вместимость 2) ---")
my_garage.add_car(auto1) # Добавим
my_garage.add_car(auto2) # Добавим
my_garage.add_car(auto3) # Не влезет

print("\n--- Пробуем добавить дубликат (должна быть ошибка) ---")
my_garage.add_car(Car("Тест", "Дубликат", 2020, "AH2345B")) # Дубликат auto1

print("\n--- Выводим информацию о всех машинах в гараже ---")
my_garage.list_all_cars()

print("\n--- Снимаем с парковки существующую припаркованную машину (auto1) ---")
my_garage.unpark_car("AH2345B") # Успешно

print("\n--- Снимаем с парковки ту же машину (auto1), она уже в пути ---")
my_garage.unpark_car("AH2345B") # Должна быть уже не в гараже

print("\n--- Снимаем с парковки несуществующую машину ---")
my_garage.unpark_car("НЕ-СУЩ-НОМЕР") # Не найдена

print("\n--- Выводим информацию о всех машинах после unpark ---")
my_garage.list_all_cars() # auto1 должна быть "В пути"

print("\n--- Пробуем припарковать машину (auto1), которая в пути ---")
my_garage.park_car("AH2345B") # Успешно

print("\n--- Пробуем припарковать ту же машину (auto1), она уже припаркована ---")
my_garage.park_car("AH2345B") # Должна быть уже припаркована

print("\n--- Пробуем припарковать несуществующую машину ---")
my_garage.park_car("НЕ-СУЩ-НОМЕР") # Не найдена

print("\n--- Выводим информацию о всех машинах после park ---")
my_garage.list_all_cars() # auto1 должна быть "Припаркована"