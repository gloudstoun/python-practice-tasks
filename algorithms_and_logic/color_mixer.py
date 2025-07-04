color_1, color_2 = str(input()), str(input())
color_list = ["красный", "синий", "желтый"]

if color_1 in color_list and color_2 in color_list:
    if color_1 == color_2:
        print(color_1)

    elif (color_1 == "красный" and color_2 == "синий") or (
        color_1 == "синий" and color_2 == "красный"
    ):
        print("фиолетовый")

    elif (color_1 == "красный" and color_2 == "желтый") or (
        color_1 == "желтый" and color_2 == "красный"
    ):
        print("оранжевый")

    elif (color_1 == "синий" and color_2 == "желтый") or (
        color_1 == "желтый" and color_2 == "синий"
    ):
        print("зеленый")

else:
    print("ошибка цвета")
