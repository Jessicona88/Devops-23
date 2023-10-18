import random
import os
# Skapar klass Kort.

class Kort:

    # Attribut för klassen Kort
    def __init__(self, valör, färg, värde):
        self.valör = valör
        self.färg = färg
        self.värde = värde

    # Metod för att kunna printa ut kortets färg och valör.
    def visa_kort(self):
        print(f"{self.färg}{self.valör}")

    # Metod för att kunna ha tillgång till värdet så man kan räkna och jämföra värdena i kortspelet
    def get_värde(self):
        return self.värde


# Klass för kortlek.
class Kortlek:
    # När jag skapar ett objekt av klassen Kortlek kommer den ha en tom lista
    # för kortlek som fylls med 52 kort samt blandar dessa kort.
    def __init__(self):
        # Lagrar kortlekens kort.
        self.kortlek = []
        # Anropar metoden skapa kortlek
        self.skapa_kortlek()
        # Anropar metoden blandning av kortlek
        self.blanda()

    # Metod för att skapa kortlek med 52 kort med färg, valör och värde.
    def skapa_kortlek(self):
        färger = ["♠", "♥", "♦", "♣"]
        valörer = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung"]
        # Nästlade loopar för att skapa en kortlek med 52 kort.
        for färg in färger:
            for valör in valörer:
                # Bestämmer det numeriska värdet för varje valör
                if valör == "A":
                    värde = 14
                elif valör == "Knekt":
                    värde = 11
                elif valör == "Dam":
                    värde = 12
                elif valör == "Kung":
                    värde = 13
                else:
                    värde = int(valör)
                # Skapar kortobjekt
                uppsättning = Kort(färg, valör, värde)
                # Lägger kortobjekt till kortlek
                self.kortlek.append(uppsättning)

    # Metod för att blanda kortlek
    def blanda(self):
        random.shuffle(self.kortlek)

    def dela(self):
        return self.kortlek.pop()


# Klass Spelare
class Spelare:
    def __init__(self, kortlek):
        # Attribut för klass Spelare.
        # Vill att alla spelare ska spela under omgången med samma kortlek.
        self.kortlek = kortlek
        # Tom lista för att spara spelarens kort i hand
        self.hand = []
        # Håller reda på spelarens poäng
        self.poäng = 0
        # Håller reda på antal Ess för spelaren
        self.Ess = 0
        # Anropa metod spelstart så fort man skapar instans av Spelare
        self.spelstart()

    # Metod för att visa kort i handen för spelaren samt poängsumma.
    def visa_hand(self):
        for kort_i_hand in self.hand:
            # metod från klass Kortlek
            kort_i_hand.visa_kort()
        print("Poäng:", self.poäng)

    def spelstart(self):
        # Funktion starta spel där 2 kort utdelas till spelare.
        for kortutdelning in range(2):
            # metod från klassen Kortlek
            kort = self.kortlek.dela()
            self.hand.append(kort)
            # metod från klassen Kort
            self.poäng += kort.get_värde()
            # Om dragna kortet är Ess
            if kort.get_värde() == 14:
                # Ess adderas till self.Ess
                self.Ess += 1
        # Justera värdet för Ess vid behov
        if self.poäng > 21:
            self.justera_poäng()

    # Metod dra ett kort och hantera Ess och värde, ganska lik metod spelstart.
    # Skillnaden är att det görs ett kort i taget så länge poängen inte är > 21.
    def dra_kort(self):
        kort = self.kortlek.dela()
        self.hand.append(kort)
        self.poäng += kort.get_värde()
        if kort.get_värde() == 14:
            self.Ess += 1
        if self.poäng > 21:
            self.justera_poäng()

    # Metod för att hantera värdet för Ess
    def justera_poäng(self):
        # Dra av 13 poäng för varje Ess och ta bort ett Ess från self.Ess
        if self.Ess:
            self.Ess -= 1
            self.poäng -= 13

    # Metod för att hantera jämförelse av poäng och kunna utse vinnare
    def __gt__(self, other):
        # Denna metod jämför det till vänster om operatorn med det till höger och returnerar True om sant
        # Här vill jag bara jämföra poängen och inget annat.
        return self.poäng > other.poäng

    def __ge__(self, other):
        return self.poäng >= other.poäng


# Skapar evighetsloop för att spela så många omgångar som användaren vill.
while True:
    # Rensar terminalen
    os.system("clear")
    kortlek = Kortlek()
    spelare = Spelare(kortlek)
    # Visa hand för spelaren
    spelare.visa_hand()
    while spelare.poäng <= 21:
        plus1 = input("Vill du ta ett till kort? j/n: ").lower()
        if plus1 == "j":
            # Vid ja, dra ett kort och spara värde, kort och ESS.
            spelare.dra_kort()
            # Visa hand efter nytt kortdragning
            spelare.visa_hand()
            # Om spelaren har spruckit avbryts omgången
            if spelare.poäng > 21:
                print(f"Du har spruckit! 💣")
                break
        # Vid nej samt att spelaren inte har spruckit ska spelet fortsätta
        else:
            print("Bankirens tur: ")
            bankir = Spelare(kortlek)
            # Här vill jag att bankir ska alltid försöka slå spelaren och ha en fördel.
            while bankir.poäng < 21 and spelare > bankir:
                bankir.dra_kort()
            # Jämföra poängen och utse vinnaren.
            bankir.visa_hand()
            if bankir.poäng > 21:
                print("Du vinner")
            elif bankir >= spelare:
                print("Bankir vinner")
            else:
                print("Du vinner")
            break
    ny_runda = input("Spela igen? j/n: ").lower()
    if ny_runda != "j":
        break
