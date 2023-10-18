#14.6 Övningsuppgifter

#14.1
"""
def km_to_miles(dist):
    distance = int(dist) * 0.621371192
    return distance

def miles_to_km(dist):
    distance = float(dist) * 1.609344
    return distance


indata = input("Ange avstånd: ")
x = indata.endswith("km")
y = indata.endswith("miles")
if x == True:
    dist = indata.strip("km")
    print(f"{km_to_miles(dist)} mil.")
elif y == True:
    dist = indata.strip("miles")
    print(f"{miles_to_km(dist)} km.")


#14.2
import ui

#Variabler

exempel = "Inköpslista"
altA = "A | Visa inköpslista"
altB = "B | Lägg till vara"
altC = "C | Ta bort vara"
altX = "X | Stäng programmet"
text = (f"Detta är ett exempel på hur \n| ett gränssnitt kan se ut")
presentation = "Välj vad du vill göra"


#Implementering av funktioner
ui.line(False)
ui.header(exempel)
ui.line(True)
ui.echo(text)
ui.line(False)
ui.header(presentation)
ui.line(False)
ui.echo(altA)
ui.echo(altB)
ui.echo(altC)
ui.echo(altX)
ui.line(False)
#Input går sist ananrs stoppar det hela körningen och utskrift av funktioner
val = input("| Val > ")
#Utskrift av input via funktionen prompt()
ui.prompt(val)


#14.3
import random

numbers = []

#Rad 1: gör rad 2 10 gånger:
for x in range(10):
    #rad 2: lägg till listan numbers ett random heltal från random modulen från 0 till 9.
    numbers.append(random.randint(0,9))


def get_even(list):
    #kopierar originallistan
    list = numbers.copy()
    even = []
    for l in list:
        if l % 2 == 0:
            even.append(l)
    print(even)

print(numbers)
get_even(numbers)

"""

#14.4

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


#14.6

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

print_table(tom_lista)







