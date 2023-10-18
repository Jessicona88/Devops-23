"""
Iteration av bokstäver:
alfabet = "ABCDEFG"
index = 0
while index < len(alfabet):
        print(alfabet[index])
        index += 1
"""

text = input("Ange texten som ska granskas: ")
textLower = text.lower()
bokstav = input("Ange bokstaven vi ska hitta i texten: ")
bokstavLower = bokstav.lower()

count = 0
antal = 0
while count < len(textLower):
        if textLower[count] == bokstavLower:
                antal += 1
        count += 1

print("Bokstaven", bokstav, "förekommer", antal, "gånger i texten")

#6.2

print("Robber Translate")
print("-" * 16)

indata = input("Ange meningen som ska översättas: ")

vokalerna = ["a", "e", "i", "o", "u", " ", "ä", "ö", "å", "y"]

#loopa igenom, hitta allt som inte matchar vokalerna och lägg till 'o'
# och matchningen med append
tolkning = []
for i in range(len(indata)):
        if indata[i] in vokalerna:
                tolkning.append(indata[i])
                continue
        else:
                tolkning.append(indata[i])
                tolkning.append("o")
                tolkning.append(indata[i])
print(tolkning)


print("Svenska > ", indata)
print("Rövarspråk > ", " ".join(tolkning))

#6.3
#ta input, skapa ihopsatt sträng att matcha med en omvänd ihoppsatt sträng
indata = input("Skriv ditt palindrom: ")

#skapa for loop för att iterera och sätta ihop allt utan mellanslag eller tecken
strippas = [" ", "!", ",", "."]
nakenHund = []

for i in range(len(indata)):
    if indata[i] not in strippas:
        nakenHund.append(indata[i])
    else:
        continue


print(nakenHund)
strang_utan_mellanslag = "".join(nakenHund)
print(strang_utan_mellanslag)
omvand_lista = list(reversed(strang_utan_mellanslag))
print(omvand_lista)
ny_strang_utan_mellanslag = "".join(omvand_lista)
print(ny_strang_utan_mellanslag)
lite_ny_strang_utan_mellanslag = ny_strang_utan_mellanslag.lower()
lite_strang_utan_mellanslag = strang_utan_mellanslag.lower()

#jämföra bägge strängar och avgöra resultat
if lite_strang_utan_mellanslag == lite_ny_strang_utan_mellanslag:
    print(indata, "Är ett palindrom")
else:
    print(indata, "är INTE ett palindrom")