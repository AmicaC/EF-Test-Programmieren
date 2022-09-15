teiler = input("Zahl?")

#decimal -> binary
binarylist = []

#decimal -> hexadecimal
hdList = []

integerX = int(teiler)
zahlB = integerX
zahlH = integerX

#Falls input < teiler = tauschen
if zahlB <= 2:
    teiler = zahlB
    zahlB = 2
if zahlH <= 16:
    teilerH = zahlH
    zahlH = 16

#Teilungsreste berechnen + Listen hinzufügen
while zahlB > 0:
    restB = zahlB % 2
    zahlB = zahlB // 2
    binarylist.insert(0, restB)
print (binarylist)

while zahlH > 0:
    restH = zahlH % 16
    if restH >= 9:
        if restH == 10:
            restH = "A"
        elif restH == 11:
            restH = "B"
        elif restH == 12:
            restH = "C"
        elif restH == 13:
            restH = "D"
        elif restH == 14:
            restH = "E"
        elif restH == 15:
            restH = "F"
    hdList.insert(0, restH)
    zahlH = zahlH // 16
    
print (hdList)

#Output
outputB = ''
for i in binarylist:
    outputB += str(i)
print(integerX, 'as binary number is', outputB)

outputH = ''
for i in hdList:
    outputH += str(i)
print(integerX, 'as hexadecimal number is', outputH)

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
