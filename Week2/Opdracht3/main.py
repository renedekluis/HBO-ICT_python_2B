from myStack import myStack


def check(value):
	"""
	This function checks if the list of brackets are correct

	Parameters
	----------
	value : list
		list of brackets
		
	Return
	------
	message : string
		if the list is correct the fuction returns "correct"
		
		if the list has invalid values the function returns an error
			including the first found invalid value
		
		if the list has invalid bracket usage, 
			the function will return the open brackets on the stack

	Example
	-------
	>>> #value = ['(',')']
	>>> return = "Correct"

	"""
	brackets = { ')' : '(', '>' : '<', ']' : '['}
	stack = myStack()
	for i in value:
		if i in brackets.values():
			stack.push(i)
		elif i in brackets.keys():
			# if brackets[i] != stack.pop():
				# return False
			for x in brackets.keys():
				if i == x:
					stack.pop()

		else:
			print("ERROR: '%s' not accepted" % i)
			return False

	if stack.isEmpty():
		return True
	else:
		print(stack.show())
		return str(stack.show())

# test 1
haakjes = ['<', '(', ')','>']
result = check(haakjes)
print(result)


# test 2
haakjes = ['<', '(', 'a','>']
result = check(haakjes)
print(result)

# test 3
haakjes = ['<', '(', '(','>']
result = check(haakjes)
print(result)



