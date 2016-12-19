'''
Opdrachten 1-4 Week 2
Door:
	René de Kluis
	1661627
'''

def machtv1(a,n):
    return a**n

def machtv2(a,n):
    assert n > 0
    m = 1
    for _ in range(0,n):
        m = m*a;
    return m


def machtv3(a,n):
	"""
    This function returns the result of a pow(n) 
    
    Parameters
    ----------
    a : integer
        value to calculate the power on
	
	n : integer
		value of the power
    
    Return
    ------
    m : integer
        result of a pow(n)
    
    Example
    -------
    >>> a = 2
	>>> n = 10
    >>> m = 1024
    
    """
	if n == 0:
		return 1
	elif n < 0:
		return 1/machtv3(a,-n)
	else:
		m = 1
		while n > 0:
			if n%2 == 0:
				m *= a * a
				n-=2
			else:
				m=a
				n-=1
		return m

def trace(a,n):
	"""
    This function returns the result of a pow(n) 
    
    Parameters
    ----------
    a : integer
        value to calculate the power on
	
	n : integer
		value of the power
    
    Return
    ------
    times : integer
        value of multiply times to calculate a pow(n)
    
    Example
    -------
    >>> a = 2
	>>> n = 10
    >>> m = 10
    
    """
	assert n > 0
	times = 0
	while n > 0:
		if n%2 == 0:
			times+=2
			n-=2
		else:
			times+=1
			n-=1
	return times

print("\n\nOPDRACHT 1\n-----------------------\n")  
print(machtv1(2,10))
print(machtv2(2,10))
print(machtv3(2,10))
print("multiplied ",trace(2,10)," times.")






class myStack:

    def __init__(self):
        """
        This function is the constructor of the meStack class
        
        Parameters
        ----------
        self : list
            the stack will be set on the object that calls this class
        
        
        Example
        -------
        >>> a = myStack() --> stack will be created on value a
        
        """
        self.stack = [] 
        
        

    def push(self, value):
        """
        This function add a value to the stack
        
        Parameters
        ----------
        self : list
            the stack
            
        value : type of stack
            value to add to the stack
        
        Example
        -------
        >>> # stack = []
        >>> # stack = [4]
        
        """
        self.stack.append(value)
        
        
        
    def pop(self):
        """
        This function removes the last value of the stack
        
        Parameters
        ----------
        self : stack
            the stack
        
        Example
        -------
        >>> # stack = [4]
        >>> # stack = []
        
        """
        self.stack.pop()
        
        
        
        
    def peek(self):
        """
        This function returns the last value of the stack
        
        Parameters
        ----------
        self : stack
            the stack
        
        Return
        ------
        last value on stack : type of stack
            last value on the stack
        
        Example
        -------
        >>> # stack = [4,5]
        >>> self.stack[len(self.stack)-1] = 4
        
        """
        if len(self.stack) > 0:
            result = self.stack[len(self.stack)-1]
            return result
        else:
            return "ERROR: Stack is empty"
    
    
    
    def isEmpty(self):
        """
        This function checks if the stack is empty
        
        Parameters
        ----------
        self : stack
            the stack
            
        Return
        ------
        if boolean is empty : boolean
            boolean if the stack is empty (True) or not (False)
        
        Example
        -------
        >>> #stack = [4]
        >>> return = False
        
        """
        return self.stack == []



    def size(self):
        """
        This function checks the size of the stack
        
        Parameters
        ----------
        self : stack
            the stack
            
        Return
        ------
        size of stack : integer
            value of the size of the stack
        
        Example
        -------
        >>> #stack = [4]
        >>> return = 1
        
        """
        return len(self.stack)    
    
    
    
    def show(self):
        """
        This function returns the values on the stack
        
        Parameters
        ----------
        self : stack
            the stack
            
        Return
        ------
        stack : list
            value on the stack
        
        Example
        -------
        >>> #stack = [4,5]
        >>> self.stack = [4,5]
        
        """
        return self.stack




print("\n\nOPDRACHT 2\n-----------------------\n")  
d = myStack()
print(d.peek())


d.push(2)
print(d.peek())


d.push(3)
print(d.peek())


d.pop()
print(d.peek())


b = d.isEmpty()
print(b)







def check(value):
    """
    This function checks if the list of brackets are correct
    
    Parameters
    ----------
    value : list
        list of brackets
        
    Return
    ------
    message : string
        if the list is correct the fuction returns "correct"
        
        if the list has invalid values the function returns an error
            including the first found invalid value
        
        if the list has invalid bracket usage, 
            the function will return the open brackets on the stack
    
    Example
    -------
    >>> #value = ['(',')']
    >>> return = "Correct"
    
    """
    brackets = { ')' : '(', '>' : '<', ']' : '['}
    stack = myStack()
    for i in value:
        if i in brackets.values():
            stack.push(i)
        elif i in brackets.keys():
            for x in brackets.keys():
                if i == x:
                    stack.pop()
        else:
            print("ERROR: '%s' not accepted" % i)
            return False

    if stack.isEmpty():
        return True
    else:
        print(stack.show())
        return str(stack.show())

		
		
print("\n\nOPDRACHT 3\n-----------------------\n")
# test 1
haakjes = ['<', '(', ')','>']
result = check(haakjes)
print(result)


# test 2
haakjes = ['<', '(', 'a','>']
result = check(haakjes)
print(result)

# test 3
haakjes = ['<', '(', '(','>']
result = check(haakjes)
print(result)

  

  
  

def mybin(n):
	"""
    This function returns the binary value of a decimal. 
    
    Parameters
    ----------
    n : integer
        value to convert to binary
    
    Return
    ------
    binary string : string
        string that contains the binary value of the given decimal
    
    Example
    -------
	>>> n = 10
    >>> binary string = '1010'
    
    """
	if n < 1:
		return ''
	else:
		if int(n%2) == 0:
			return mybin(n/2) + '0'
		else:
			return mybin(n/2) + '1'


print("\n\nOPDRACHT 4\n-----------------------\n")
print(mybin(13))






