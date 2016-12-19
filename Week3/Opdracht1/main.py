


def check(a,i): # ga na of i aan a toegevoegd kan worden
	n = len(a)
	return not (i in a or
		# niet in dezelfde kolom
		i+n in [a[j]+j for j in range(n)] or
		# niet op dezelfde diagonaal
		i-n in [a[j]-j for j in range(n)])
		# niet op dezelfde diagonaal

		
def printQueens(a):
	n = len(a)
	for i in range(n):
		for j in range(n):
			if a[i] == j:
				print("X",end= " ")
			else:
				print("*",end= " ")
		print()
	print()


		
def rsearch2(N, possibilities = None, possibility_list = None, list_of_all_possibilities = None):
	"""
	This function checks all possible outcomes for the queen problem.

	Parameters
	----------
	N : integer
		Number of rows and koloms.

	possibilities : integer
		Number of possibilities.

	possibility_list : list of lists
		A possible outcome is saved in this list.

	list_of_all_possibilities : list
		All possible outcomes.

		
	Return
	------
	This function returns two values:

	possibilities : integer
		Number of all possibilities

	list_of_all_possibilities : list of lists
		List of lists with all the possible outcomes.

	Example
	-------
	>>> N = 2
	>>> return = 2 , [[1,3,0,2],[2,0,3,1]]

	"""
	if possibilities is None:
		possibilities = 0
	if possibility_list is None:
		possibility_list = []
	if list_of_all_possibilities is None:
		list_of_all_possibilities = []
		
		
	for i in range(N):
		if check(possibility_list,i):
			possibility_list.append(i)	
			if len(possibility_list) == N:
				possibilities+=1					# oplossing erbij
				if possibility_list not in list_of_all_possibilities:
					list_of_all_possibilities.append(list(possibility_list)) # geschikte a gevonden
			else:
				possibilities, list_of_all_possibilities = rsearch2(N, possibilities, possibility_list, list_of_all_possibilities)
			del possibility_list[-1]	# verwijder laatste element	

	return possibilities, list_of_all_possibilities



x, y = rsearch2(8)
print(x)
print(y)

