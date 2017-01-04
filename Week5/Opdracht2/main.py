from BFS import *



v = [Vertex(i) for i in range(4)]

g = {
	v[0] : [v[1],v[3]],
	v[1] : [v[2],v[0]],
	v[2] : [v[3],v[1]],
	v[3] : [v[2],v[0]]
	}

	
g2 = {
	v[0] : [v[1]],
	v[1] : [v[2],v[0]],
	v[2] : [v[3],v[1]],
	v[3] : [v[2]]
	}	
	
	
def no_cycles(G, x = 0, start_node = 0):
	BFS(G,v[start_node])
	a = edges(G)
	start = a[start_node]
	
	if x < len(a):
		print(
			"checking:",
			start,
			"==",
			a[x],
			"\t|\t",
			start[0] == a[x][1]
		)
		print(a[x][1]<=start_node)
		if start[0] == a[x][1] and a[x] != (start[1],start[0]):
			print(start,a[x])
			return False
	
		no_cycles(G,x+1,start_node)
		
	else:
		print("\n===========================================\n")
		if start_node < len(a):
			start_node+=1
			return no_cycles(G,0+start_node,start_node)
		else:
			return True

		




print(no_cycles(g))



print(no_cycles(g2))
'''
G = {
	v[0] : [v[4],v[5]],
	v[1] : [v[4],v[6]],
	v[2] : [v[5]],
	v[3] : [v[7]],
	v[4] : [v[0],v[1]],
	v[5] : [v[0],v[2]],
	v[6] : [v[1]],
	v[7] : [v[3]],
	}
'''