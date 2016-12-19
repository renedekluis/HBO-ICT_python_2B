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

  
print(machtv1(2,10))
print(machtv2(2,10))
print(machtv3(2,10))
print("multiplied ",trace(2,10)," times.")



