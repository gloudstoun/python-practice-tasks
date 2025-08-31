numbers = [38, 27, 43, 10, 3, 9, 82, 11]

for i in range(len(numbers)):
    swapped = False
    for j in range(1, len(numbers) - i):
        if numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            swapped = True

    if not swapped:
        break

print(f"Sorted array(Bubble sort): {numbers}")

print("-" * 70)

numbers = [38, 27, 43, 10, 3, 9, 82, 11]

for i in range(len(numbers)):
    min_idx = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j

    if min_idx != i:
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print(f"Sorted array(Selection sort): {numbers}")

print("-" * 70)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left or right)
    return merged


my_array = [38, 27, 43, 10, 3, 9, 82, 11]
sorted_array = merge_sort(my_array)
print(f"Sorted array(Merge sort): {sorted_array}")
