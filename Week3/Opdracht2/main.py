class ListNode:
	def __init__(self,data,next_node):
		self.data = data
		self.next = next_node
	def __repr__(self):
		return str(self.data)

				
class MyCircularLinkedList:
	"""
    This class creates a looping list of nodes. 
    
    """
	def __init__(self):					
		self.tail = None			
		
	def __repr__(self):
		"""
		This prints the node_list. 
		
		
		Return
		------
		s : string
			string of the node_list
		
		Example
		-------
		>>> print(mylist)
		>>> 5 -> 6
		>>> print(myEmptyList)
		>>> 'empty list'
		
		"""
		s = '' 	
		
		if not self.tail:
			return 'empty list'
				
		current = self.tail.next
		if current != None:
			s = s + str(current)
			current = current.next
		while current != self.tail.next:					
			s = s + " -> " + str(current)
			current = current.next

		return s 

		
	def addLast(self,e):
		"""
		This function adds a node to the list. 
		
		Parameters
		----------
		e : integer
			value to add
		

		Example
		-------
		>>> addLast(5)
		>>> addLast(6)
		>>> node_list = 5 -> 6
		
		"""
		if not self.tail:
			self.tail = ListNode(e,self.tail)
		else:
			self.tail.next = ListNode(e,self.tail.next)
			self.tail = self.tail.next
			
		if not self.tail.next:
			self.tail.next = self.tail


	def delete(self,e, current = None):
		"""
		This function removes a function from the node_list. 
		
		Parameters
		----------
		e : integer
			value to be removed
		
		
		Example
		-------
		>>> node_list = 5 -> 6 -> 7
		>>> delete(6)
		>>> node_list = 5 -> 7
		
		"""
		if not current:
			current = self.tail
		
		if current.next.data == e:
			current.next = current.next.next
		else:
			self.delete(e,current.next)

		if e == self.tail.data:
			self.tail = None

			
mylist2 = MyCircularLinkedList()
print(mylist2)
mylist2.addLast(1)
mylist2.addLast(2)
mylist2.addLast(3)
mylist2.addLast(4)
mylist2.addLast(5)
print(mylist2)
mylist2.delete(1)
print(mylist2)
mylist2.delete(2)
print(mylist2)
mylist2.delete(3)
print(mylist2)
mylist2.delete(4)
print(mylist2)
mylist2.delete(5)
print(mylist2)


