#Funktioner och moduler

"""
def addera(tal1, tal2): #parametrar
    summa = tal1 + tal2
    return summa

#alt def addera(tal1, tal2):
    #return tal1 + tal2

#Anropa en funktion (call/invoke)
addera(1, 2)# argument

#resultatet måste lagras för att printa ut
result = addera(1, 2)
print(result)

# alt
print(addera(1, 2))
print(addera(3, 5))

#####################################

#Anropa en funktion som returnerar det minsta talet från en lista med tal:
def minimum(numbers):
    minst = min(numbers)
    return(minst)
#return min(lista)


numbers = [5, 2, 7, 4, 9]
print(minimum(numbers))

#####################################

#Lärarens lösning på föregående uppgift:
def minimum(lista):
    minsta_talet = lista[0] #fångar första listan (tal 1)
    for i in lista:
        if minsta_talet > i:
            minsta_talet = i

    return(minsta_talet)

my_list = [10, 2, 5, 50]
minimum(minimum(my_list))
"""
#####################################

#Funktion med flera argument samt användning av modul


import utils
#def greet (first_name , last_name):
    #print("Hello", first_name , last_name)

# greet() --> TypeError, argument saknas
utils.greet("Lisa","Svensson")