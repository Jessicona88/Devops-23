#5.2 Övningsuppgifter

#5.1

inmatning = input("Ange ett tal som du vill dubblera: ")

try:
    indata = int(inmatning)
    dubbel = indata * 2
    print(dubbel)
except ValueError:
    print(inmatning, "kan inte översättas till ett heltal.")

#5.2

#Användargränssnitt
space = 30
print(space * "*")
print("* The Great Divider *".center(space))
print("_" * space)
print("""
""")
print("""Beräknar c för uttrycket:       
""")
print("a \ b = c".center(space))
print("_" * space)

#Användaren får mata in a och b värden
indata = input("Skriv in värdet för flyttal a: ")
indata2 = input("Skriv in värdet för flyttal b: ")
print("a = ", indata)
print("b = ", indata2)

#Här fångar man upp möjliga fel i inmatningen som strängar
#som inte går att typomvandla till flyttal eller nollor
try:
    indata_fl = float(indata)
    indata2_fl = float(indata2)
    resultat = indata_fl/indata2_fl
    print("_" * space)
    print(indata_fl, " / ", indata2_fl, " = ", float(resultat))
except ValueError:
    print("a = ", indata)
    print("b = ", indata2)
    print("FEL: Ogiltigt nummer")
except ZeroDivisionError:
    print("FEL: Division med 0")

#5.3

#Användargränssnitt
print(".:MATHLETE V.2.0.:".center(30))
print("-" * 30)

indata = []
inp = ()

while True:
    try:
        inp = input("Ange ett värde: ")
        print(inp)
        if inp != "exit":
            heltal = int(inp)
            indata.append(heltal)
        elif inp == "exit":
            break
    except ValueError:
        print("FEL: Ogiltigt nummer")

#Rita rad
print("-" * 30)

#Antal, summa och medelvärde
längd = len(indata)
summa = sum(indata)
medel = summa/längd
print("Kardinalitet: ", längd)
print("Summa: ", summa)
print("Medelvärde: ", medel)

