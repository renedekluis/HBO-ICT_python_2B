
def faculteit(n):
	if n <= 0:
		return 1
	else:
		return n*faculteit(n-1)



def B(n,k):
	return (faculteit(n)//faculteit(k))//faculteit(n-k)


	
print(B(100,50))

