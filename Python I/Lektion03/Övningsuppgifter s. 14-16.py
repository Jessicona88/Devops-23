# 3.3 Övningsuppgifter

3.1 

tal_1 = int(input("Ange ett tal: "))
tal_2 = int(input("Ange ännu ett tal: "))
tal_3 = int(input("Ange ett sista tal: "))
max_num = max(tal_1, tal_2, tal_3)
if True:
    print("Det största inmatade talet är ", max_num)

3.2

namn = input("Ange ditt namn: ")
alder = int(input("Ange din ålder: "))
#Tabell med ålder och sömnbehov/natt
tabell = {
    1: "14",
    2: "13",
    3: "12",
    4: "11,5",
    5: "11",
    6: "11",
    7: "10,5",
    8: "10",
    9: "10",
    10: "10",
    11: "9,5",
    12: "9",
    13: "9",
    14: "9",
    15: "9",
    16: "8,5"
}

if alder in tabell:
    barn_timmar = tabell[alder]
    print("Hallå", namn + "! Enligt Enligt Vardguidens rekommendationer behover individer i din alder,", alder, "år, sova", barn_timmar, "timmar per natt.")
else:
    print("Hallå", namn + "!Enligt Enligt Vardguidens rekommendationer behover individer i din alder,", alder, "år, sova 8 timmar per natt.")


3.3

import random
dice = random.randint(1, 6)

if dice == 2:
    print("Du slog en 2:a!")
    print(f"""

- - - - - - - - -
|   X           | 
|               | 
|           X   |          
- - - - - - - - -
""")
elif dice == 1: 
    print("Du slog en 1:a!")
    print(f"""

- - - - - - - - -
|               | 
|       X       | 
|               |          
- - - - - - - - -
""")
    
elif dice == 3: 
    print("Du slog en 3:a!")
    print(f"""

- - - - - - - - -
|  X            | 
|       X       | 
|            X  |          
- - - - - - - - -
""")
elif dice == 4: 
    print("Du slog en 4:a!")
    print(f"""

- - - - - - - - -
|   X       X   | 
|               | 
|   X       X   |          
- - - - - - - - -
""")
elif dice == 5: 
    print("Du slog en 5:a!")
    print(f"""

- - - - - - - - -
|   X       X   | 
|       X       | 
|   X       X   |          
- - - - - - - - -
""")   
elif dice == 6: 
    print("Du slog en 6:a!")
    print(f"""

- - - - - - - - -
|   X       X   | 
|   X       X   | 
|   X       X   |          
- - - - - - - - -
""")

3.4

land = input("Mata in ett land för att veta om det tillhör Norden eller Storbritannien: ")

Norden =("Danmark Finland Island Sverige Norge")
norden_gemener = Norden.lower()
NORDEN_VERSALER = Norden.upper()
Storbritannien = ("England Nordirland Skottland Wales")
storbritannien_gemener = Storbritannien.lower()
STORBRITANNIEN_VERSALER = Storbritannien.upper()

if land in Norden or land in norden_gemener or land in NORDEN_VERSALER:
    print(land, "tillhör Norden")
elif land in Storbritannien or land in storbritannien_gemener or land in STORBRITANNIEN_VERSALER:
    print(land, "tillhör Storbritannien")
else:
    print(land, "tillhör varken Norden eller Storbritannien")

3.5

kon = input("Ange kön: ")
harfarg = input("Ange hårfärg: ")
ogonfarg = input("Ange ögonfärg: ")

anvandare = [kon, harfarg, ogonfarg]

celebrities = {
    "Selena Gomes" : ["kvinna", "brun", "brun"],
    "Emma Watson" : ["kvinna", "brun", "brun"],
    "Daniel Radcliffe" : ["man", "brun", "brun"],
    "Rupert Grin" : ["man", "röd", "blå"],
    "lilla sjojungfrun" : ["kvinna", "röd", "blå"],
    "Kleopatra" : ["kvinna", "svart", "svart"],
    "Esmeralda" : ["kvinna", "svart", "grön"],
    "Idris Elba" : ["man", "svart", "svart"],
    "Ed Sheeran" : ["man", "röd", "svart"]
}
match = []
for nyckel, lista in celebrities.items():
    if lista == anvandare:
        match.append(nyckel)

if match:
    print("Du liknar:", ", ".join(match))
else:
    print("Du liknar en apa")
