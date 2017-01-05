'''
Oefententamen A&D
------------------


========
Opgave 1
========
Check of een lijst alleen 
	dezelfde elementen bevat
'''

lijstje = [1,1,1,2,1,1]

def identical_elements(a):
	if len(a) < 2:
		return True
	a.sort()
	return a[0] == a[-1]

def identical_elements2(a): #Dit is de veilige manier
	for i in range(len(a)-1):
		if a[i] != a[i+1]:
			return False
	return True
	
print(identical_elements(lijstje))
print(identical_elements2(lijstje))



'''
========
Opgave 2
========
Check recursief of een lijst 
	alleen dezelfde elementen bevat
'''	
lijstje2 = [1,1,1,1,1]
def rec_identical_elements(a):
	if len(a) < 2:
		return True
	if a[0] != a[1]:
		return False
	return rec_identical_elements(a[1:])

	
print(rec_identical_elements(lijstje2))



'''
========
Opgave 3
========
bevat een ListNode in de lijst 
	een waarde waarbij data == None
'''	


class ListNode:
	def __init__(self,data,next_node):
		self.data = data
		self.next = next_node


def contains_None_data_node(n):
	if not n:
		return False
	if n.data == None:
		return True
	if not n.next:
		return False
	return contains_None_data_node(n.next)
	


'''
========
Opgave 4
========
count x in tree
'''	

class TreeNode:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right


		
def count(n,x):
	result = 0
	if not n:
		return 0
	if n.data == x:
		result+=1
	if n.left:
		result += count(n.left,x)
	if n.right:
		result += count(n.right,x)
	return result
		


'''
========
Opgave 5
========
Ga na of node s tot een cycle behoort.
'''	


def node_in_cyle(G,s):
	temp_list = []
	a = vertices(G)
	b = edges(G)
	for i in range(len(a)):
		for x in range(i,len(b)):
			print(a[i],b[x][1],i,x)
			if a[i] == b[x][1]:
				return True
	return False
	
	










































	