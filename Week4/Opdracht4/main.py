

m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]

t = []	

def fill_m(n,m):
	"""
	This function creates a two dimentional table
	
	Parameters
	----------
	n: integer 
		value to pay
	m: integer
		coin values
	
	
	Example:
	--------
	
	>>> fill_m(4,4)
	[
	[1,	1,		1,		1		],
	[1,	None,	None,	None	],
	[1,	None,	None,	None	],
	[1,	None,	None,	None	]	
	]	
	"""
	for i in range(len(t),n+2):
		t.append([])
		for x in m:
			t[i].append(None)
		t[i][0] = 1
	t[0] = [1]*len(m)
	

	
def f(n, x = len(m)-1):
	"""
	This function fills a table with the number of ways to pay
		a given value
	
	Parameters
	----------
	
	n: integer 
		value to pay
	
	Returns:
	--------
	t[n][x] : integer
		number of ways the value can be payed
	
	Example:
	--------
	>>> B(19)
	>>> 34	
	"""
	global m

	fill_m(n,m)

	if n < 0 or x < 0:
		return 0
	
	elif n == 0:
		return 1
		
	elif t[n][x]:
		return t[n][x]	
		
	elif n >= m[x]:
		t[n][x] = f(n,x-1)+f(n-m[x],x)
		return t[n][x]
		
	return f(n,x-1)

	

for i in range(900):
	print(f(i))
	










