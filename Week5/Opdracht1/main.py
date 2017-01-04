from BFS import *


def is_connected(G):
	"""
	This function checks if graph is fully connected.
	
	Parameters
	----------
	
	G: graph 
		Dictionary of graph connections.
	
	Returns:
	--------
	is_connected : Boolean
		returns if the graph is fully connected or not.
	
	Example:
	--------
	
	>>> G = {v[0]:[v[1],v[2]],
			 v[1]:[v[0],v[2],v[3]],
			 v[2]:[v[0],v[1],v[3]],
			 v[3]:[v[7]],
			 v[7]:[v[3]]}
	>>> False	
	"""
	BFS(G,v[0])
	for i in G:
		if i.distance == INFINITY:
			return False
	return True



v = [Vertex(i) for i in range(8)]

G = {v[0]:[v[4],v[5]],
	 v[1]:[v[4],v[5],v[6]],
	 v[2]:[v[4],v[5],v[6]],
	 v[3]:[v[7]],
	 v[4]:[v[0],v[1],v[5]],
	 v[5]:[v[0],v[1],v[2],v[4]],
	 v[6]:[v[1],v[2]],
	 v[7]:[v[3]]}

print(is_connected(G))


v = [Vertex(i) for i in range(8)]

G = {v[0]:[v[4],v[5]],
	 v[1]:[v[4],v[5],v[6]],
	 v[2]:[v[4],v[5],v[6]],
	 v[4]:[v[0],v[1],v[5]],
	 v[5]:[v[0],v[1],v[2],v[4]],
	 v[6]:[v[1],v[2]]}

	 
	 
print(is_connected(G))













