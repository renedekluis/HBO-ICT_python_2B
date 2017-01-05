import sys
sys.path.append("../")
from BFS import *


def is_connected(G):
	BFS(G,v[0])
	for i in G:
		if i.distance == INFINITY:
			return False
	return True

def get_bridges(G):
	bridges = []
	for i in edges(G):		
		G[i[0]].remove(i[1])
		G[i[1]].remove(i[0])
		
		if not is_connected(G):
			bridges.append(i)
		
		G[i[0]].append(i[1])
		G[i[1]].append(i[0])

	return bridges



def is_Euler_graph(G):
	"""
	This function checks if given graph is an Eulerian graph.
	
	Parameters
	----------
	G: graph 
		Dictionary of graph connections.
	
	Returns:
	--------
	is_Euler_graph : Boolean
		Returns if the number of all connections in given graph are even.
	
	Example:
	--------
	>>> G = {
			v[0] : [v[1],v[3]],
			v[1] : [v[2],v[0]],
			v[2] : [v[3],v[1]],
			v[3] : [v[0],v[2]]
			}
	>>> True
	"""
	for i in vertices(G):
		if len(G[i]) % 2 > 0:
			return False
	return True

	
def get_Euler_circuit(G):
	"""
	This function calculates an Euler circuit from a graph.
	
	Parameters
	----------
	G: graph 
		Dictionary of graph connections.
	
	Returns:
	--------
	temp_list : List
		List with the Euler circuit of the graph.
	
	Example:
	--------
	>>> G = {	
			v[0] : [v[1],v[3]],
			v[1] : [v[2],v[0]],
			v[2] : [v[3],v[1]],
			v[3] : [v[0],v[2]]
			}
	>>> [2, 3, 0, 1, 2]
	"""
	start_key = list(G.keys())[0]

	a = edges(G)
	temp_list = []
	temp_list.append(start_key)
	
	while(G[start_key]):
		for t in G[start_key]:
			if (start_key, t) not in get_bridges(G):
				break

		temp_list.append(t)
		G[start_key].remove(t)
		G[t].remove(start_key) 
		start_key = t

	if len(temp_list) >= len(a)//2:
		return temp_list
	return [None]



print("\n")	
print(50*"=","\n")
#  ///////////////////////	
# ///Assignment graph ///	
#///////////////////////	
	
v = [Vertex(i) for i in range(8)]
g = {
	v[0] : [v[1],v[2]],
	v[1] : [v[0],v[3]],
	v[2] : [v[0],v[3]],
	v[3] : [v[1],v[2],v[4],v[6]],
	v[4] : [v[3],v[5],v[6],v[7]],
	v[5] : [v[4],v[6]],
	v[6] : [v[3],v[4],v[5],v[7]],
	v[7] : [v[4],v[6]]
}
print(
	"\nTesting graph of assignment",
	"\n----------------------------------\n"
)
print("Checking if graph is an Euler graph: ",is_Euler_graph(g))
print("Euler circuit solution: ",get_Euler_circuit(g))
	

print("\n")
print(50*"=","\n")
#  /////////////////////////
# ///assignment 3 graph ///	
#/////////////////////////	
	
v = [Vertex(i) for i in range(8)]
g1 = {
	v[0] : [v[1],v[3]],
	v[1] : [v[0],v[2]],
	v[2] : [v[1],v[3],v[4]],
	v[3] : [v[0],v[2]],
	v[4] : [v[2],v[5],v[6]],
	v[5] : [v[4],v[6]],
	v[6] : [v[4],v[5],v[7]],
	v[7] : [v[6]],
}
print(
	"\nTesting graph assignment 3",
	"\n----------------------------------\n"
)
print("Checking if graph is an Euler graph: ",is_Euler_graph(g1))
print("Euler circuit solution: ",get_Euler_circuit(g1))




print("\n")
print(50*"=","\n")
#  /////////////////////////
# ///	   square		///	
#/////////////////////////	


v = [Vertex(i) for i in range(4)]
g2 = {	
	v[0] : [v[1],v[3]],
	v[1] : [v[2],v[0]],
	v[2] : [v[3],v[1]],
	v[3] : [v[0],v[2]]
}
print(
	"\nTesting Square",
	"\n----------------------------------\n"
)
print("Checking if graph is an Euler graph: ",is_Euler_graph(g2))
print("Euler circuit solution: ",get_Euler_circuit(g2))




print("\n")
print(50*"=","\n")
#  /////////////////////////
# ///	One line house	///	
#/////////////////////////	

v = [Vertex(i) for i in range(5)]
g3 = {
	v[0] : [v[1],v[3],v[4]],
	v[1] : [v[0],v[2],v[3],v[4]],
	v[2] : [v[1],v[3]],
	v[3] : [v[0],v[1],v[2],v[4]],
	v[4] : [v[0],v[1],v[3]]
}

print(
	"\nTesting one-liner house\n",
	"\n----------------------------------\n"
)
print("Checking if graph is an Euler graph: ",is_Euler_graph(g3))
print("Euler circuit solution: ",get_Euler_circuit(g3))
print("\n")
print(50*"=","\n")


























































	
	










