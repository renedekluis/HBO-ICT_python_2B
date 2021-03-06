
t = [[1]]

def b(n,k):
	"""
	This function creates the piramid of pascal
	
	Parameters
	----------
	
	n: integer 
		used as vertical indexer
	k: integer
		used as horizontal indexer
	
	Returns:
	--------
	t[n][k] : integer
		result of the calculation (n!//(k!))//(n-k)!
	
	Example:
	--------
	
	>>> B(7,3)
	>>> 35	
	"""
	if k > n or k < 0 or n < 0:
		print("ValueError: Given value not accepted.")
		return 0
	
	if k==0 or k==n:
		return 1
		
	if len(t) > n:
		if t[n][k] == None:
			t[n][k] = b(n-1,k-1) + b(n-1,k)

	else:
		temp = [None]*(len(t)+1)
		temp[0] = 1
		temp[-1] = 1
		t.append(temp)
		b(n,k)
	
	return t[n][k]
		
print(b(5,2))