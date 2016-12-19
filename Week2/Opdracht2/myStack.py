from _overlapped import NULL
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
            
        value : undefined type
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
        self.stack[len(self.stack)-1] : undefined value
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
        self.stack == [] : boolean
            boolean if the stack is empty (True) or not (False)
        
        Example
        -------
        >>> #stack = [4]
        >>> (self.stack == []) = False
        
        """
        return self.stack == []
        
        