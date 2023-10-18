#9.4 Övningsuppgifter
'''
#9.1
heltal = []
for i in range(0, 100001):
    if i % 2 == 0:
        heltal.append(i)
summa = sum(heltal)
print(summa)
#9.2
udda = []
for i in range(0, 501):
    if i % 2 != 0:
        udda.append(i)
summa = sum(udda)
print(summa)

# 9.3
registrerade=["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar=["Anna", "Erik", "Karl"]

for i in registrerade:
    if i in avanmälningar:
        del registrerade[0]
print(registrerade)

#9.4
todos =['Städa', 'Handla', 'Plugga', 'Ge blod']

for i in todos:
    print("-" + i)

# 9.5

POST_1 =[]
Display = ()
import os
while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print(".:␣STACKMASTER V1.33.7␣:.")
    print("-------------------------")
    print(Display)
    for i in POST_1:
        print("-" + i)
    print("-------------------------")
    print("          |MENU|         ")
    print("push| Push element to stack")
    print("pull| Pull element from stack")
    print("exit| Exit program")
    print("-------------------------")
    try:
        indata = input("Meny> ")
        if indata == "exit":
            break
        elif indata == "push":
            id = input("ITEM: ")
            POST_1.append(id)
        elif indata == "pull":
            POST_1.pop()
        else:
            print("FEL: Okänt kommando", indata)
            input("Tryck␣enter␣för␣att␣fortsätta...")
    except IndexError:
        print("Listan är redan tom")
        Display = ("Tomt =(")

'''

