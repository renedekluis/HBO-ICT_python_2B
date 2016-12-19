
def getNumbers(a):
    """
    This function gets all the integers from a 
    
    Parameters
    ----------
    a : list
        The string of which the integers are returned
    
    Return
    ------
    lijst : list
        all integers in given a
    
    Example
    -------
    >>> a = "lalalala12lololo34"
    >>> lijst = [12,34]
    
    """
    lijst = [];
    if len(a) == 0:
        return "ERROR: given value is empty."
    
    for i in a:
        if i.isdigit():
            lijst.append(i)
        else:
            lijst.append(" ")
    lijst = "".join(lijst)
    lijst = lijst.split()
    lijst = [int(x) for x in lijst]
    return lijst

a = 'een123zin45 6met-632meerdere+7777getallen5'
b = []
print(getNumbers(a))
print(getNumbers(b))