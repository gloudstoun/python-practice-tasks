scores = [42, 77.2323, 13, 99.3232, 44]

def calculate_average_score(result):
    total_sum = sum(result)
    total_len = len(result)
    average_score = total_sum / total_len
    return average_score

num = calculate_average_score(scores)
print(f"Средний бал 5 студентов: {round(num, 1)} ")