class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        # Мы НЕ создаем self._salary здесь напрямую.
        # Вместо этого, мы вызываем сеттер через 'self.salary = salary'.
        # Это вызовет метод @salary.setter
        self.salary = salary # <--- Эта строка вызовет наш сеттер!
        self.is_active = True

    @property # <--- Это декоратор, превращающий метод в геттер
    def salary(self):
        """Геттер для зарплаты."""
        print("Вызван геттер salary.") # Для демонстрации
        return self._salary # Возвращаем значение из "приватного" атрибута

    @salary.setter # <--- Это декоратор, превращающий метод в сеттер для свойства 'salary'
    def salary(self, new_salary):
        """Сеттер для зарплаты с валидацией."""
        print(f"Вызван сеттер salary с значением {new_salary}.") # Для демонстрации
        if new_salary >= 0:
            self._salary = new_salary # Присваиваем значение внутреннему атрибуту
        else:
            print(f"Ошибка: Зарплата ({new_salary}) не может быть отрицательной!")
            # Можно выбросить ошибку или оставить значение без изменений
            # В данном случае, оставим старое значение.

    # Остальные методы (display_info, calculate_bonus) остаются без изменений
    def display_info(self):
        status = "Активен" if self.is_active else "Неактивен"
        # Обратите внимание, здесь мы обращаемся к 'self.salary' как к атрибуту!
        print(f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}. Статус: {status}.")

    def calculate_bonus(self):
        # Здесь тоже обращаемся к 'self.salary' как к атрибуту!
        employee_bonus = self.salary * 0.10
        print(f"Базовый бонус для {self.name}: {employee_bonus:.2f}.")
        return employee_bonus

# --- ТЕСТИРОВАНИЕ с @property ---
print("\n--- Тестирование Employee с @property для salary ---")

emp1 = Employee("Алиса", "Разработчик", 60000) # Вызовет сеттер при инициализации
emp1.display_info()
print(f"Прямой доступ к зарплате (через геттер): {emp1.salary}") # Вызовет геттер

print("\n--- Попытка изменить зарплату на допустимое значение ---")
emp1.salary = 65000 # Вызовет сеттер
emp1.display_info()

print("\n--- Попытка изменить зарплату на недопустимое значение ---")
emp1.salary = -5000 # Вызовет сеттер, сработает валидация
emp1.display_info() # Зарплата не изменилась
print(f"Текущая зарплата после неудачной попытки: {emp1.salary}") # Вызовет геттер