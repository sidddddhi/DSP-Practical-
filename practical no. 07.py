def linear_search(values, target):
	for index, value in enumerate(values):
		if value == target:
			return index
	return -1


print("=== Program 1: Linear Search ===")
values = [10, 25, 30, 45, 60]
target = 30
result = linear_search(values, target)
if result != -1:
	print("Element found at index:", result)
else:
	print("Element not found")


def binary_search(values, target):
	low = 0
	high = len(values) - 1

	while low <= high:
		middle = (low + high) // 2
		if values[middle] == target:
			return middle
		if values[middle] < target:
			low = middle + 1
		else:
			high = middle - 1
	return -1


print("\n=== Program 2: Binary Search ===")
sorted_values = [10, 20, 30, 40, 50]
target = 40
result = binary_search(sorted_values, target)
if result != -1:
	print("Element found at index:", result)
else:
	print("Element not found")