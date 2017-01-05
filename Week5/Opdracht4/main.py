import sys
sys.path.append("../")
from BFS import *


def is_connected(G):
	BFS(G,v[0])
	for i in G:
		if i.distance == INFINITY:
			return False
	return True


def is_strongly_connected(G):
	"""
	This function checks every node in the graph is accessible from every node.
	
	Parameters
	----------
	G: graph 
		Dictionary of graph connections.
	
	Returns:
	--------
	is_strongly_connected : Boolean
		returns if the every node is accessible from every node.
	
	Example:
	--------
	>>> G = {
			v[0]: [v[1]],
			v[1]: [v[2]], 
			v[2]: [v[0]]
			}
	>>> True
	"""
	if not is_connected(G):
		return False
	
	temp_graph = {}

	for key, values in G.items():
		for value in values:
			temp_graph[value] = []
			temp_graph[value].append(key)
			
	if not is_connected(temp_graph):
		return False
	
	return True


	
	
	
v = [Vertex(i) for i in range(3)]
g = {
	v[0]: [v[1]],
    v[1]: [v[2]], 
    v[2]: [v[0]]
}


print("Checking if graph g is strongly connected.\n",is_strongly_connected(g))
print("\nLayout of g:\n",list(g.items()))
print(50*"=","\n")	



v = [Vertex(i) for i in range(3)]
g2 = {
	v[0]: [v[1]],
    v[1]: [], 
    v[2]: [v[0],v[1]]
}


print("Checking if graph g2 is strongly connected.\n",is_strongly_connected(g2))
print("\nLayout of g2:\n",list(g2.items()))































































