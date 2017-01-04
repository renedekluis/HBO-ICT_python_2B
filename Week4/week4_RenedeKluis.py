'''
Opdrachten 1 & 2 Week 4
Door:
	René de Kluis
	1661627
'''



class HashTable:
	'''
	This class is a hash table consisting of a list of sets
	'''
	def __init__(self):
		self.hashtable = [set()]
		self.number_of_elements = 0
	def __repr__(self):
		return str(self.hashtable)
		
	def search(self,e):	
		"""
		This function searches a value in the hashTable.
		
		Parameters
		----------
		e : To be defined type
			value to calculate the power on
		
		Return
		------
		value found : boolean
			returns if the value is found in the hashTable
		
		Example
		-------
		>>>e = 9
		>>>True
		>>>e = 0
		>>>False
	
		"""
		for i  in self.hashtable:
			if e in i:
				return True 
		return False
		
	def insert(self,e):
		"""
		this function inserts a value to the hash hashtable.
		
		Parameters
		----------
		e : To be defined type
			value to calculate the power on
			
		Example
		-------
		>>>e = 9
		>>>[{9}]
		

		"""
		self.number_of_elements += 1
		
		if self.number_of_elements/len(self.hashtable) > 0.75:
			self.rehash(2 * len(self.hashtable))
		

		self.hashtable[hash(e) % len(self.hashtable)].add(e)
		
		
	def delete(self,e):
		"""
		This function deletes a value from the hashTable.
		
		Parameters
		----------
		e : To be defined type
			value to calculate the power on
		
		Example
		-------
		[{6},{9},set(),set()]
		>>>e = 9
		[{6},set(),set(),set()]

		"""
		self.hashtable[hash(e) % len(self.hashtable)].remove(e)
		self.number_of_elements -= 1
		
	def rehash(self,new_len):
		"""
		This function rehashes the hashTable to twice the size.
		
		Parameters
		----------
		new_len : integer
			new length of hashtable
			
		Example
		-------
		>>>new_len = 4
		>>>len(self.hashtable) == 4

		"""
		temp_rehash_table = []
		for h in range(new_len):
			temp_rehash_table.append(set())
		for  i in self.hashtable:
			for j in i:
				temp_rehash_table[
					hash(j) % len(temp_rehash_table)
				].add(j)
		self.hashtable = temp_rehash_table
		print(
			"\n====================\nRehashing: \n\tNew len: ",
			new_len,
			"\n====================\n",
			temp_rehash_table
		)

		
a = HashTable()

for i in range(200):
	a.insert(i)

for i in range(100):
	a.delete(i)

print(
	"\n====================\nNumber of elements: ",
	a.number_of_elements,
	"\n====================\n"
)


#===============================================================


def find_duplicate_hash():
	"""
	This function searches for two values 
			what have the same hashvalue.
	
	Return
	------
	value : integer
		value with a duplicate hash value.
	
	Example
	-------
	>>>find_duplicate_hash()
	>>>0.53726837

	"""
	value = 0
	hashList = {}
	while value < 1:
		try:
			hashList[hash(value)]
			return repr(value)
		except:
			print(repr({hash(value):value}))
			hashList.update({hash(value):value})
			value += 0.00000001
	
#print(find_duplicate_hash())
#function call commented out, because a 64 bit computer takes too long to calculate.


