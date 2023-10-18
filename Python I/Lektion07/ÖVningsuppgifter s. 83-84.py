#Övningsuppgifter 13.3

#13.1

import requests
import json

heltal = input("Ange ett heltal större än 0: ")

if int(heltal) >= 2:
    api_url = (f"https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer={heltal}")
    response = requests.get(api_url)
    response_dictionary = json.loads(response.text)
    print(response_dictionary)
    if response_dictionary["even"] == "false":
        nummertyp = " är inte ett jämnt nummer."
    else:
        nummertyp = " är ett jämnt nummer."
    if response_dictionary["prime"] == "false":
        primtal = " är inte ett primtal."
    else:
        primtal = " är ett primtal."
        faktorer = response_dictionary['factors']
        faktorer_str = str(faktorer)[1: -1]
        print(f"{heltal}{nummertyp} {heltal}{primtal}")
        print(f"Numrets faktorer är {faktorer_str}")
else:
    print("Någonting gick fel! Försök igen.")


#13.2

#lista städer tillgänglig väderrapport
print("""*Stockholm
*Uppsala
*Göteborg
*Malmö
*Västerås
""")
#användaren väljer stad
city = input("Enter the name of the city for which you want forecasts: ")
#byter ut svenska bokst mot engelska
city = city.replace("ä", "a")
city = city.replace("å", "a")
city = city.replace("ö", "o")
print(city)
#hämtar info från API
url = (f"https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/{city}")
get = requests.get(url)
#varför hittar inte jag Göteborg?
väder = json.loads(get.text)
#print(väder)
print(f"> {city}")
#hämta värdena
datum = väder["forecasts"]

print("----------------------")
print("FORECAST")
print("**********************")
for dates in datum:
    print(dates['date'],"    ", dates['forecast'])

#13.3

url = (f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")
artister = requests.get(url)
artister_get = json.loads(artister.text)
print(artister_get)

# for loopa genom artistnamnen så att avnändaren kan välja artist
for artist in artister_get['artists']:
    namn = artist['name']
    print(namn)
print("------------------")
val = input("Select artist: ")
print("> ", val)
for artist in artister_get["artists"]:
    namn = artist['name']
    id = artist['id']
    if val == namn:
        print(namn)
        print(id)
        break
url2 = (f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{id}")
#kommunicerar med API
information = requests.get(url2)
#koverterar från json till python
artistinfo = json.loads(information.text)
print(artistinfo)
print("******************")

# for info in artistinfo[]
for yttre_nycklar, inre_dictionaries in artistinfo.items():
    # print("yttre nyckel: ", yttre_nycklar)
    # print("inre dictionaries: ", inre_dictionaries)
    for inre_nycklar, listor in inre_dictionaries.items():
        # replace with Caps
        # print("Inre loopen, inre nycklar: ", inre_nycklar)
        # print("Inre loopen, listor: ", listor)
        print(inre_nycklar, ": ", " ".join(listor))
#alt
"""
print("Genres: ", artistinfo['genres'])
print("Members: ", artistinfo['member'])
print("Years active: ", artistinfo['years_active'])
"""
print("------------------")




