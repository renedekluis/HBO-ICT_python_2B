


def find_duplicate_hash():
	"""
	This function searches for two values 
			what have the same hashvalue.
	
	Return
	------
	value : integer
		value with a duplicate hash value.
	
	Example
	-------
	>>>find_duplicate_hash()
	>>>0.53726837

	"""
	value = 0
	hashList = {}
	while value < 1:
		try:
			hashList[hash(value)]
			return repr(value)
		except:
			print(repr({hash(value):value}))
			hashList.update({hash(value):value})
			value += 0.00000001
	
print(find_duplicate_hash())


















