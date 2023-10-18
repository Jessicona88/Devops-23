#Övningsuppgifter 2.4
2.1
citat="datatyper␣har␣inbyggda␣metoder"
ny_citat = citat.upper()
print(ny_citat)

2.2
inmatning = float(input("Vilket flyttal vill du avrunda:"))
print(round(inmatning))

2.3
first = input("Hej! Vad heter du i förnamn?: ")
second = input("Vad är ditt efternamn: ")
print("Hej!", first, second)
""""""
2.4
age = int(input("Hur gammal är du:? "))
result = 18 - age
print("Du blir myndig om ", result, "år.")

2.5
num_1 = int(input("Ange en siffra: "))
num_2 = int(input("Ange en till: "))
num_3 = int(input("Ange ännu en: "))
num_4 = int(input("Nästan klara, ännu än: "))
num_5 = int(input("Sista siffran nu: "))
max_num = max(num_1, num_2, num_3, num_4, num_5)
print("Högsta siffran du angett är: ", max_num)

2.6
import math
vanligaKorvar2 = int(input("Hur många barn vill ha 2 korvar?: "))
vanligaKorvar3 = int(input("Hur många barn vill du 3 korvar?: "))

veganskaKorvar2 = int(input("Hur många barn vill ha 2 veganska korvar?: "))
veganskaKorvar3 = int(input("Hur många barn vill ha 3 veganska korvar?: "))

totaltVanligaKorvar = (vanligaKorvar2 * 2 + vanligaKorvar3* 3)/8
korvpaket_round = math.ceil(totaltVanligaKorvar)
totaltVeganskaKorvar = (veganskaKorvar2 * 2 + veganskaKorvar3 *3)/4
vegKorvpaket_round = math.ceil(totaltVeganskaKorvar)

antalElever = vanligaKorvar2 + vanligaKorvar3 + veganskaKorvar2 + veganskaKorvar3

print("Inköpslista:")
print("Vanliga korvar: ", korvpaket_round, "paket")
print("Veganska korvar: ", vegKorvpaket_round, "paket")
print("Dryck: ", antalElever, "st")

totaltBeloppKorv = korvpaket_round * 20.95
totaltBeloppVegKorv = vegKorvpaket_round * 34.95
beloppDryck = antalElever * 13.95

notan = totaltBeloppKorv + totaltBeloppVegKorv + beloppDryck
print(notan, "SEK")
