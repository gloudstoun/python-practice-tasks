import math

a, b, c = float(input()), float(input()), float(input())
discriminant = math.pow(b, 2) - 4 * a * c

if discriminant < 0:
    print("Нет корней")
elif discriminant == 0:
    print(-b / (2 * a))
elif discriminant > 0:
    square_root1 = (-b - math.sqrt(discriminant)) / (2 * a)
    square_root2 = (-b + math.sqrt(discriminant)) / (2 * a)
    if square_root1 > square_root2:
        print(square_root2)
        print(square_root1)
    else:
        print(square_root1)
        print(square_root2)
