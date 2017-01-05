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
	"""
	This function checks if bridges in a graph are bridges.
	
	Parameters
	----------
	G: graph 
		Dictionary of graph connections.
	
	Returns:
	--------
	bridges : list of tuples
		returns a list of bridges in the graph.
	
	Example:
	--------
	>>> G = {
				v[0] : [v[1],v[3]],
				v[1] : [v[0],v[2]],
				v[2] : [v[1],v[3],v[4]],
				v[3] : [v[0],v[2]],
				v[4] : [v[2],v[5],v[6]],
				v[5] : [v[4],v[6]],
				v[6] : [v[4],v[5],v[7]],
				v[7] : [v[6]],
			}
	>>> [(2, 4), (4, 2), (6, 7), (7, 6)]	
	"""
	bridges = []
	for i in edges(G):		
		G[i[0]].remove(i[1])
		G[i[1]].remove(i[0])
		
		if not is_connected(G):
			bridges.append(i)
			print(i,"is a bridge. ",bridges)
		
		G[i[0]].append(i[1])
		G[i[1]].append(i[0])
	
	if len(bridges) <1:
		print("No bridges found.")
		
	return bridges


	
	
v = [Vertex(i) for i in range(8)]
g = {
	v[0] : [v[1],v[3]],
	v[1] : [v[0],v[2]],
	v[2] : [v[1],v[3],v[4]],
	v[3] : [v[0],v[2]],
	v[4] : [v[2],v[5],v[6]],
	v[5] : [v[4],v[6]],
	v[6] : [v[4],v[5],v[7]],
	v[7] : [v[6]],
}

print(get_bridges(g))


print(50*"=","\n")


v = [Vertex(i) for i in range(8)]
g2 = {
	v[0] : [v[1],v[3]],
	v[1] : [v[2],v[0]],
	v[2] : [v[3],v[1]],
	v[3] : [v[0],v[2]]
}

print(get_bridges(g2))









