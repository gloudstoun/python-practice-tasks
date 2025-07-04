line_number = int(input())  # значение строки x
column_number = int(input())  # значение столбца y

line_number_move = int(input())  # новое значение строки x
column_number_move = int(input())  # новое значение столбца y


if (line_number + column_number + line_number_move + column_number_move) % 2 == 0:
    print("YES")
else:
    print("NO")
