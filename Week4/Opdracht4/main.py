m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]


def f(n, i = 0):
	global m
	results = 0
	n2=n
	if i >= len(m):
		return 1-n
	while n2-m[i] >=0:
		print(n,m[i])
		n2-=m[i]
		results+=1
	
	return (results+f(n,i+1))
	
	
print("\n\n",f(7))