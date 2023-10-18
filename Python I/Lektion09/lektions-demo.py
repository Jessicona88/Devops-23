#En klass som beskriver en rektangel

class Rectangle():
    #Attribut
    length:0
    width:0

"""  #Metoder
    def area(self):
        #returnerar resultatet på en gång, skippar variabeln
        return self.length * self.width
"""

#Skapa objekt av klassen
#variabelnamnet kan vara vadsomhelst
r1 = Rectangle() #parentes anropar klassen som en funktion, funkar ej utan.
print(r1)
#Resultat: <__main__.Rectangle object at 0x10ef8d150>
#Nu finns det ett objekt i datorns minne
#print(r1.length)
#print(r1.width)

#Ändra attribut
r1.length = 10
r1.width = 5

print("Rektanglets area är ", r1.area())

r2 = Rectangle()
r2.width = 10
r2.length = 10
print("Area:", r2.area())


# mer komplicerad metod
    def __init__(self, length, width):
        self.length = length
        self.width = width


#efter init funktionen ändrar jag argumenten i parentesen
r3 = Rectangle(2, 3)

#Inkapsling skyddar attributen/instansvariablerna

    def __init__(self, length, width):
        #privata attribut __
        self.__length = length
        self.__width = width

#Extra metoder: setters och getters, för att modifera skydddade attribut/instansvariabler

    #getter
    def get_length(self):
        return self.__length

    #setter
    def set_length(self, length):
        self.__length = length

    #Definiera en metod som hämtar width

    def get_width(self):
        return self.__width

 #Säkra metoder, if, else eller try, except.
    # setter
    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print("Felaktig längd.")

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Felaktig width")

#Lista av objekt
lista = [
    Rectangle(1, 2),
    Rectangle(3, 4),
    Rectangle(5, 6)
]
#skriva ut min lista
print(lista)

#iterera över listan av rektanglar och skriva ut area på varje rektangel:
for r in lista:
    print(r.area())

#sammanlagt area på alla rektanglar i en funktion:
def get_sum(lista):
    sum = 0
    for r in lista:
        sum += r.area()
        print("Summa av alla arean", sum)

#Skapa 1000 rektanglar med slumpmässiga dimensioner
import random

#Skapa en tom lista
tom_lista= []

#Skapa en iteration som loopar 1000 gånger:
for i in range(1001):
    #skapa ett objekt, en instans av Rectangle
    tom_lista.append(Rectangle(random.randint(1, 100), randint(1, 100)))





