# Stack Implementation

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

# Pop operation
stack.pop()
print("After pop:", stack)

# Peek
print("Top element:", stack[-1])


# Infix to Postfix (Simple)


def precedence(operator):
	if operator in "+-":
		return 1
	if operator in "*/":
		return 2
	return 0


def infix_to_postfix(expression):
	operators = []
	result = []

	for character in expression:
		if character.isalnum():
			result.append(character)
		elif character == "(":
			operators.append(character)
		elif character == ")":
			while operators and operators[-1] != "(":
				result.append(operators.pop())
			if operators:
				operators.pop()
		else:
			while (operators
				   and operators[-1] != "("
				   and precedence(operators[-1]) >= precedence(character)):
				result.append(operators.pop())
			operators.append(character)

	while operators:
		result.append(operators.pop())

	return "".join(result)


expression = "A+B*C"
print("Postfix:", infix_to_postfix(expression))


