# Деление чисел с обработкой ZeroDivisionError

try:
    num1 = int(input("Введите числитель: "))
    num2 = int(input("Введите знаменатель: "))
    res_div = num1 / num2
except ZeroDivisionError:
    print("Знаменатель не может быть равен нулю.")
except ValueError: 
    print("Ошибка ввода: Пожалуйста, вводите только целые числа.")
else:
    print(f"Результат равен: {round(res_div, 2)}")

print("Программа завершила работу (если не было фатальных ошибок).")

# Преобразование ввода с обработкой ValueError

try:
    num = int(input("Введите целое число: "))
except ValueError:
    print("Ошибка: Введите, пожалуйста, целое число!")
else:
    print(f"Вы успешно ввели число: {num}")