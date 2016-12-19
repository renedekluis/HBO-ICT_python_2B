


#Wat returnt de volgende funcite? --> 11
def func(a):
	if not a:
		return 0
	p = a.pop()
	print(p , a , a)
	return p + func(a.copy()) + func(a.copy())


b = [1,2,3]	
print(func(b))