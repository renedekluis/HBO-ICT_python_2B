import random

def createClass(students):
    """
    This function creates a class of students students
    with random birthdays 
    
    Parameters
    ----------
    students : integer
        number of students in a class
    
    Return
    ------
    list : list
        list of birthdays of the students
    
    Example
    -------
    >>> students = 4
    >>> list = [2,263,63,74]
    
    """
    list = []
    for x in range(students):
        list.append(random.randint(1, 365))
    return list




def calculateChance1(a):
    """
    This function returns the chance that two people share the same 
    birthday in a class of a
    
    Parameters
    ----------
    a : integer
        number of students in a class
    
    Return
    ------
    result : float
        percentage of the above explained chance
    
    Example
    -------
    >>> a = 23
    >>> result ~ 53
    
    """
    result = 0
    for x in range(100):
        chance = 1
        for i in range(a):
            chance = chance*(365-i)/365
        
        result = result+((1-chance)*100)
    
    return result/100


def calculateChance2(a):
    """
    This function returns the chance that two people share the same 
    birthday in a class of a
    
    Parameters
    ----------
    a : integer
        number of students in a class
    
    Return
    ------
    result : integer
        percentage of the above explained chance
    
    Example
    -------
    >>> a = 23
    >>> result ~ 53
    
    """
    duplicates = 0
    
    for i in range(100):
        lijst = list(set(createClass(a)))
        if len(lijst) < a:
            duplicates+=1
    result =  100-duplicates 
    return result  



print("Sum of algaritm times 100: ",calculateChance1(23),"%")
print("Result per class: ",calculateChance2(23), "%")


