# 4.2 Övningsuppgifter

4.1

inmatning = []
talserie = []               
stopp = 0
while stopp < 1:
    inmatning = int(input("Ange en siffra: "))
    if inmatning > 0:
        talserie.append(inmatning)
        print(talserie)
    else:    
        stopp += 1


minsta = min(talserie)  
storsta = max(talserie)
summa = sum(talserie)
medelvarde = summa/len(talserie) 

print("Det minsta talet du matat in är : ", minsta)
print("Det största talet du matat in är : ", storsta)
print("Summan av alla tal är: ", summa)
print("Medelvärdet av alla tal är : ", medelvarde)

4.2 

faktor = int(input("Ange siffra: "))
siffra = 0
while True:
    siffra+= faktor
    print(siffra)
    siffra+=faktor
    print(siffra)
    siffra+= faktor
    print(siffra)
    inp = input("Fortsätt? ja eller nej: ")
    if inp == "ja":
        continue
    if inp == "nej":
        break    


4.3 

import random 

måfå = random.randint(1, 99)

print("Welcome to The Higher Lower Game. I will randomise a number between 0 and 99. \nCan you guess it? ")
gissningar = []
antal_gissningar = ()
while True:
    inp = int(input("Your guess:"))
    gissningar.append(inp)
    if inp < måfå:
        print("Higher!")
        continue
    elif inp > måfå:
        print("Lower")
        continue
    elif inp == måfå:
        print("You guessed right! The number is: ", inp)
        antal_gissningar = len(gissningar)
        print("Times you guessed ", antal_gissningar)
        break


    