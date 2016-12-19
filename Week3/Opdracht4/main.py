

def count_words_in_file(filename):
	"""
    This function writes the number of words found in the trie 
		to a given file.
    
	Parameters
	------
	
	filename : file
		file the trie 
	
    
    Example
    -------
    >>> tree.max()
	>>> 10
    """
	file = open(filename, 'r')
	word_string = file.read()
	words_dict = {}
	for word in word_string.split():
		if word not in words_dict:
			words_dict[word] = 1
		else:
			words_dict[word] += 1

	output_file = open("output1.txt", 'w')
	for x in words_dict:
		output_file.write('{0:10} ==> {1:10d}\n'.format(x, words_dict[x]))

		
		
		
class TrieNode:
	"""
    This class creates a trie of letters.   
    """
	def __init__(self):
		self.count = 1
		self.branch = {}
	
	def __repr__(self):
		return str(self.branch) + ":"+str(self.count) + "\n"

	def write_to_file(self, file, string = ''):
		"""
		This function writes the number of words found in the trie 
			to a given file.
		
		Parameters
		------
		filename : file
			file the trie 
		
		
		Example
		-------
		>>> kat kast --> in Trie
		>>> k		==> 2
		>>> ka 		==> 2
		>>> kat 	==> 1
		>>> kas 	==> 1
		>>> kast 	==> 1

		"""
		for i in self.branch:
			s = string + str(i)
			value = str(self.branch[i].count)
			
			file.write('{0:10} ==> {1:10}\n'.format(s, value))
			self.branch[i].write_to_file(file,s)


class wortel:
	"""
    This class creates a trie of letters from a string.   
    """
	def __init__(self, file_name = None):
		self.root = TrieNode()
		if file_name:
			full_string = open(file_name,"r").read()
			for word in full_string.split():
					self.insert(word)
				
	def __repr__(self):
		return str(self.root)
		


	def insert(self,string):
		"""
		This function adds a string to the trie
		
		Parameters
		----------
		string : string
			value to be added in the tree
		
		
		Example
		-------
		>>> insert('kat kast')
		>>> 
		>>> 			kast
		>>> k		kas
		>>> 	ka
		>>> 		kat
		"""
		if self.root:
			current = self.root
			for letter in string:
				if letter in current.branch:
					current = current.branch[letter]
					current.count+=1
				else: 
				  current.branch.update({letter:TrieNode()})
				  current = current.branch[letter]
		else: 
			return
		
	def write_to_file(self,filename):
		"""
		This function writes the trie to a file
		
		Parameters
		----------
		filename : opened file
			file to be written to
		
		
		Example
		-------
		>>> kat kast --> in Trie
		>>> k		==> 2
		>>> ka 		==> 2
		>>> kat 	==> 1
		>>> kas 	==> 1
		>>> kast 	==> 1

		"""
		file = open(filename,"w")
		self.root.write_to_file(file)



input_file = "text.txt"
output1 = "output1.txt"
count_words_in_file(input_file)
print(open(output1, 'r').read())


output2 = "output2.txt"
tree = wortel(input_file)
tree.write_to_file(output2)
print(open(output2, 'r').read())

















