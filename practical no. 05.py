import math
from functools import reduce


print("=== Math Module ===")
number = 16
print("Square root:", math.sqrt(number))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))


print("\n=== Reduce Function ===")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda first, second: first + second, numbers)
print("Sum using reduce:", total)


print("\n=== User-Defined Functions ===")


def add(first, second):
	return first + second


def multiply(first, second):
	return first * second


print("Addition:", add(5, 3))
print("Multiplication:", multiply(4, 2))