def print_even_indexed_elements(items):
    for i in range(len(items)):
        if i % 2 == 0:
            print(items[i])

print("--- Элементы на четных индексах ---")
print_even_indexed_elements(["a", "b", "c", "d", "e"])
print("---") 
print_even_indexed_elements([10, 20, 30, 40])
print("---")
print_even_indexed_elements(["Hello"])
print("---")
print_even_indexed_elements([])
print("---")
print_even_indexed_elements([1, 2, 3, 4, 5, 6])
print("---")
print_even_indexed_elements(["first", "second", "third", "fourth"])