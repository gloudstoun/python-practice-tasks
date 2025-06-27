def check_number(number):
    if number == 0:
        print("Число равно нулю.")
    elif number > 0: # Если число не 0, и оно больше 0 (значит, положительное)
        if number % 2 == 0:
            print(f"Число {number} положительное и четное.")
        else: # Если положительное, но не четное, значит нечетное
            print(f"Число {number} положительное и нечетное.")
    else: # Если число не 0 и не больше 0 (значит, отрицательное)
        if number % 2 == 0:
            print(f"Число {number} отрицательное и четное.")
        else: # Если отрицательное, но не четное, значит нечетное
            print(f"Число {number} отрицательное и нечетное.")

# Ваш тестовый код остаётся таким же
print("--- Проверка чисел ---")
check_number(4)
check_number(7)
check_number(-2)
check_number(-5)
check_number(0)
check_number(100)
check_number(-99)