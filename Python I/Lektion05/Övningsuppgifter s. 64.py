#Övningsuppgifter 11.2

#11.1

import json

random_stuff = [1337, 13.37, "Ååh Yää!"]


with open("json-demo.txt", "w") as f:
    random_stuff = json.dumps(random_stuff)
    f.write(random_stuff)
    print(random_stuff)

#11.2

import json
heltal_minne 
with open("json-demo.txt") as f:
    lista = f.read()

lista = json.loads(lista)
print(lista)
print(type(lista))

for i in lista:
    print(i)

#11.3

import os
import json

heltal_minne = []
f = open("heltal.json.txt", 'r')
heltal_minne = json.load(f)


while True:
    os.system("clear")
    print(".: intMEMORIZER :.")
    print(" ******************")
    for i in heltal_minne:
        print("* ", i)
    print("------------------")
    print("SUMMA:", sum(heltal_minne)) #leerlo del documento
    print("------------------")
    print("mata in heltal")
    print("0 stänger scriptet")
    print("------------------")
    indata = input("> ")
    if indata != "0":
        heltal = int(indata)
        if heltal not in heltal_minne:
            heltal_minne.append(heltal)
    elif indata == "0":
        # spara till textfil.
        f = open("heltal.json.txt", "w")
        json.dump(heltal_minne, f)
        f.close()
        break
    else:
        print("Detta är inte ett tal.")
        print("Tryck Enter för att fortsätta.")
