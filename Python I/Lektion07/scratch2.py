import requests
import json
"""
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)
response = json.loads(r.text)
localartist = {}
for x in response["artists"]:
    print(x["name"])
    localartist[x["name"]] = x["id"]
    print(localartist)

print("----------------------------")
indata = input("Select artist: ")
print("----------------------------")

a = requests.get(url + localartist[indata])
response = json.loads(a.text)
artist = response["artist"]

genres = f'{artist["genres"]}'.strip("[]")

genres = genres.replace("'", "")

members = f'{artist["members"]}'.strip("[]")

members = members.replace("'", "")


print(f'Name: {artist["name"]}')
print(f'Genres: {genres}')
print(f'Years active: {artist["years_active"][0]}')
print(f'Member: {members}')
print("----------------------------")
"""
spelaren = [(2, "Hjärter"), (3, "Ruter")]

for element in spelaren:
    if element == int:
        print(element)

valörer = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Knekt", "Dam", "Kung", "Ess"]
färger = ["Spader", "Hjärter", "Ruter", "Klöver"]


kortlek = []
for v in valörer:
    for f in färger:
        kort = v, f
        kortlek.append(list(kort))
print(kortlek)
print(type(kortlek))