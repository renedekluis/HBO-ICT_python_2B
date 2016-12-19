
class HashTable:
	def __init__(self):
		self.len = 10
		self.hashtable = set([]*self.len)
		self.number_of_elements = 0
	def __repr__(self):
		return str(self.hashtable)
		
	def search(self,e,saved_set = set()):
		if self.hashtable:
			b = self.hashtable.pop()
			saved_set.add(b)
			if e == b:
				return saved_set.pop()
			else:
				self.hashtable.add(self.search(e,saved_set))
				b = saved_set.pop()
				self.hashtable.add(b)
				return b
		else:
			return False

	def insert(self,e):
		if (self.number_of_elements+1)/self.len >= 0.75:
			self.rehash(self.len*2)

		self.hashtable.add(e)
		self.number_of_elements+=1

	def delete(self,e):
		self.hashtable.remove(e)
		self.number_of_elements-=1
		while (self.number_of_elements)/(self.len/2) < 0.75:
			self.rehash(self.len/2)
			
	def rehash(self,new_len):
		self.len = new_len
		self.hashtable = set(list(self.hashtable)*int(self.len))
		print(
			"\n-------------------------\n",
			"rehashing to:",
			self.len,
			"\n",
			self.hashtable,
			"\n-------------------------"
		)

class SCH:
	def __init__(self):
		self.root = HashTable()
	def __repr__(self):
		return str(self.root)
	def search(self,e):
		return self.root.search(e)
	def insert(self,e):
		self.root.insert(e)
	def delete(self,e):
		self.root.delete(e)
		
a = SCH()

for i in range(200):
	a.insert(i)

for i in range(100):
	a.delete(i)








