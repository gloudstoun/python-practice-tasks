for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = a**5 + b**5 + c**5 + d**5
                e = int(sum ** (1 / 5))
                if sum == e**5:
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
                    break
