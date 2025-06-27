# Обратный отсчет
countdown = 5

while countdown != 0:
    print(countdown)
    countdown -= 1
print("Старт!")

print("\n") # Для разделения

# Сумма чисел
total_sum = 0

for num1 in range(1, 11):
    print(num1)
    total_sum += num1
print(f"Общая сумма чисел: {total_sum}")

# Четные числа
for num2 in range(1, 21):
    if num2 % 2:
        continue
    else:
        print(num2)

# Четные и нечетные числа
numbers = [1, 5, 8, 12, 3]
for num in numbers:
    if not num % 2:
        print(f"Число {num} четное.")
    else:
        print(f"Число {num} нечетное")

