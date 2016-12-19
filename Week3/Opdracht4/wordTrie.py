
class Trie:
	def __init__(self,parent,child):
		self.parent = parent
		self.child = child
		self.value =1

	def __repr__(self,nspaces=0):
		s1 = ''
		s2 = ''
		s3 = ''
		if self.child != None:
			s1 = self.child.__repr__(nspaces + 3)
		s2 = s2 + ' '*nspaces + str(self.parent) + '\n'
		return s1 + s2 + s3






class wordTrie:
	"""
    This class creates a tree of integers.   
    """
	def __init__(self,a=None):
		parent = None
		if a:
			a = open(a, 'r').read()
			self.insert_full_file(a)

	def __repr__(self):
		if self.root:
			return str(self.root)
		else:
			return 'null-tree'

			
		
	def insert_full_file(self,e):
		
		for word in e.split():
			self.insert(word)


	def insert(self, e, index = 0):
		if not self.parent:
			self.parent = Trie('',None)
		else:
			current = self.parent
			if not current.child:
				current.child = Trie(current.parent+e[index],None)
			else:
				if current == e[index]:
					current.value +=1
				current = current.child
				self.insert(e, index+1)

	
		
	def search(self,e, current = None):
		"""
		This function searches for a value in the tree
		
		Parameters
		----------
		e : integer
			value to be searched in the tree
		

		Return
		------
		wantedValue : integer
			wanted value to be searched in the tree
		
		Example
		-------
		>>> rsearch(5)
		>>> 5
		"""
		if isinstance(e,int):
			if current == None:
				current = self.root
				
			if current.element == e:
				return current.element
			else:
				if current.right == None and current.left == None:
					return False
				elif e > current.element:
					return self.rsearch(e,current.right)
				elif e < current.element:
					return self.rsearch(e,current.left)
				
		else:
			print(e, "not in list")
			return 0
		
	
	
		
		

		



	



