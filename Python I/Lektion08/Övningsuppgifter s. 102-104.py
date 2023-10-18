#Kompendiet
personlista =[
    {
        "namn": "Babbar",
        "ålder": 60
    },
    {
        "namn": "Bing",
        "ålder": 5
    }
]
#Skapa nyckelfunktion som returnerar det värdet som sorteringen ska göras efter.
def get_age(element):
    return element["ålder"]

sortedlist = sorted(personlista, key=get_age)
print(sortedlist)

def get_name(element):
    return element["namn"].lower() #gör om alla strängar till gemener annars
                                   #kommer prioritera versaler.

sortedlist = sorted(personlista, key=get_name)#lista, nyckel, reverse T/F
print(sortedlist)



#15.2 Övningsuppgifter

#15.1
"""
persons = [
    "Alice", "Lucas", "Olivia",
    "Liam", "Astrid", "William"
]
studenter = sorted(persons)
print(studenter)

for s in studenter:
    print("[ ] ", s)


#15.2

import random
numbers = []
for x in range(10):
    numbers.append(random.randint (0, 20))

print("BEFORE SORTING:")
for n in numbers:
    print("—", n)

print("AFTER SORTING:")
sort_numbers = sorted(numbers)
for sn in sort_numbers:
    print("—", sn)

"""
#15.3


teams = {
    "Brazil": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals for": 0,
        "goals against": 0
    },
    "Serbia": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals for": 0,
        "goals against": 0
    },
    "Switzerland" : {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals for": 0,
        "goals against": 0
    },
    "Costa Rica": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals for": 0,
        "goals against": 0 }
}


def add_game(home_team, home_score, away_team, away_score):
    if home_team in teams and away_team in teams:
        if home_score > away_score:
            teams[home_team]["wins"] += 1
            teams[away_team]["losses"] += 1
            teams[home_team]["goals for"] += home_score
            teams[away_team]["goals against"] += home_score
        elif home_score < away_score:
            teams[away_team]["wins"] += 1
            teams[home_team]["losses"] += 1
            teams[away_team]["goals for"] += away_score
            teams[home_team]["goals against"] += away_score
        elif home_score == away_score:
            teams[home_team]["draws"] += 1
            teams[away_team]["draws"] += 1
            teams[home_team]["goals for"] += home_score
            teams[home_team]["goals against"] += away_score
            teams[away_team]["goals for"] += away_score
            teams[away_team]["goals against"] += home_score
    else:
        print("Det har skett något fel på vägen för koden funkar")


#17 juni 2018
add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
#22 juni 2018
add_game("Brazil", 2, "Costa Rica", 0)
add_game("Serbia", 1, "Switzerland", 2)
#27 juni 2018
add_game("Serbia", 0, "Brazil", 2)
add_game("Switzerland", 2, "Costa Rica", 2)

#print(teams)

#14.5
def make_list(teams):
    tom_lista = []
    for land in teams:
        country_dict = {  # första nyckel
            "country": land,
            "wins": teams[land]["wins"],
            "draws": teams[land]["draws"],
            "losses": teams[land]["losses"],
            "goals_for": teams[land]["goals for"],
            "goals_against": teams[land]["goals against"]
        }
        # appenda detta till tomlistan
        tom_lista.append(country_dict)
    return tom_lista

tom_lista = make_list(teams)
print(tom_lista)


def sort_list(tom_lista):
    return tom_lista["wins"]

teams_list_sorted =  sorted(tom_lista, key=sort_list, reverse=True)
print(teams_list_sorted)


def print_table(lista):
    print("-"*46)
    print("| # |", "Nation".ljust(10),"| W | D | L |GF |GA |GD | P |")
    print("-" * 46)
    num = 1
    for i in lista:
        c = i["country"]
        gd = i["goals_for"]-i["goals_against"]
        w = i["wins"]
        d = i["draws"]
        l = i["losses"]
        gf = i["goals_for"]
        ga = i["goals_against"]
        p = i["wins"] * 3 + i["draws"]
        print(f"| {num} |{c.ljust(11)} | {w} | {d} | {l} | {gf} | {ga} |{str(gd).rjust(2)} | {p} |")
        num += 1
    print("-" * 46)

print_table(teams_list_sorted)

