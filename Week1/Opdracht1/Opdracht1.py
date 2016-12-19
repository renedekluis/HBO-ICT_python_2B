


def mymax(a):
    """
    This function determines the maximum of a 
    
    Parameters
    ----------
    a : list
        The numbers of which the maximum will be calculated
    
    Return
    ------
    maximum : integer
        The highest number or an error if this is not used correctly
    
    Example
    -------
    >>> a = "[1, 2, 3, 4, 5, 6, 7 ]"
    >>> maximum = 7
    
    """
    
    maximum = 0
    if len(a) == 0:
        return "ERROR: given value is empty."
    for i in a:
        if isinstance(i, int): 
            if i > maximum:
                maximum = i
    
    return maximum

a = [1,2,6,4,9,'b',8,3,5]
b = []

print(mymax(b))
print(mymax(a))