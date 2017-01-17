import sys
sys.path.append("../")
from BFS import *


def no_cycles(G):
	"""
	This function looks if the graph contains a cycles .

	Parameters
	----------
	G: Dictionary
		Dictionary where graph layout is written. 
   

	Return
	------
	Doesn't_consist_cycles : boolean
		This boolean returns if the given graph doesn't have cycles.       

	EXAMPLE:
	
	>>> G = {
			v[0]:[v[1]],
			v[1]:[v[2],v[0]],
			v[2]:[v[3],v[1]],
			v[3]:[v[0]]
			}
	>>> True
	""" 		
	return (len(edges(G))/2) < len(G)



#Graaf bovenstaand aan de opdracht
v = [Vertex(i) for i in range(6)]

g1 = {
	v[0] : [v[3],v[4]],
	v[1] : [v[3],v[4],v[5]],
	v[2] : [v[3],v[4],v[5]],
	v[3] : [v[0],v[1],v[2],v[4]],
	v[4] : [v[0],v[1],v[2],v[3]],
	v[5] : [v[1],v[2]]
	}	

print("\nGraaf 1 (bovenstaand aan de opdracht):")
print(no_cycles(g1))



#//////////////////////////////////////////////////////////////

#Graaf onderstaand aan de opdracht
v = [Vertex(i) for i in range(8)]
g2 = {
	v[0] : [v[4],v[5]],
	v[1] : [v[4],v[6]],
	v[2] : [v[5]],
	v[3] : [v[7]],
	v[4] : [v[0],v[1]],
	v[5] : [v[0],v[2]],
	v[6] : [v[1]],
	v[7] : [v[3]]
	}	
	
print("\nGraaf 2 (onderstaand aan de opdracht):")		
print(no_cycles(g2))




#//////////////////////////////////////////////////////////////

v = [Vertex(i) for i in range(8)]
g3 = {
	v[0] : [v[1],v[3]],
	v[1] : [v[2],v[0]],
	v[2] : [v[3],v[1]],
	v[3] : [v[0],v[2]]
	}	
	
print("\nGraaf 3 (gesloten vierkant):")		
print(no_cycles(g3))




#//////////////////////////////////////////////////////////////

v = [Vertex(i) for i in range(4)]
g4 = {
	v[0] : [v[1]],
	v[1] : [v[2],v[0]],
	v[2] : [v[3],v[1]],
	v[3] : [v[2]]
	}	
	
print("\nGraaf 4 (open vierkant):")		
print(no_cycles(g4))


v = [Vertex(i) for i in range(4)]
g5 = {
	v[0] : [v[1],v[2]],
	v[1] : [v[0],v[2]],
	v[2] : [v[1],v[0]]
	}	
	
print("\nGraaf 5 (test):")		
print(no_cycles(g5))
	
	
	
	
	
	
	
	
	