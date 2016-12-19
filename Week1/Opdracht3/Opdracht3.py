def getPriem(a):
    """
    This function returns all prime numbers below a 
    
    Parameters
    ----------
    a : integer
        value to get all prime numbers below of
    
    Return
    ------
    lijst : list
        list of all prime numbers below a
    
    Example
    -------
    >>> a = 10
    >>> lijst = [2,3,5,7]
    
    """
    lijst = []
    removeList = []
    for i in range(2,a):
        lijst.append(i)
    if a < 2:
        return "ERROR: value to small."

    for x in range(2, len(lijst)):
        for j in range(2,a):
            if j%x == 0 and x != j:
                removeList.append(j)
        
    removeList = list(set(removeList))
    for t in removeList:
        lijst.remove(t)

    return lijst


primes = getPriem(1000)
print(len(primes))
print(primes)






