largest1, largest2 = 0, 0

for _ in range(int(input())):
    num_user = int(input())
    if largest1 < num_user:
        largest2, largest1 = largest1, num_user
    elif largest2 < num_user:
        largest2 = num_user
print(largest1, largest2, sep="\n")
