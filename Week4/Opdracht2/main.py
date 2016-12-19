
#week4.2
	

def FindHash2():
	dict = {} # make dict
	getal = 0 # 1e getal
	while( getal < 1 ): #ga door tot 1
		print(getal)
		try: # probeer
			dict[hash(getal)]
			print(repr(getal))
			break
		except: # als de try niet lukt
			dict.update({hash(getal):getal})#zet getal + hash in dict
			getal = getal + 0.01 #tel getal omhoog
	for x in dict.keys():
		print(x,dict[x])
    #return print("klaar")
		





def FindHash():
    dict = {} # make dict
    getal = 0 # 1e getal
    while( getal < 1 ): #ga door tot 1
        try: # probeer
            dict[hash(getal)]
            print(repr(getal))
            break
        except: # als de try niet lukt
            dict.update({hash(getal):getal})#zet getal + hash in dict
            getal = getal + 0.01 #tel getal omhoog
    #return print("klaar")
    # NIET UITVOEREN OP 64 BIT COMPUTER.
	
#FindHash2()


print(hash(0.9137260267282177))
print(hash(0.9400579282662489))
print(hash(-2008789643))



















