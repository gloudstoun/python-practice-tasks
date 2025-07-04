num1, num2 = int(input()), int(input())
symbol = str(input())
symbol_case = ["+", "-", "*", "/"]
try:
    if symbol not in symbol_case:
        print("Неверная операция")
    elif symbol == symbol_case[0]:
        print(num1 + num2)
    elif symbol == symbol_case[1]:
        print(num1 - num2)
    elif symbol == symbol_case[2]:
        print(num1 * num2)
    elif symbol == symbol_case[3]:
        print(num1 / num2)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
