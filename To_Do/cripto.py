rndchar=[]
def cripto (x):
    xlen=int(len(x)/4)
    for i in range(xlen):
        if int(i+1) % 4 == 0:
            rndchar.append("?")
        elif int(i+1) % 3 == 0:
            rndchar.append("!")
        elif int(i+1) % 2 == 0:
            rndchar.append("+")
        else:
            rndchar.append(".")
    criptxt=""
    for i in range(len(x)):
        criptxt+= chr(ord(x[i])+3)
        if int(i+1) % 4 == 0:
            criptxt += rndchar[0]
            del rndchar[0]    
        
    
    return(criptxt)
