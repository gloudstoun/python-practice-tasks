def sum_numbers_in_range(start, end):
    sum_numbers = 0
    if start > end:
        start, end = end, start
    
    #return sum(range(start, end + 1))

    total = 0
    for number in range(start, end + 1):
        total += number
    return total

print(sum_numbers_in_range(2, 10))

print(sum_numbers_in_range(10, 2))

