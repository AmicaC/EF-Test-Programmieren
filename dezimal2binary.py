def dezimalToBinary(zahl):
    binarylist = []
    teiler = 2
    #if zahl < 2:
        #teiler = zahl
        #zahl = 2
    while zahl != 0:
        binarylist.append(zahl%teiler)
        zahl = zahl%teiler
    print (binarylist)

dezimalToBinary(12)
