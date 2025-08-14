current_alphabet_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
current_alphabet_ru = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"


def encryptor_decryptor(text, language, key, mode):

    text = list(text)
    if mode == "encryptor":
        modifier = 1
    else:
        modifier = -1

    if language.lower() == "en":

        for char in range(len(text)):
            if text[char].isalpha():
                try:
                    if text[char].isupper():
                        new_idx = (
                            current_alphabet_en.index(text[char]) + key * modifier
                        ) % 26
                        text[char] = current_alphabet_en[new_idx]
                    else:
                        new_idx = (
                            current_alphabet_en.index(text[char]) + key * modifier
                        ) % 26
                        text[char] = current_alphabet_en[new_idx + 26]
                except ValueError:
                    pass

        return "".join(text)

    elif language.lower() == "ru":

        for char in range(len(text)):
            if text[char].isalpha():
                try:
                    if text[char].isupper():
                        new_idx = (
                            current_alphabet_ru.index(text[char]) + key * modifier
                        ) % 32
                        text[char] = current_alphabet_ru[new_idx]
                    else:
                        new_idx = (
                            current_alphabet_ru.index(text[char]) + key * modifier
                        ) % 32
                        text[char] = current_alphabet_ru[new_idx + 32]
                except ValueError:
                    pass

        return "".join(text)


def main():
    print("Добро пожаловать в программу Шифр Цезаря!")
    mode, language, count = "", "", 0

    while True:
        if count > 0:
            user_choice = input("Желаете ввести новое сообщение? (да/нет): ")
            if user_choice.lower() == "да":
                pass
            elif user_choice.lower() == "нет":
                print("Спасибо, что воспользовались приложением. Еще увидимся!")
                break
            else:
                print("Ошибка. Введите корректный ответ.")
                continue
        count += 1

        while True:
            user_choice = input(
                "Желаете зашифровать или дешифровать собщение? (зашифровать - 'з'/дешифровать - 'д'): "
            )
            if user_choice.lower() == "з":
                mode = "encryptor"
                break
            elif user_choice.lower() == "д":
                mode = "decryptor"
                break
            else:
                print("Ошибка. Введите корректный ответ.")

        while True:
            user_choice = input(
                "Укажите язык исходного текста. (русский - 'р'/английский - 'а'): "
            )
            if user_choice.lower() == "а":
                language = "en"
                break
            elif user_choice.lower() == "р":
                language = "ru"
                break
            else:
                print("Ошибка. Введите корректный ответ.")

        while True:
            try:
                user_key = int(
                    input("Введите ROT(сдвиг) для шифровки/дешифровки сообщения: ")
                )
                if language.lower() == "en":
                    if 0 <= user_key <= 25:
                        break
                    print("Введите целое число в диапазоне от 0 до 25(включительно).")
                    continue
                elif language.lower() == "ru":
                    if 0 <= user_key <= 31:
                        break
                    print("Введите целое число в диапазоне от 0 до 31(включительно).")
                    continue
            except ValueError:
                print("Ошибка. Введено недопустимое значение, введите целое число.")
                continue

        user_text = input("Введите Ваше сообщение: ")

        if mode == "encryptor":
            print(
                f"Сообщение успешно зашифровано, результат: {encryptor_decryptor(user_text, language, user_key, mode)}"
            )
        else:
            print(
                f"Сообщение успешно дешифровано, результат: {encryptor_decryptor(user_text, language, user_key, mode)}"
            )


main()
