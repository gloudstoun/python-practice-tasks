import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"


def get_yes_no_input(prompt):
    answer = prompt.lower()

    while True:
        answer = input(prompt).lower()
        if answer == "да":
            return True
        elif answer == "нет":
            return False
        else:
            print("Ошибка. Введено недопустимое значение, попробуйте снова.")


def generate_password(chars, length):
    return "".join(random.choice(chars) for _ in range(length))


def password_configuration():
    print("Вас приветствует генератор безопасных паролей!")
    print("-" * 50)

    while True:
        try:
            amount = int(input("Введите кол-во паролей, которое нужно сгенерировать: "))
            if amount >= 1:
                break
            print("Введите целое число больше нуля.")
        except ValueError:
            print("Ошибка. Введено недопустимое значение, введите целое число.")
            continue

    while True:
        try:
            length = int(input("Введите желаемую длину пароля(паролей): "))
            if 8 <= length <= 60:
                break
            print("Длина пароля должна быть в пределах от 8 до 60 символов.")
        except ValueError:
            print("Ошибка. Введено недопустимое значение, введите целое число.")
            continue

    chars = ""
    if get_yes_no_input("Включать ли цифры? (да/нет): "):
        chars += digits
    if get_yes_no_input("Включать ли прописные буквы? (да/нет): "):
        chars += uppercase_letters
    if get_yes_no_input("Включать ли строчные буквы? (да/нет): "):
        chars += lowercase_letters
    if get_yes_no_input("Включать ли символы? (да/нет): "):
        chars += punctuation
    if get_yes_no_input("Исключать ли неоднозначные символы? (да/нет): "):
        ambiguous_chars = "il1LoO0"
        for char in ambiguous_chars:
            chars = chars.replace(char, "")

    if not chars:
        print("Ошибка. Вы не выбрали ни один набор символов.")
        return

    print("-" * 50)

    for i in range(1, amount + 1):
        print(f"Пароль №{i}: {generate_password(chars, length)}")


password_configuration()
