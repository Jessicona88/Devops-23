
# 10. 3

import os
import csv

while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    print(f""
          )
    print(".: PEOPLES DATABASE :.")
    print("----------------------")
    print("get_id | Get person by ID")
    print("scan_f | List people by FORENAME")
    print("scan_s | List people by SURNAME")
    print("exit | Exit program")
    print("----------------------")
    with open("databas.csv") as f:
        databas = csv.reader(f)
        indata = input("| > ")
        if indata == 'get_id':
            id = (input("Ange id: "))
            for rad in databas:
                for cell in rad:
                    if cell.startswith(id):
                        print(rad[1: ])
        elif indata == 'scan_f':
            förnamn = (input("Ange förnamn: "))
            for rad in databas:
                for cell in rad:
                    if rad[1] == förnamn:
                        print(rad[1: ])
        elif indata == 'scan_s':
            efternamn = (input("Ange efternamn: "))
            for rad in databas:
                for cell in rad:
                    if rad[2] == efternamn:
                        print(rad[1: ])
        elif indata == 'exit':
            break
        else:
            print("Unknown command")
            print("Press enter to continue...")



