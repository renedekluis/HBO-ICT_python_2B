
t = [[1]]

def B(n,k):
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
			t[n][k] = B(n-1,k-1) + B(n-1,k)
			return t[n][k]
		else:
			return t[n][k]
	else:
		
		temp = [None] * (len(t)+1)
		temp[0] = 1
		temp[-1] = 1
		t.append(temp)
		return B(n,k)

		
print(B(5,2))







