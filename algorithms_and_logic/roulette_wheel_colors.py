number = int(input())

if number in range(0, 37):
    if number == 0:
        print("зеленый")
    elif number in range(1, 11):
        if number % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif number in range(11, 19):
        if number % 2 == 0:
            print("красный")
        else:
            print("черный")
    elif number in range(19, 29):
        if number % 2 == 0:
            print("черный")
        else:
            print("красный")
    elif number in range(29, 37):
        if number % 2 == 0:
            print("красный")
        else:
            print("черный")

else:
    print("ошибка ввода")
