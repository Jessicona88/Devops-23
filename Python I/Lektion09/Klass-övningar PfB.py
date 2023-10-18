#13.1
"""
class Bil:
    def __init__(self):
        self.fabrikat = "inget"
        self.årsmodell = 0
        self.tjänstevikt = 0
        self.motoreffekt = 0
        self.ägare = "ägare"

class Person:
    def __init__(self):
        self.namn = "namn"




bil1 = Bil()
"strängar måste markeras som en sträng"
bil1.fabrikat = "Renault"
bil1.årsmodell = 2010
bil1.tjänstevikt = 900
bil1.motoreffekt = 75
bil1.ägare = Person()
bil1.ägare.namn = "Frank"
bil2 = Bil()
bil2.fabrikat = "BMV"
bil2.årsmodell = 2011
bil2.tjänstevikt = 1500
bil2.motoreffekt = 150
bil2.ägare = Person()
bil2.ägare.namn = "Inger"

print("Första bilen", bil2.fabrikat, "tillhör", bil2.ägare.namn)
print(f"Modell från {bil2.årsmodell}, med {bil2.motoreffekt} hk.")

from Rektangel import Rektangel

in1 = int(input("Ange höjd: "))
in2 = int(input("Ange bredd: "))
r = Rektangel()
r.höjd = in1
r.bredd = in2
arean = r.area()
print(arean)

class Datum:
    def __init__(self):
        self.år = 0
        self.mån = 0
        self.dag = 0

    def __str__(self):
        return f"{self.år:04}-{self.mån:02}-{self.dag:02}"

idag = Datum()
idag.år = 1988
idag.mån = 3
idag.dag = 26

dagens = idag
print(dagens)


class Cirkel:
    def __init__(self, x=0, y=0, radie=0):
        self.x = x
        self.y = y
        self.r = radie

    def area(self):
        return 3.14 * self.r ** 2


    def __eq__(self, other):
        return self.r == other.r

    def __lt__(self, other):
        return self.r < other.r

c1 = Cirkel(1, 1, 3)
c2 = Cirkel(2, 2, 3)

print(c1 == c2)
print(c1 != c2)
print(c1 < c2)

"""

class Flervåningshus():
    def __init__(self, l, b, v):
        self.längd = l
        self.bredd = b
        self.antal = v

    def höghus(self):
        return self.antal >= 10

    def yta(self):
        return self.längd * self.bredd * self.antal

class Skola(Flervåningshus):
    def __init__(self, l, b, v, k):
        super().__init__(l, b, v)
        self.antal_klassrum = k

    def yta(self):
        return super().yta() * self.antal_klassrum

s = Skola(15,1, 1, 2)
skolans_yta = s.yta()
print(skolans_yta)