
class Person():
    namn = ()
    ålder = 0
    adress = ()

    #Metod
    def person(self):
        print(f"Denna person heter {self.name}, hon är {self.ålder} gammal och bor på {self.adress}.")
    #alt print(self.name, är self.ålder, och bor på self.adress)

p = Person()
p.name = "Jessica"
p.ålder = 35
p.adress = "Banangatan 1"


class Circle():
    omkrets: 0
    radie:0
    diameter: 0

    def rund(self):
        return self.radie * 3.14 * 2

 #attribut
c = Circle()
c.radie = 1.593


print(c.rund())


#Har skapat klassen bankkonto:
class Bankkonto():
    #Konstruktor
    #Nedan står instansvariabler för instansering
    def __init__(self):
        self.kontonummer = 0
        self.saldo = 0
        self.pinkod = 0

    #Klassens metoder (funktioner endast för denna klass), med parametern self
    def insättningar(self):
        try:
            kod = int(input("Ange pinkod: "))
            #För att komma åt instansvariablerna (saldo,pinkod) behöver jag inne i metoden skriva self
            if self.pinkod == kod:
                insättning = int(input("Ange belopp för insättning: "))
                self.saldo += insättning
                print("Insättning: ", insättning, "Nuvarande saldo: ", self.saldo)
        except:
            print("Det har skett nåt fel")

    def uttag(self):
        kod = int(input("Ange pinkod: "))
        try:
            if self.pinkod == kod:
                print("Pinkod är rätt")
                uttag = int(input("Ange belopp för uttag: "))
                self.saldo -= uttag
                print("Uttag: ", uttag, "Nuvarande saldo: ", self.saldo)
        except:
            print("Det har skett nåt fel")

#Instansera ett objekt av klassen Bankkonto
kontoinnehavare1 = Bankkonto()
kontoinnehavare1.kontonummer = 3330
kontoinnehavare1.pinkod = 1402
kontoinnehavare1.uttag()
kontoinnehavare1.insättningar()

kontoinnehavare2 = Bankkonto()
kontoinnehavare2.kontonummer = 3333
kontoinnehavare2.pinkod = 1898
kontoinnehavare2.uttag()
kontoinnehavare2.uttag()

print("Hej kontoinnehavare, dagens transaktion ser ut som följande: ", kontoinnehavare1.uttag)
print("Hej kontoinnehavare, dagens transaktion ser ut som följande: ", kontoinnehavare1.insättningar)



class Employee():
    def __init__(self):
        self.namn = "Inget namn än"
        self.löneinformation = 0
        self.anställningsdatum = []

    def lojalitet(self):
        dagensdatum = [2023, 9, 21]
        return dagensdatum[0] - self.anställningsdatum[0]


Eva_Britt = Employee()
Eva_Britt.anställningsdatum = [1985, 8, 15]
antal_år = Eva_Britt.lojalitet()
print("Eva_Britt Söderström har arbetat på Södersjukhuset i", antal_år, "år.")


class Student():
    def __init__(self, n, b):
        self.namn = n
        self.betyg = b

    def genomsnittsbetyg(self):
        try:
            summa = sum(self.betyg)
            medel = summa/3
            return medel
        except:
            print("Error")


student_A = Student("Marie Curie", [""" Fysik """100, """Kemi"""100, """Strålskydd"""63])
a = student_A.genomsnittsbetyg()
print(student_A.namn, "har genomsnittsbetyget", a)



