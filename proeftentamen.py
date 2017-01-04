

'''
Oefententamen A&D
------------------


========
Opgave 1
========
Check of een lijst alleen 
	dezelfde elementen bevat
'''
a=[1,1,1]
b=[1,2,1]


def all_equal():
	if len(a) < 1:
		return True
	a.sort()
	return a[0]==a[-1]
	

#print(all_equal())




'''
========
Opgave 2
========
Check recursief of een lijst 
	alleen dezelfde elementen bevat
'''	
def rec_all_equal(a):
	if len(a)<=1:
		return True
	if a[0] == a[1]:
		return rec_all_equal(a[1:])
	return False

		
	
	
	
#print(rec_all_equal(a))
#print(rec_all_equal(b))
	


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
	#return True
	if n.data == None:
		return True
	if not n.next:
		return False
	contains_None_data_node(n.next)
			

a = ListNode(5,None)
print(contains_None_data_node(a))



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
	def __repr__(self):
		return str(self.data)


def count(n,x):
	result = 0
	if not n:
		return result
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
class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)
        
class Vertex:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):         # voor afdrukken
        return str(self.data)
    
    def __lt__(self, other):    # voor sorteren
        return self.data < other.data

import math
INFINITY = math.inf # float("inf")

def vertices(G):
    return sorted(G)

def edges(G):
    return [(u,v) for u in vertices(G) for v in G[u]]


def clear(G): 
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)



def BFS(G,s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s) 
    while q:
        u = q.dequeue() 
        for v in G[u]:
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
			


				
				
v = [Vertex(i) for i in range(8)]

G = {v[0] : v[1],
	v[1] : v[2],
	v[2] : [v[4],v[3]],
	v[4] : v[1]}
	

def node_in_cyle(G,s):
	BFS(G,v[0])
	for i in G:
		if i.distance != INFINITY:
			print(i)
	
node_in_cyle(G,v[0])


	