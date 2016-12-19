

def B(n,k):
	if n == 0 or k ==0:
		return 1
	else:
		return (n * B(n-1,1)),(k * B(1,k-1))


	
print(B(100,50))

'''
Maak de functie B(n,k) die (n!//(k!))//(n-k)! berekent.
(n!//(k!))//(n-k)!:
floor((floor(n faculteit/k faculteit))/n-k faculteit)
Doe dit op basis van dynamic programming.
Wat is B(100,50) ?
'''
