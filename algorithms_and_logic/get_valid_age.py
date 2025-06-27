def get_valid_age():
    while True:
        try:
            user_age_str = input("Введите ваш возраст: ")
            user_age_int = int(user_age_str)
        except ValueError:
            print("Возраст не может содержать буквы, символы или НЕ целые числа!")
            continue
        else:
            if user_age_int < 0 or user_age_int > 120: # Возраст меньше 0 или больше 120 (условный максимум)
                print("Недопустимое значение возраста. Пожалуйста, введите корректный возраст!")
                continue
            else:
                return user_age_int
            
user_true_age = get_valid_age()
print(f"Ваш возраст: {user_true_age} лет(года).")