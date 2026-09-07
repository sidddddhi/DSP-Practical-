print("=== List Operations ===")

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers[2] = 35
print("Updated list:", numbers)

numbers.append(60)
numbers.insert(1, 15)
print("After insertion:", numbers)

numbers.remove(40)
del numbers[0]
print("After deletion:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

numbers.sort()
print("Sorted list:", numbers)
