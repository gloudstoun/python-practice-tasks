def is_leap_year(year):
    if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
        return True
    else:
        return False

print("--- Проверка високосных годов ---")
# Выводим сообщение в строке с вызовом print
print(f"2000: {'високосный' if is_leap_year(2000) else 'не високосный'}") # Ожидаем True
print(f"1900: {'високосный' if is_leap_year(1900) else 'не високосный'}") # Ожидаем False
print(f"2004: {'високосный' if is_leap_year(2004) else 'не високосный'}") # Ожидаем True
print(f"2023: {'високосный' if is_leap_year(2023) else 'не високосный'}") # Ожидаем False
print(f"2024: {'високосный' if is_leap_year(2024) else 'не високосный'}") # Ожидаем True
print(f"1600: {'високосный' if is_leap_year(1600) else 'не високосный'}") # Ожидаем True
print(f"2100: {'високосный' if is_leap_year(2100) else 'не високосный'}") # Ожидаем False