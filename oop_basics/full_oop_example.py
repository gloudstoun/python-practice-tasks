import abc

# --- Абстрактный класс Worker (Рабочий) ---
class Worker(abc.ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    @abc.abstractmethod # Декоратор, который делает метод абстрактным
    def perform_daily_task(self):
        pass # Нет тела метода, только заглушка

# --- Класс Employee (Сотрудник), наследуется от абстрактного класса Worker ---
class Employee(Worker):
    def __init__(self, name, position, salary):
        """
        Конструктор для класса Employee.
        :param name: Имя сотрудника (строка).
        :param position: Должность сотрудника (строка).
        :param salary: Зарплата сотрудника (число).
        """
        self.name = name
        self.position = position
        # !!! ИСПРАВЛЕНИЕ: Инициализируем _salary здесь, до вызова сеттера.
        #    Это гарантирует, что _salary всегда существует,
        #    даже если сеттер отклонит начальное значение.
        self._salary = 0
        # Мы НЕ создаем self.salary здесь напрямую.
        # Вместо этого, мы используем наш СЕТТЕР для установки начального значения.
        self.salary = salary # <--- Эта строка вызовет метод @salary.setter (сеттер!)
        self.is_active = True  # Статус активности сотрудника

    def perform_daily_task(self): # Реализация абстрактного метода
        print(f"Сотрудник {self.name} {self.position} выполняет общие обязанности.")

    @property # <--- Этот декоратор превращает метод 'salary' ниже в ГЕТТЕР
    def salary(self):
        """
        Геттер для атрибута 'salary'. Позволяет читать зарплату как emp.salary.
        """
        print(f"--- Вызван ГЕТТЕР для {self.name}'s salary ---") # Отладочное сообщение
        return self._salary # Возвращаем значение из нашего внутреннего, "скрытого" атрибута
    
    @salary.setter # <--- Этот декоратор превращает метод 'salary' ниже в СЕТТЕР
    def salary(self, new_salary):
        """
        Сеттер для атрибута 'salary'. Позволяет устанавливать зарплату как emp.salary = value
        с проверкой на валидность.
        """
        print(f"--- Вызван СЕТТЕР для {self.name}'s salary с значением {new_salary} ---") # Отладочное сообщение
        if new_salary >= 0:
            self._salary = new_salary # Сохраняем значение в наш внутренний атрибут
        else:
            print(f"!!! ОШИБКА: Зарплата ({new_salary}) для {self.name} не может быть отрицательной. Значение не изменено. !!!")
            # Мы могли бы также выбросить ошибку (raise ValueError(...)) вместо print.

    def display_info(self):
        """
        Выводит основную информацию о сотруднике.
        """
        status = "Активен" if self.is_active else "Неактивен"
        # Обратите внимание: здесь мы просто используем self.salary, как обычный атрибут.
        # Но на самом деле вызывается наш ГЕТТЕР @property def salary(self):
        print(f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}. Статус: {status}.")

    def calculate_bonus(self):
        """
        Рассчитывает и выводит базовый бонус для сотрудника (10% от зарплаты).
        :return: Сумма бонуса. Здесь тоже используем self.salary, но вызывается ГЕТТЕР.
        """
        employee_bonus = self.salary * 0.10
        return employee_bonus

# --- Класс Manager (Менеджер), наследуется от Employee ---
class Manager(Employee):
    def __init__(self, name, position, salary, managed_department):
        """
        Конструктор для класса Manager.
        Он ПЕРЕОПРЕДЕЛЯЕТ конструктор родительского класса Employee,
        вызывая его через super() и добавляя новый атрибут 'managed_department'.
        """
        super().__init__(name, position, salary)
        #super().__init__(name, position, salary)  # Вызов конструктора родительского класса
        self.managed_department = managed_department

    def perform_daily_task(self): # Реализация абстрактного метода
        print(f"Сотрудник {self.name} {self.position} организует работу команды.")

    def display_info(self):
        """
        Переопределенный метод display_info для менеджера.
        Выводит основную информацию и информацию об управляемом отделе.
        """
        super().display_info()  # Вызов метода родительского класса
        print(f"Управляет отделом: {self.managed_department}.")

    def assign_task(self, employee_object, task_description):
        """
        Уникальный метод для менеджера, чтобы поручить задачу другому сотруднику.
        :param employee_object: Объект Employee, которому назначается задача.
        :param task_description: Описание задачи (строка).
        """
        # Исправлено: вывод имени менеджера, а не отдела
        print(f"Менеджер по имени {self.name}, из {self.managed_department} поручил(а) {employee_object.name}, {employee_object.position} задачу: '{task_description}'.")

    def calculate_bonus(self):
        """
        Переопределенный метод calculate_bonus для менеджера (20% от зарплаты).
        :return: Сумма бонуса менеджера.
        """
        manager_bonus = self.salary * 0.20
        return manager_bonus

# --- Класс Freelancer (Фрилансер), наследуется от абстрактного класса Worker ---
class Freelancer(Worker):
    def __init__(self, name, position, hourly_rate, hours_worked):
        """
        Конструктор для класса Freelancer.
        :param name: Имя фрилансера (строка).
        :param hourly_rate: Часовая ставка фрилансера (число).
        :param hours_worked: Отработано часов (число).
        """
        super().__init__(name, position)
        self._hourly_rate = 0
        self.hourly_rate = hourly_rate
        self._hours_worked = 0
        self.hours_worked = hours_worked
        self.is_active = True

    @property 
    def hourly_rate(self):
        """
        Геттер для атрибута hourly_rate.
        """
        return self._hourly_rate
    
    @hourly_rate.setter 
    def hourly_rate(self, new_hourly_rate):
        """
        Сеттер для атрибута hourly_rate.
        """
        if isinstance(new_hourly_rate, (int, float)) and new_hourly_rate >= 0:
            self._hourly_rate = new_hourly_rate
        else:
            print("!!! ОШИБКА: Часовая ставка фрилансера должена быть положительным числом. Значение не изменено. !!!")
            return

    @property 
    def hours_worked(self):
        """
        Геттер для атрибута hours_worked.
        """
        return self._hours_worked
    
    @hours_worked.setter 
    def hours_worked(self, new_hours_worked):
        """
        Сеттер для атрибута hours_worked.
        """
        if isinstance(new_hours_worked, (int, float)) and new_hours_worked >=0:
            self._hours_worked = new_hours_worked
        else:
            print("!!! Ошибка: Количество отработанных фрилансером часов должно быть положительным числом. !!!")
            return
        
    def perform_daily_task(self): # Реализация абстрактного метода
        print(f"Фрилансер {self.name} выполняет работу по проекту.")

    @property
    def payment_due(self):
        """Вычисляемое свойство: сумма к оплате."""
        return self.hourly_rate * self.hours_worked
    
    def display_info(self):
        """Выводит информацию о фрилансере."""
        status = "Активен" if self.is_active else "Неактивен"
        print(f"Имя: {self.name}, Должность: {self.position}, Ставка: {self.hourly_rate}/час, Часы: {self.hours_worked}, К оплате: {self.payment_due:.2f}. Статус: {status}.")

    def calculate_bonus(self):
        """
        Расчет "бонуса" для фрилансера (15% от текущей суммы к оплате).
        """
        # Сначала убедимся, что payment_due рассчитана
        current_payment = self.payment_due # Это вызовет геттер payment_due
        freelancer_bonus = current_payment * 0.15
        return freelancer_bonus
    
# --- Класс Company (Компания) ---
class Company:
    def __init__(self, name, initial_budget = 1000000):
        """
        Конструктор для класса Company.
        :param name: Название компании (строка).
        """
        self.current_budget = initial_budget
        self.name = name
        self.employees = []  # Список для хранения объектов Employee и Manager
    
    def hire_employee(self, employee_object):
        """
        Добавляет сотрудника в штат компании.
        :param employee_object: Объект класса Employee или Manager.
        """
        # Проверка на наличие сотрудника по имени (чтобы избежать дубликатов)
        for emp in self.employees:
            if emp.name == employee_object.name:
                print(f"Сотрудник {employee_object.name} уже числится в компании '{self.name}'.")
                return False

        self.employees.append(employee_object)
        print(f"Сотрудник {employee_object.name} принят на работу в '{self.name}'.")
        return True

    def list_all_employees(self):
        """
        Выводит информацию о всех сотрудниках в компании.
        """
        print(f"\n--- Сотрудники в {self.name}: ---")
        if not self.employees:
            print(f"В компании {self.name} пока нет сотрудников.")
        else:
            for employee in self.employees:
                employee.display_info()

    def fire_employee(self, name_to_fire):
        """
        Увольняет сотрудника по имени, меняя его статус на 'Неактивен'.
        :param name_to_fire: Имя сотрудника для увольнения (строка).
        :return: True, если сотрудник уволен; False в противном случае.
        """
        for employee in self.employees:
            if employee.name == name_to_fire:
                if employee.is_active:
                    employee.is_active = False
                    print(f"Сотрудник {employee.name} уволен из {self.name}.")
                    return True
                else:
                    print(f"Сотрудник {employee.name} уже неактивен.")
                    return False
        print(f"Сотрудник с именем {name_to_fire} не найден в компании.")
        return False
    
    def find_employee(self, query):
        """
        Находит сотрудников по части имени или должности (без учета регистра).
        :param query: Строка запроса.
        :return: Список найденных объектов Employee/Manager.
        """
        found_employees = []
        for employee in self.employees:
            if query.lower() in employee.name.lower() or query.lower() in employee.position.lower():
                found_employees.append(employee)
        
        if found_employees:
            print(f"\n--- Найденные сотрудники по запросу '{query}': ---")
            for found_employee in found_employees:
                found_employee.display_info()
            return found_employees
        else:
            print(f"Сотрудники по запросу '{query}' не найдены.")
            return []
        
    def add_funds(self, amount):
        if amount > 0:
            self.current_budget += amount
            print(f"[{self.name}] Добавлено {amount:.2f} в бюджет. Текущий бюджет: {self.current_budget:.2f}")
        else:
            print(f"[{self.name}] Сумма добавления в бюджет должна быть положительной.")

    def deduct_expenses(self, amount, description="неизвестные расходы"):
        if amount <= 0:
            print(f"[{self.name}] Сумма расходов должна быть положительной.")
            return False
        if self.current_budget >= amount:
            self.current_budget -= amount
            print(f"[{self.name}] Успешно вычтено {amount:.2f} за {description}. Текущий бюджет: {self.current_budget:.2f}")
            return True
        else:
            print(f"[{self.name}] Недостаточно средств в бюджете для '{description}'. Требуется: {amount:.2f}, Доступно: {self.current_budget:.2f}")
            return False

    def pay_bonuses(self):
        print(f"\n--- Выплата бонусов в {self.name} ---") # Отладочное сообщение
        total_bonuses_paid = 0 # Переменная для подсчета общей суммы выплаченных бонусов
        for employee in self.employees:
            if employee.is_active:
                bonus_amount = employee.calculate_bonus()
                description = f"бонус для {employee.name} ({employee.position})"
                if self.deduct_expenses(bonus_amount, description):
                    total_bonuses_paid += bonus_amount
                else:   
                    print(f"Не удалось выплатить бонус для {employee.name} из-за недостатка средств.")
            else:
                print(f"Бонус не выплачен для {employee.name} (неактивен).")
        print(f"--- Общая сумма выплаченных бонусов: {total_bonuses_paid:.2f}. Текущий бюджет: {self.current_budget:.2f} ---")
        return total_bonuses_paid

    def pay_salaries(self):
        print(f"\n--- Выплата зарплат в {self.name} ---")
        total_salaries_paid = 0
        for employee in self.employees:
            # Проверяем, является ли работник "традиционным" сотрудником с зарплатой
            if isinstance(employee, Employee) and not isinstance(employee, Freelancer) and employee.is_active:
                salary_amount = employee.salary # Получаем зарплату (геттер)
                description = f"зарплата для {employee.name} ({employee.position})"
                if self.deduct_expenses(salary_amount, description):
                    total_salaries_paid += salary_amount
                else:
                    print(f"Не удалось выплатить зарплату для {employee.name} из-за недостатка средств.")
            elif isinstance(employee, Freelancer) and employee.is_active:
                # Для фрилансеров, возможно, нужна отдельная логика оплаты (например, раз в месяц за все часы)
                # Пока просто пропустим их здесь, но имейте в виду, что их тоже нужно "оплачивать"
                print(f"Фрилансер {employee.name} обрабатывается отдельно для выплат.")
        print(f"--- Общая сумма выплаченных зарплат: {total_salaries_paid:.2f}. Текущий бюджет: {self.current_budget:.2f} ---")
        return total_salaries_paid

    def pay_freelancers(self):
        print(f"\n--- Выплата фрилансерам в {self.name} ---")
        total_freelancer_payments = 0
        for employee in self.employees:
            if isinstance(employee, Freelancer) and employee.is_active:
                payment = employee.payment_due
                description = f"оплата за проект для фрилансера {employee.name}"
                if self.deduct_expenses(payment, description):
                    total_freelancer_payments += payment
                    # После оплаты можно "сбросить" часы фрилансера, если это проектная работа
                    employee.hours_worked = 0 
                    print(f"Часы для фрилансера {employee.name} сброшены на 0 после оплаты.")
                else:
                    print(f"Не удалось оплатить фрилансеру {employee.name} из-за недостатка средств.")
        print(f"--- Общая сумма выплат фрилансерам: {total_freelancer_payments:.2f}. Текущий бюджет: {self.current_budget:.2f} ---")
    
# --- Класс Car (Автомобиль) ---
class Car:
    def __init__(self, make, model, year, license_plate):
        """
        Конструктор для класса Car.
        :param make: Марка автомобиля (строка).
        :param model: Модель автомобиля (строка).
        :param year: Год выпуска (число).
        :param license_plate: Госномер (строка, уникальный идентификатор).
        """
        self._license_plate = "" # Безопасное начальное значение (пустая строка)
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.is_parked = True  # По умолчанию автомобиль припаркован при создании

    @property # <--- Этот декоратор превращает метод 'license_plate' ниже в ГЕТТЕР
    def license_plate(self):
        print(f"--- Вызван ГЕТТЕР для номерных знаков ({self.make} {self.model}) ---") # Отладочное сообщение
        """
        Геттер для атрибута 'license_plate'. Позволяет читать госномер как my_car.license_plate.
        """
        return self._license_plate

    @license_plate.setter
    def license_plate(self, new_license_plate):
        print(f"--- Вызван СЕТТЕР для номерных знаков ({self.make} {self.model}) со значением '{new_license_plate}' ---") # Отладочное сообщение
        """
        Сеттер для атрибута 'license_plate'. Позволяет устанавливать госномер как my_car.license_plate = value
        с проверкой на валидность.
        """
        if not isinstance(new_license_plate, str):
            print(f"!!! ОШИБКА: Госномер ('{new_license_plate}') для {self.make} {self.model} должен быть строкой. Значение не изменено. !!!")
            return # Выходим из сеттера, ничего не меняем
        
        # Если это строка, очищаем от пробелов
        cleaned_plate = new_license_plate.strip()

        if cleaned_plate: # Если строка не пуста (после strip())
            self._license_plate = cleaned_plate 
        else:
            print(f"!!! ОШИБКА: Госномер для {self.make} {self.model} не может быть пустым. Значение не изменено. !!!")

    def display_car_info(self):
        """
        Выводит информацию об автомобиле и его текущем статусе.
        """
        status = "Припаркован" if self.is_parked else "В пути"
        print(f"Марка: {self.make}, Модель: {self.model}, Год: {self.year}, Госномер: {self.license_plate}. Статус: {status}.")

# --- Класс Garage (Гараж) ---
class Garage:
    def __init__(self, name, capacity=2): # Установил capacity по умолчанию
        """
        Конструктор для класса Garage.
        :param name: Название гаража (строка).
        :param capacity: Максимальное количество машин в гараже (число).
        """
        self._capacity = 0
        self.name = name
        self.cars = []  # Список для хранения объектов Car
        self.capacity = capacity

    @property # <--- Этот декоратор превращает метод 'capacity' ниже в ГЕТТЕР
    def capacity(self):
        print(f"--- Вызван ГЕТТЕР для гаража {self.name} ---") # Отладочное сообщение
        """
        Геттер для атрибута 'capacity'
        """
        return self._capacity # Возвращаем значение из нашего внутреннего, "скрытого" атрибута
    
    @capacity.setter
    def capacity(self, new_capacity):
        print(f"--- Вызван СЕТТЕР для гаража '{self.name}' с значением {new_capacity} ---") # Отладочное сообщение
        """
        Сеттер для атрибута 'capacity'
        """
        if new_capacity > 0:
            self._capacity = new_capacity
        else:
            print(f"!!! ОШИБКА: Недопустимое значение мест на парковке ({new_capacity}) для гаража '{self.name}'. Значение не изменено. !!!")

    def add_car(self, car_object):
        """
        Добавляет автомобиль в гараж, если есть место и нет дубликатов госномера.
        :param car_object: Объект класса Car.
        :return: True, если автомобиль добавлен; False в противном случае.
        """
        # Проверка на дубликаты по license_plate
        for car in self.cars:
            if car.license_plate == car_object.license_plate:
                print(f"Ошибка: Автомобиль с госномером {car_object.license_plate} уже существует в гараже '{self.name}'.")
                return False

        # Здесь вызывается ГЕТТЕР self.capacity, чтобы получить актуальную вместимость
        if self._get_parked_count() < self.capacity: 
            self.cars.append(car_object)
            car_object.is_parked = True # <--- Добавлено: Явно устанавливаем статус "припаркован"
            print(f"Автомобиль {car_object.make} {car_object.model} с номером {car_object.license_plate} добавлен в гараж '{self.name}'.")
            return True
        else:
            # Здесь вызывается ГЕТТЕР self.capacity
            print(f"Гараж '{self.name}' полон ({self._get_parked_count()}/{self.capacity} мест). Невозможно добавить автомобиль {car_object.make} {car_object.model}.")
            return False

    def _get_parked_count(self):
        """Вспомогательный метод для подсчета припаркованных машин."""
        count = 0
        for car in self.cars:
            if car.is_parked:
                count += 1
        return count

    def list_all_cars(self):
        """
        Выводит список всех автомобилей в гараже.
        """
        print(f"\n--- Автомобили в гараже '{self.name}': (Припарковано: {self._get_parked_count()}/{self.capacity}) ---")
        if not self.cars:
            print("В гараже пока нет автомобилей.")
        else:
            for car in self.cars:
                car.display_car_info()
    
    def park_car(self, license_plate_to_park):
        """
        Паркует автомобиль по госномеру.
        :param license_plate_to_park: Госномер автомобиля для парковки (строка).
        :return: True, если успешно припаркован; False в противном случае.
        """
        for car in self.cars:
            if car.license_plate == license_plate_to_park:
                if not car.is_parked: # Если НЕ припаркован, то паркуем
                    car.is_parked = True
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} успешно припаркован. Занято мест: {self._get_parked_count()}/{self.capacity}.")
                    return True
                else: # Если уже припаркован
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} уже припаркован в гараже. Занято мест: {self._get_parked_count()}/{self.capacity}.")
                    return False
        # Если цикл завершился, значит, машина с таким номером не найдена
        print(f"Автомобиль с госномером '{license_plate_to_park}' не найден в гараже '{self.name}'.") 
        return False
    
    def unpark_car(self, license_plate_to_unpark):
        """
        Отправляет автомобиль "в путь" (снимает с парковки) по госномеру.
        :param license_plate_to_unpark: Госномер автомобиля для снятия с парковки (строка).
        :return: True, если успешно снят с парковки; False в противном случае.
        """
        for car in self.cars:
            if car.license_plate == license_plate_to_unpark:
                if car.is_parked: # Если припаркован, то снимаем с парковки
                    car.is_parked = False
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} выехал из гаража. Занято мест: {self._get_parked_count()}/{self.capacity}.")
                    return True
                else: # Если уже не припаркован (в пути)
                    print(f"Автомобиль {car.make} {car.model} с номером {car.license_plate} уже не в гараже (в пути). Занято мест: {self._get_parked_count()}/{self.capacity}.")
                    return False
        # Если цикл завершился, значит, машина с таким номером не найдена
        print(f"Автомобиль с госномером '{license_plate_to_unpark}' не найден в гараже '{self.name}'.")
        return False

# =================================
# --- ТЕСТИРОВАНИЕ ВСЕХ КЛАССОВ ---
# =================================

my_company = Company("ООО Хардбасс", initial_budget=500000)

# Создаем объекты Employee и Manager и проверяем через сеттер допустимые значения зарплаты
person1 = Employee("Григорий", "Слесарь", 30000)
person2 = Employee("Максим", "Стажер", 15000)
person3 = Employee("Антон", "Секретарь", 25000)
manager1 = Manager("Ольга", "Старший менеджер", 70000, "Отдел продаж")
person4 = Employee("Сергей", "Продавец", 40000)
manager2 = Manager("Ирина", "Менеджер по кадрам", 60000, "HR Отдел")
freelancer1 = Freelancer("Игорь", "Программист", 50, 233)

print("\n--- Добавляем сотрудников в компанию ---")
my_company.hire_employee(person1)
my_company.hire_employee(person2)
my_company.hire_employee(person3)
my_company.hire_employee(person4)
my_company.hire_employee(manager1)
my_company.hire_employee(manager2)
my_company.hire_employee(freelancer1)

all_staff = [person1, person2, person3, person4, manager1, manager2, freelancer1]

''' ТЕСТИРОВАНИЕ БЮДЖЕТА КОМПАНИИ

# =====================================
# --- ТЕСТИРОВАНИЕ БЮДЖЕТА КОМПАНИИ ---
# =====================================

print("\n" + "="*50)
print("--- ТЕСТИРОВАНИЕ БЮДЖЕТА КОМПАНИИ ---")
print("="*50)

print(f"\nНачальный бюджет компании {my_company.name}: {my_company.current_budget:.2f}")

my_company.pay_salaries() # Выплачиваем зарплаты
my_company.pay_bonuses()  # Выплачиваем бонусы
my_company.pay_freelancers() # Выплачиваем фрилансерам

# Попробуйте добавить средства
my_company.add_funds(200000)

# Попробуйте вызвать расходы, когда денег недостаточно
print("\n--- Попытка вызвать слишком большие расходы ---")
my_company.deduct_expenses(1000000, "Очень большой проект")

print(f"\nКонечный бюджет компании {my_company.name}: {my_company.current_budget:.2f}")

'''


''' ТЕСТИРОВАНИЕ СИСТЕМЫ КОМПАНИЯ-СОТРУДНИКИ 

# ===============================================
# --- ТЕСТИРОВАНИЕ СИСТЕМЫ КОМПАНИЯ-СОТРУДНИКИ ---
# ===============================================
print("="*50)
print("--- ТЕСТИРОВАНИЕ СИСТЕМЫ КОМПАНИЯ-СОТРУДНИКИ ---")
print("="*50)

print("\n--- Пробуем добавить уже существующего сотрудника ---")
my_company.hire_employee(Employee("Григорий", "Инженер", 50000)) # Дубликат по имени

# Выводим информацию о всех сотрудниках
my_company.list_all_employees()

print("\n--- Пробуем уволить существующего, активного сотрудника (Григорий) ---")
my_company.fire_employee("Григорий")

print("\n--- Пробуем уволить существующего, неактивного сотрудника (Григорий) ---")
my_company.fire_employee("Григорий")

print("\n--- Пробуем уволить несуществующего сотрудника (Сюзанна) ---")
my_company.fire_employee("Сюзанна")

print("\n--- Пробуем найти сотрудника по имени (Максим) ---")
my_company.find_employee("максим")

print("\n--- Пробуем найти сотрудника по должности (секретарь) ---")
my_company.find_employee("секретарь")

print("\n--- Пробуем найти сотрудника по части имени/должности (прод) ---")
my_company.find_employee("прод") # Должен найти Сергея (продавец) и Ольгу (Отдел продаж - менеджер)

print("\n--- Пробуем найти несуществующего сотрудника (Саша) ---")
my_company.find_employee("Саша")

print("\n--- Выводим информацию о менеджере и даем задание сотруднику ---")
manager1.display_info()
manager1.assign_task(person4, "Подготовить отчет по продажам за квартал")
manager2.assign_task(person3, "Организовать корпоратив")

print("\n--- Расчет бонусов для всего персонала (демонстрация полиморфизма) ---")
# Создаем список, содержащий как Employee, так и Manager объекты
total_bonus_sum = 0.0 # Используем float для точности

for person in all_staff:
    person.display_info() # Выводим информацию о сотруднике
    # Получаем бонус для текущего сотрудника/менеджера, вызывая его полиморфный метод calculate_bonus()
    current_person_bonus = person.calculate_bonus()
    total_bonus_sum += current_person_bonus # Добавляем этот бонус к общей сумме
    print("-" * 30) # Разделитель для читаемости

print(f"\nОбщая сумма бонусов для всего персонала: {total_bonus_sum:.2f}.") # Форматируем вывод
'''


'''ТЕСТИРОВАНИЕ КЛАССА EMPLOYEE С @property ДЛЯ ЗАРПЛАТЫ 
# =============================================================
# --- ТЕСТИРОВАНИЕ КЛАССА EMPLOYEE С @property ДЛЯ ЗАРПЛАТЫ ---
# =============================================================

print("="*50)
print("--- ТЕСТИРОВАНИЕ КЛАССА EMPLOYEE С @property ДЛЯ ЗАРПЛАТЫ ---")
print("="*50)

# 1. Создаем сотрудника - это вызывает КОНСТРУКТОР __init__
#    Внутри __init__, строка 'self.salary = 60000' ВЫЗОВЕТ СЕТТЕР!
print("--- 1. Создание сотрудника 'Анна' с зарплатой 60000 ---")
anna = Employee("Анна", "Менеджер", 60000)
print(f"Зарплата 'Анны' после создания: {anna.salary}\n") # Это ВЫЗОВЕТ ГЕТТЕР!

# 2. Попытка изменить зарплату на допустимое значение
#    Это ВЫЗОВЕТ СЕТТЕР!
print("--- 2. Попытка изменить зарплату 'Анны' на 65000 ---")
anna.salary = 65000
print(f"Новая зарплата 'Анны': {anna.salary}\n") # Это ВЫЗОВЕТ ГЕТТЕР!

# 3. Попытка изменить зарплату на недопустимое (отрицательное) значение
#    Это ВЫЗОВЕТ СЕТТЕР, но сработает проверка!
print("--- 3. Попытка установить отрицательную зарплату для 'Анны' (-5000) ---")
anna.salary = -5000
print(f"Зарплата 'Анны' после неудачной попытки: {anna.salary}\n") # Это ВЫЗОВЕТ ГЕТТЕР! (должна быть 65000)

# 4. Использование других методов, которые обращаются к salary
#    Здесь тоже будут вызываться ГЕТТЕРЫ!
print("--- 4. Вывод полной информации об 'Анне' (display_info) ---")
anna.display_info()

print("\n--- 5. Расчет бонуса для 'Анны' (calculate_bonus) ---")
anna.calculate_bonus()

# 6. Попробуем создать сотрудника сразу с отрицательной зарплатой
print("\n--- 6. Создание сотрудника 'Иван' с отрицательной зарплатой (-1000) ---")
ivan = Employee("Иван", "Стажер", -1000) # Это ВЫЗОВЕТ СЕТТЕР с проверкой
print(f"Зарплата 'Ивана' после создания: {ivan.salary}\n") # Это ВЫЗОВЕТ ГЕТТЕР! (должна быть 0, если сеттер не дал изменить)
ivan.display_info()
'''


''' ТЕСТИРОВАНИЕ АБСТРАКТНОГО КЛАССА WORKER 
# ===============================================
# --- ТЕСТИРОВАНИЕ АБСТРАКТНОГО КЛАССА WORKER ---
# ===============================================

print("="*50)
print("--- ТЕСТИРОВАНИЕ АБСТРАКТНОГО КЛАССА WORKER ---")
print("="*50)

print("\n--- Попытка создать экземпляр абстрактного класса (вызовет ошибку) ---")
try:
    abstract_worker = Worker("Ваня", "Уборщик")
except TypeError as e:
    print(f"ОШИБКА: {e}")

print("\n--- Применение абстрактного метода для классов Manager и Employee (демонстрация полиморфизма) ---")

for person in all_staff:
    person.perform_daily_task()
'''


'''ТЕСТИРОВАНИЕ СИСТЕМЫ АВТОМОБИЛИ-ГАРАЖ 
# ===============================================
# --- ТЕСТИРОВАНИЕ СИСТЕМЫ АВТОМОБИЛИ-ГАРАЖ ---
# ===============================================
print("\n")
print("="*50)
print("--- ТЕСТИРОВАНИЕ СИСТЕМЫ АВТОМОБИЛИ-ГАРАЖ ---")
print("="*50)

# Создаем объекты Car
auto1 = Car("Киа", "Рио", 2012, "AH2345B")
auto2 = Car("Ниссан", "Жук", 2010, "ОМ2065B")
auto3 = Car("Мицубиши", "Лансер", 2015, "ОД9041А")
auto4 = Car("Лада", "Веста", 2019, "ВХ777КМ") # Будет ждать места

my_garage = Garage("ООО Драйв", capacity=2) # Гараж на 2 машины

print("\n### ТЕСТИРОВАНИЕ КЛАССА CAR С @property ДЛЯ GOSNOMERA ###\n")

# 1. Создаем автомобиль с допустимым госномером
print("--- 1. Создание автомобиля 'Ford Focus' с номером 'K456XY' ---")
my_car_1 = Car("Ford", "Focus", 2018, "K456XY") # Вызовет сеттер
my_car_1.display_car_info() # Вызовет геттер

# 2. Попытка установить пустой госномер
print("\n--- 2. Попытка установить пустой госномер для 'Ford Focus' ---")
my_car_1.license_plate = "   " # Вызовет сеттер, сработает проверка
my_car_1.display_car_info() # Госномер не должен измениться (K456XY)

# 3. Попытка установить госномер, который не является строкой
print("\n--- 3. Попытка установить госномер, который не является строкой (число) ---")
my_car_1.license_plate = 12345 # Вызовет сеттер, сработает проверка
my_car_1.display_car_info() # Госномер не должен измениться (K456XY)

# 4. Установка нового допустимого госномера
print("\n--- 4. Установка нового допустимого госномера 'P789OP' ---")
my_car_1.license_plate = "P789OP" # Вызовет сеттер
my_car_1.display_car_info() # Госномер должен обновиться

print("\n--- Добавляем машины в гараж ---")
my_garage.add_car(auto1) # Добавим
my_garage.add_car(auto2) # Добавим
my_garage.add_car(auto3) # Не влезет
my_garage.add_car(auto4) # Не влезет

print("\n--- Пробуем добавить дубликат по госномеру ---")
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

print("\n--- Пробуем припарковать машину (auto1), которая 'в пути' ---")
my_garage.park_car("AH2345B") # Успешно

print("\n--- Пробуем припарковать ту же машину (auto1), она уже припаркована ---")
my_garage.park_car("AH2345B") # Должна быть уже припаркована

print("\n--- Пробуем припарковать несуществующую машину ---")
my_garage.park_car("НЕ-СУЩ-НОМЕР") # Не найдена

print("\n--- Выводим информацию о всех машинах после park ---")
my_garage.list_all_cars() # auto1 должна быть "Припаркована"

'''