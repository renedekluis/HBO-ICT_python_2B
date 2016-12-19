
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
        print(n,"%2 = ", int(n%2))
        if int(n%2) == 0:
            return mybin(n/2) + '0'
        else:
            return mybin(n/2) + '1'



result = mybin(13)
print(result)



