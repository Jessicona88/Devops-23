import json
"""
notes = {
    "Meddelande från skolan": "Friluftsdag␣på␣tisdag",
    "Kom ihåg!": "Ta␣bilen␣till␣verkstad",
    "Inför tentamen": "Gör␣alla␣instuderingsuppgifter"
}

#12.1


while True:
    indata = input("Anteckning > ")
    try:
        print(notes[indata])
    except KeyError:
        print('FEL: Attribut existerar inte')


#12.3
for i in notes:
    print(i)

#12.4
for i in notes:
    print("Text: " + i + "|  Meddelande:  " + notes[i])
    print("______________________________________")
    

#12.5
print(notes)

indata = input("Vilken anteckning vill du ta bort? ")

del notes[indata]

print(notes)


#12.6



try:
    f = open("notes.txt", "w")
    notes = json.load(f)
    print(notes)
except FileNotFoundError:
    f = open("notes.txt", "r")
    notes = json.load(f)



import os

ui_bredd = 30

try:
    with open('notes.txt', 'r') as fil:
        notes_json = fil.read()
        notes = json.loads(notes_json)
        print(notes)
except FileNotFoundError:
    with open("notes.txt", "w") as fil:
        notes = {}

while True:
    os.system("clear")
    print("*" * 30)
    print(".: ALWAYSNOTE .:".center(ui_bredd))
    print("--gold edition--".center(ui_bredd))
    print("*" * 30)
    print("view " + "|" + " view note")
    print("add  "+ "|" + " add note")
    print("rm   "+ "|" + " remove note")
    print("exit "+ "|" + " exit program")
    print("*" * 30)
    try:
        indata = input("Menu > ")
        if indata == "view":
            val = input("Välj anteckning: ")
            print(notes[val])
        elif indata == "add":
            ny_titel = input("Ny anteckning: ")
            ny_text = input("Text: ")
            notes[ny_titel] = ny_text
            print(notes)
        elif indata == "rm":
            bort = input("Välj anteckning:")
            del notes[bort]
            print(notes)
        elif indata == "exit":
            print("Bye")
            with open("notes.txt", "w") as f:
                notes_json = json.dumps(notes)
                f.write(notes_json)
            break
        else:
            print("Try again")
    except KeyError:
        print("Ogiltigt val, försök igen")

"""

