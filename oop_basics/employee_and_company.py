class Employee:

    def __init__(self, name, position, salary): # name (строка, имя сотрудника), position (строка, должность), salary (число, зарплата)
        self.name = name
        self.position = position
        self.salary = salary
        self.is_active = True

    def display_info(self):
        status = "Активен" if self.is_active else "Неактивен"
        print(f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}. Статус: {status}.")

    def calculate_bonus(self):
        employee_bonus = self.salary * 0.10
        print(f"Базовый бонус для {self.name}: {employee_bonus}.")
        return employee_bonus

class Company:

    def __init__(self, name): # name (строка, название компании)
        self.name = name
        self.employees = [] # список self.employees = [] для хранения объектов Employee
    
    def hire_employee(self, employee_object): # принимает self и employee_object (объект класса Employee)
        self.employees.append(employee_object)
        print(f"Сотрудник {employee_object.name} принят на работу в '{self.name}'.")

    def list_all_employees(self):
        print(f"\n--- Сотрудники в {self.name}: ---")
        if not self.employees:
            print(f"В компании {self.name} пока нет сотрудников")
        else:
            for employee in self.employees:
                employee.display_info()

    def fire_employee(self, name_to_fire): # employee_name (строка, имя сотрудника для увольнения)
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
    
    def find_employee(self, query): # query (строка - может быть частью имени или должности)
        found_employees = []
        for employee in self.employees:
            if query.lower() in employee.name.lower() or query.lower() in employee.position.lower():
                found_employees.append(employee)
        if found_employees:
            print("\n--- Найденные сотрудники: ---")
            for found_employee in found_employees:
                found_employee.display_info()
            return found_employees
        else:
            print(f"Сотрудники по запросу '{query}' не найдены.")
            return []

class Manager(Employee):

    def __init__(self, name, position, salary, managed_department): # managed_department (строка, название отдела, которым управляет менеджер)
        super().__init__(name, position, salary)
        self.managed_department = managed_department
    
    def display_info(self): # Переопределенный метод из родительского класса Employee.
        super().display_info()
        print(f"Управляет отделом: {self.managed_department}.")

    def assign_task(self, employee_object, task_description):
        '''
        Это уникальный метод для менеджера.
        Принимает self, employee_object (объект Employee, которому назначается задача), 
        task_description (строка, описание задачи).
        '''
        print(f"Менеджер по имени {self.name}, из {self.managed_department} поручил(а) {employee_object.name}, {employee_object.position} задачу: '{task_description}'.")

    def calculate_bonus(self):
        manager_bonus = self.salary * 0.20
        print(f"Бонус менеджера для {self.name}: {manager_bonus}.")
        return manager_bonus

#ДОБАВЛЕНИЕ ОБЪЕКТОВ
my_company = Company("ООО Хардбасс")
person1 = Employee("Григорий", "Слесарь", 30000)
person2 = Employee("Максим", "Стажер", 15000)
person3 = Employee("Антон", "Секретарь", 25000)
manager1 = Manager("Ольга", "Старший менеджер", 70000, "Отдел продаж")
person4 = Employee("Сергей", "Продавец", 40000)

print("\n--- Пробуем добавить сотрудника в компанию ---")
my_company.hire_employee(person1)
my_company.hire_employee(person2)
my_company.hire_employee(person3)
my_company.hire_employee(person4)
my_company.hire_employee(manager1)

#ПРОВЕРКИ РАБОТЫ МЕТОДОВ
my_company.list_all_employees()

print("\n--- Пробуем уволить существующего, активного сотрудника ---")
my_company.fire_employee("Григорий")

print("\n--- Пробуем уволить существующего, неактивного сотрудника ---")
my_company.fire_employee("Григорий")

print("\n--- Пробуем уволить несуществующего сотрудника ---")
my_company.fire_employee("Сюзанна")

print("\n--- Пробуем найти сотрудника по имени ---")
my_company.find_employee("максим")
my_company.find_employee("Антон")
my_company.find_employee("ГригорИй")

print("\n--- Пробуем найти сотрудника по должности ---")
my_company.find_employee("секретарь")
my_company.find_employee("Стажер")
my_company.find_employee("СлЕсаРь")

print("\n--- Пробуем найти сотрудника по части имени/должности ---")
my_company.find_employee("секрет")
my_company.find_employee("Стаж")
my_company.find_employee("Григ")

print("\n--- Пробуем найти несуществующего сотрудника ---")
my_company.find_employee("Саша")

print("\n--- Пробуем вывести информацию о менеджере и дать задание сотруднику ---")
manager1.display_info()
manager1.assign_task(person4, "Подготовить отчет по продажам за квартал")

print("\n--- Расчет бонусов для всего персонала ---")
all_staff = [person1, person2, person3, person4, manager1]
total_bonus_sum = 0
for person in all_staff:
    person.display_info() # Выводим информацию о сотруднике
    # Получаем бонус для текущего сотрудника/менеджера, вызывая его полиморфный метод calculate_bonus()
    current_person_bonus = person.calculate_bonus() # ЭТО И ЕСТЬ ПРИМЕР ПОЛИМОРФИЗМА
    total_bonus_sum += current_person_bonus # Добавляем этот бонус к общей сумме
    print("-" * 30)

print(f"\nОбщая сумма бонусов для всего персонала: {total_bonus_sum}.")
