def convert_from_decimal(number, notation):
    hexadecimal_alph = ["A", "B", "C", "D", "E", "F"]
    result_str, temp_number = "", int(number)

    while temp_number > 0:
        if temp_number % notation < 10:
            result_str += str(temp_number % notation)
        else:
            position = (temp_number % notation) - 10
            result_str += hexadecimal_alph[position]
        temp_number //= notation

    return result_str[::-1]


def convert_to_decimal(number_str, notation):
    hexadecimal_alph = ["A", "B", "C", "D", "E", "F"]
    result_num, temp_number_str = 0, number_str[::-1]

    for i in range(len(temp_number_str)):
        if temp_number_str[i].isdigit():
            result_num += int(temp_number_str[i]) * notation**i
        else:
            position = hexadecimal_alph.index(temp_number_str[i]) + 10
            result_num += position * notation**i

    return result_num


def main():
    choice = input("1-из 10-ной, 2-в 10-ную: ")
    if choice == "1":
        num, base = input("Число: "), int(input("Система: "))
        print(convert_from_decimal(num, base))
    else:
        num, base = input("Число: "), int(input("Система: "))
        print(convert_to_decimal(num, base))


main()
