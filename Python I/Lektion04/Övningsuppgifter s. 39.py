#7.4 Övningsuppgifter

#7.4

POST_1 = ""
POST_2 = ""
POST_3 = ""

import os
while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print(".:␣basicBILLBOARD␣:.")
    print(" ** ** ** ** ** ** ** ** ** ** ")
    print("P1:", POST_1)
    print("P2:", POST_2)
    print("P3:", POST_3)
    print("--------------------")
    print("c␣|␣ ̈Andra␣post")
    print("e␣|␣Stäng␣program")
    print("--------------------")
    indata = input("Meny> ")
    if indata == "e":
        break
    elif indata == "c":
        id = input("id: ")
        if id == "1":
            POST_1 = input("P1: ")
            print(POST_1)
        elif id == "2":
            POST_2 = input("P2")
        elif id == "3":
            POST_3 = input("P3")
# [X] 5. Pausa exekvering
    else:
        print("FEL: Okänt kommando", indata)
        input("Tryck␣enter␣för␣att␣fortsätta...")
# [X] 6. Gå till 1