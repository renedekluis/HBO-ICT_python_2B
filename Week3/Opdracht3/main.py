class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)
		
		
		
class BSTNode:
	def __init__(self,element,left,right):
		self.element = element
		self.left = left
		self.right = right

	def __repr__(self,nspaces=0):
		s1 = ''
		s2 = ''
		s3 = ''
		if self.right != None:
			s1 = self.right.__repr__(nspaces + 3)
		s2 = s2 + ' '*nspaces + str(self.element) + '\n'
		if self.left != None:
			s3 = self.left.__repr__(nspaces + 3)
		return s1 + s2 + s3

	def insert(self,e):
		parent = self
		current = None
		found = False

		if parent.element < e:
			current = parent.right
		elif parent.element > e:
			current = parent.left
		else:
			found = True;

		while not found and current:
			parent = current
			if parent.element < e:
				current = parent.right
			elif parent.element > e:
				current = parent.left
			else:
				found = True

		if not found:
			if parent.element < e:
				parent.right = BSTNode(e,None,None)
			else:
				parent.left = BSTNode(e,None,None)
		return not found

	def insertArray(self,a, low=0, high=-1):
		if len(a) == 0:
			return
		if high == -1:
			high = len(a)-1
		mid = (low+high+1)//2
		self.insert(a[mid])
		if mid > low:
			self.insertArray(a,low,mid-1)
		if high > mid:
			self.insertArray(a,mid + 1,high)

	def search(self,e):
		current = self
		found = False
		while not found and current:
			if current.element < e:
				current = current.right
			elif current.element > e:
				current = current.left
			else:
				found = True
		if found:
			return current
		else:
			return None

	def search2(self,e):
		if self.element == e:
			return self
		parent = self.getParent(e)
		if parent == None:
			return None
		if parent.element < e:
			return parent.right
		return parent.left

	def getParent(self,e):
		parent = self
		current = None
		found = False

		if parent.element < e:
			current = parent.right
		elif parent.element > e:
			current = parent.left;
		else:
			return None

		while not found and current:
			if current.element == e:
				found = True
			else:
				parent = current
				if current.element < e:
					current = current.right
				else:
					current = current.left
		if found:
			return parent
		else:
			return None
		
	def parentMinRightTree(self):
		parent = self.right
		current = parent.left
		while current.left:
			parent = current
			current = current.left
		return parent

	def delete(self,e):
		parent = self.getParent(e);

		if parent == None:
			return False
		if parent.element < e:
			current = parent.right
			if current.left == None:
				parent.right = parent.right.right
				return True
			else:
				if current.right == None:
					parent.right = parent.right.left
					return True
		else:
			current = parent.left
			if current.left == None:
				parent.left = parent.left.right
				return True
			else:
				if current.right == None:
					parent.left = parent.left.left
					return True
		if current.right.left == None:
			current.element = current.right.element
			current.right = current.right.right
			return True
		node = current.parentMinRightTree()
		current.element = node.left.element
		node.left = node.left.right
		return True

class BST:
	"""
    This class creates a tree of integers.   
    """
	def __init__(self,a=None):
		if a:
			mid = len(a)//2
			self.root = BSTNode(a[mid],None,None)
			self.root.insertArray(a[:mid])
			self.root.insertArray(a[mid+1:])
		else:
			self.root = None

	def __repr__(self):
		if self.root:
			return str(self.root)
		else:
			return 'null-tree'

	def search(self,e):
		if self.root and e:
			return self.root.search(e)
		else:
			return None

	def insert(self,e):
		if e:
			if self.root:
				return self.root.insert(e)
			else:
				self.root = BSTNode(e,None,None)
				return True
		else:
			return False

	def delete(self,e):
		if self.root and e:
			if self.root.element == e:
				if self.root.left == None:
					self.root = self.root.right
				elif self.root.right == None:
					self.root = self.root.left
				elif self.root.right.left == None:
					self.root.element = self.root.right.element
					self.root.right = self.root.right.right
				else:
					node = self.root.parentMinRightTree();
					self.root.element = node.left.element
					node.left = node.left.right
				return True
			else:
				return self.root.delete(e)
		else:
			return False
			
	def max(self, current = None):
	"""
    This function returns the maximum value of the tree.
    
    Return
    ------
    max_value : integer
        maximum value found in the tree
    
    Example
    -------
    >>> tree.max()
	>>> 10
    """
		if current == None:
			current = self.root
			
		if current.right == None:
			return current.element
		else:
			return self.max(current.right)
		
	def rsearch(self,e, current = None):
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
		
	
	def rinsert(self,e, current = None):
	"""
    This function adds a new value to the tree 
    
    Parameters
    ----------
    e : integer
        value to be added to the tree
    
    Return
    ------
    succeded : bool
        returns if the value is succesfully added
    
    Example
    -------
    >>> rinsert(5)
	>>> True
    """
		if e == self.rsearch(e):
			print(e,"already in list")
			return False
		
		if isinstance(e,int):
			if current == None:
				current = self.root
				
				
			if not current.right:
				current.right = BSTNode(e,None,None)
				return True
			else:
				if e > current.element:
					return self.rinsert(e, current.right)
			if not current.left:
				current.left = BSTNode(e,None,None)
				return True
			else:
				if e < current.element:
					return self.rinsert(e, current.left)

		else:
			print(e, "is not an accepted value")
			return 0
		
		
	def showLevelOrder(self, current = None):
	"""
    This function returns a list of lists with the hierarchy of the tree 
    
	
    Return
    ------
    a : list of lists
        list of lists with the hierarchy of the tree 
    
    Example
    -------
    >>> print(showLevelOrder())
	>>> [5,[7,8,none],[3,none,4]]
	"""
		a = myqueue()
		b = myqueue()
		if not current:
			current = self.root
		

		if not current.right:
			return [current.element,current.left,current.right]
		else:
			b.enqueue(self.showLevelOrder(current.right))

		if not current.left:
			return [current.element,current.left,current.right]
		else:
			b.enqueue(self.showLevelOrder(current.left))
		
		
		a.enqueue([current.element,b])
		return a


		
		
if __name__ == '__main__':
	
	print('----------------')

	b = BST([1,2,3,4,5,6,7,8])

	a = b.max()
	print(a)
	
	a = b.rsearch(4)
	print(a)
	a = b.rsearch("g")
	print(a)
	a = b.rsearch(16)
	print(a)
	
	print(b)
	b.rinsert(16)
	print(b)
	
	print(b.showLevelOrder())
	
	
	
	


	



