a1, b1 = int(input()), int(input())  # начало и конец первого отрезка
a2, b2 = int(input()), int(input())  # начало и конец второго отрезка

max_value = max(a1, a2)  # максимальная функция
min_value = min(b1, b2)  # минимальная функция

if min_value > max_value:
    print(max_value, min_value)
elif min_value == max_value:
    print(min_value)
else:
    print("пустое множество")
