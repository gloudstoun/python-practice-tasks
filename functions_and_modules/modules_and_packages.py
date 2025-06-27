#modules_and_packages.py
from math_utils import my_calculator
from random import randint # Использую только функцию randint из модуля random
from math_utils.geometry import calculate_circle_area # Импортирую функцию calculate_circle_area из math_utils.geometry

print(f"Сумма чисел равна: {my_calculator.add(5, 6)}")
print(f"Произведение чисел равно: {my_calculator.multiply(8, 8)}")

print(f"Случайное число: {randint(1, 100)}")

print(round(calculate_circle_area(5), 2))
