import random


def get_word():
    word_list = (
        "программирование",
        "фотография",
        "путешествие",
        "приключение",
        "археология",
        "астрономия",
        "философия",
        "психология",
        "архитектура",
        "изобретение",
        "эксперимент",
        "исследование",
        "творчество",
        "воображение",
        "вдохновение",
    )
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                    """,
        # голова, торс, обе руки, одна нога
        """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                    """,
        # голова, торс, обе руки
        """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
                    """,
        # голова, торс и одна рука
        """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                    """,
        # голова и торс
        """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                    """,
        # голова
        """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                    """,
        # начальное состояние
        """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                    """,
    ]
    return stages[tries]


def game(word):
    word_completion = ["_" for i in range(len(word))]  # список, содержащая символы _ на каждую букву задуманного слова
    tries = 6  # количество попыто
    guessed_letters, guessed_words = [], []  # списки уже названных букв и слов

    while tries != 0 and "".join(word_completion) != word:
        print(display_hangman(tries))
        print(*word_completion, f"Слово состоит из {len(word)} букв.")

        user_try = input("Угадайте букву или слово: ").upper()

        if not user_try.isalpha():
            print("Ошибка. Ответ не является буквой или словом, повторите попытку.")
            continue

        if len(user_try) == 1:
            if user_try in guessed_letters:
                if user_try not in word:
                    print(f"Вы уже пытались букву {user_try}.")
                else:
                    print(f"Вы уже угадали букву {user_try}.")
            else:
                guessed_letters.append(user_try)
                if user_try in word:
                    print(f"Вы угадали букву {user_try}!")

                    for char in range(len(word)):
                        if word[char] == user_try:
                            word_completion[char] = user_try
                else:
                    print(f"Буквы {user_try} в слове нет.")
                    tries -= 1

        elif len(user_try) == len(word):
            if user_try in guessed_words:
                print(f"Вы уже пытались угадать слово - {user_try}.")
            else:
                if user_try == word:
                    for char in range(len(word_completion)):
                        word_completion[char] = user_try[char]
                else:
                    print(f"Неверно, было загадано другое слово.")
                    guessed_words.append(user_try)
                    tries -= 1
        else:
            print("Ошибка. Введите букву или целое слово.")

    print("---" * 10)

    if "".join(word_completion) == word:
        print(f"Вы победили! Загаданное слово - {word}")
    else:
        print(display_hangman(tries))
        print(f"Вы проиграли. Загаданное слово - {word}.")


def play_game():
    game_counter = 0

    while True:
        if game_counter == 0:
            print("Давайте играть в угадайку слов!")
            print("---" * 10)

        elif game_counter > 0:

            user_answer = input("Желаете сыграть снова (да/нет)? ")

            if user_answer.upper() == "ДА":
                pass
            elif user_answer.upper() == "НЕТ":
                print(f"Было сыграно игр: {game_counter}. До скорой встречи!")
                break
            else:
                print("Ошибка. Введите корректный ответ.")
                continue

        game(get_word())

        game_counter += 1


play_game()
