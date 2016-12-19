
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
        