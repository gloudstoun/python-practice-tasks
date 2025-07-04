# Нахождение серединного числа

num1, num2, num3 = int(input()), int(input()), int(input())

if (num1 < num2 < num3) or (num3 < num2 < num1):  # num2 посередине
    print(num2)
elif (num1 < num3 < num2) or (num2 < num3 < num1):  # num3 посередине
    print(num3)
elif (num2 < num1 < num3) or (num3 < num1 < num2):  # num1 посередине
    print(num1)


a, b, c = int(input()), int(input()), int(input())

if (b - a) * (c - a) < 0:
    print(a)
elif (a - b) * (c - b) < 0:
    print(b)
else:
    print(c)
