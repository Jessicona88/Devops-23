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
        print(heltal_minne)
        print(type(heltal_minne))
        if heltal not in heltal_minne:
            heltal_minne.append(heltal)
            print(heltal_minne)
    elif indata == "0":
        # spara till textfil.
        f = open("heltal.json.txt", "w")
        json.dump(heltal_minne, f)
        f.close()
        break
    else:
        print("Detta är inte ett tal.")
        print("Tryck Enter för att fortsätta.")
