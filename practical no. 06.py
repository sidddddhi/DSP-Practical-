import numpy as np


print("=== Creating NumPy Arrays ===")
one_dimensional_array = np.array([1, 2, 3, 4, 5])
print("Array:", one_dimensional_array)


print("\n=== Special Arrays ===")
print("Zeros:\n", np.zeros((2, 2)))
print("Ones:\n", np.ones((3, 3)))
print("Full:\n", np.full((2, 2), 7))
print("Random:\n", np.random.rand(2, 2))


print("\n=== Indexing, Slicing, and Reshaping ===")
array = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
])
print("Element:", array[1, 2])
print("Slice:\n", array[0:2, 1:3])
print("Reshaped:\n", array.reshape(1, 9))


print("\n=== NumPy Calculations ===")
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])
print("Addition:", first_array + second_array)
print("Multiplication:", first_array * second_array)
print("Mean:", np.mean(first_array))
print("Sum:", np.sum(second_array))