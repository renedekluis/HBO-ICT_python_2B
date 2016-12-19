


def FindHash():
    hashDict = {} 
    getal = 0 
    while( getal < 1 ): 
        try: 
            hashDict[hash(getal)]
            print(repr(getal))
            break
        except: 
            hashDict.update({hash(getal):getal})
            getal = getal + 0.000000001 

	
FindHash()




















