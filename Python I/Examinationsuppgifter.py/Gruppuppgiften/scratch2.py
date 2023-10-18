import json

class Vara:
    # Specifierade 'float' för pris så att man inte försökte räkna ut med
    # sträng eller dylikt
    def __init__(self, namn, varukod, pris: float):
        self.namn = namn
        self.varukod = varukod
        self.pris = pris

    def __str__(self):
        # Ändrade utskriften för att snygga till utskriften av ordern
        return f" ({self.varukod}) {self.namn}: {self.pris} kr"


class Order(list):
    '''
    Genererar ett ordernummer och ett totalpris
    för en lista med objekt av typen vara.
    '''
    next_order_no = 1

    def __init__(self, varor: list):
        self.order_no = Order.next_order_no
        Order.next_order_no += 1
        self.varor = varor
        self.tot_pris = sum(vara.pris for vara in varor)

    def __str__(self):
        order_info = f"Order {self.order_no}\n"
        order_info += "Varor:\n"
        for vara in self.varor:
            order_info += str(vara) + "\n"
        order_info += f"Pris: {self.tot_pris}"
        return order_info




#Fil med sortimentkatalog ska alltid finnas, det är inget som skapas från noll
#i detta fall borde det öppnas automatiskt när kassan startar och filen stängs
#efter dagsavslut/kassaräkning.



#måste skapa tom lista först för att kunna lägga till saker med funktionen nyvara


# metod för att lägga till en ny vara
def nyvara(namn, varukod, pris):

        nyvara = Vara(namn, varukod, pris)
        lst_varor.append(nyvara)
        return lst_varor

lst_varor = []

vara1 = nyvara("Bryggkaffe", "P01", 12)
vara2 = nyvara("Cappuccino", "P02", 30)
vara3 = nyvara("Caffe latte", "P03", 30)

vara4 = nyvara("Billys pizza", "P04", 30)
vara5 = nyvara("Sallad", "P05", 80)
vara6 = nyvara("3 Pannkakor", "P06", 50)

vara7 = nyvara("Morotskaka", "P07", 35)
#får inte skriva 08, eller 008, får error, python gillar inte det
vara8 = nyvara("Chokladboll", "P08", 25)
vara9 = nyvara("Mjukglass", "P09", 25)


class Kassadisplay():
    def meny(self, bredd):
        print(f"| {'Café Python'} |".center(bredd))
        print("*"*bredd)
        toprint = ""
        for x in range(1, len(lst_varor) +1):
            if x % 3 != 0:
                toprint += f"│{lst_varor[x - 1]}".ljust(int(bredd/3)) + "│"
            else:
                toprint += f"│{lst_varor[x- 1]}".ljust(int(bredd/3)) +"│\n"
        print(toprint)
        print("*" * bredd)
        print("-" * bredd)
        print("1 | Ny order")
        print("2 | Modifiera vara")
        print("3 | Sök order")
        print("-" * bredd)
        print("Ange val (1, 2, 3)")
        return input("> ")



#Huvudmeny med display och sortiment
    def huvudmeny():
        while True:
            val = meny(96)
            if val == "1":
                reg_items = register_items(lst_varor)
            elif val == "2":
                print("Modifiera vara här")
            elif val == "3":
                print("Sök i gamla ordrar med hjälp av ordernummer") ########### Alis del ###########
            else:
                print("Fel inmatning")
            return register_items

    #denna funktion aktiveras när alt "A" väljs från huvudmenyn
    def register_items(lst_varor):
        reg_items = [] #tom lista för att spara aktuellt köp
        #evighetsloop tar en inmatning i taget istället för en hel order på samma gång.
        while True:
            item = input("Registrera varukod / Q för huvudmenyn: ").casefold().capitalize()
            if item != "Q":
                for vara in lst_varor:
                    if Vara.varukod == item:
                        #utskrift av varan så att det är rätt
                        print(vara)
                        #spara till lista
                        reg_items.append(vara)
            else:
                if len(reg_items) != 0: #förhindrar att tom order skapas
                    order = Order(reg_items)
                    return order




kassa = Kassadisplay()
kassa.meny(96)
kassa.register_items()
kassa.huvudmeny()

