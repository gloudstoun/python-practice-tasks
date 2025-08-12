from random import randint


def game():

    while True:
        try:
            n = int(input("Введите число 'n': "))
            if n >= 1:
                break
            print("Введите целое число больше нуля.")
        except ValueError:
            print("Ошибка. Введено недопустимое значение, введите целое число:")
            continue

    num_rand, retry_counter = randint(1, n), 0

    while True:

        try:
            num_user = int(input(f"Введите предполагаемое число: "))
            if not 1 <= num_user <= n:
                print(f"А может быть все-таки введем целое число от 1 до {n}?")
                continue
        except ValueError:
            print(f"А может быть все-таки введем целое число от 1 до {n}?")
            continue

        retry_counter += 1

        if num_user > num_rand:
            print("Ваше число больше загаданного, попробуйте еще разок.")
            continue
        elif num_user < num_rand:
            print("Ваше число меньше загаданного, попробуйте еще разок.")
            continue
        else:
            print("Вы угадали, поздравляем!")
            print(f"Вы смогли угадать число с {retry_counter} попыток.")
            break


def start_game():
    print("Добро пожаловать в числовую 'угадайку'. Попробуйте угадать число от 1 до n.")
    game()

    while True:
        answer = input("Желаете сыграть снова? 'д' - да/'н' - нет:")
        if answer.lower() == "д":
            game()
        elif answer.lower() == "н":
            break
        else:
            print("Ошибка. Введено недопустимое значение, попробуйте снова.")


start_game()
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
