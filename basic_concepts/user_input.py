#Первый блок задания с цветом

fav_color = input("Введите ваш любимый цвет (не используйте цифры и числа): ")
fav_color_str = str(fav_color) #Для избежания ошибки, но по-хорошему тут уже нужно использовать условие.
print(f"Ваш любимый цвет - {fav_color_str}.")

#Второй блок задания с числами

num_a = input("Введите первое число: ")
num_a_int = int(num_a)
print(f"Тип переменной 'num_a': {type(num_a_int)}") # Проверка первого числа

num_b = input("Введите второе число: ")
num_b_int = int(num_b)
print(f"Тип переменной 'num_b': {type(num_b_int)}") # Проверка второго числа

total_sum = num_a_int + num_b_int

print(f"Сумма введенных чисел = {total_sum}.")

