
# Konkatenering (sammanfogning) av två strängar
str1 = "Hej"
str2 = "världen"
result = str1 + " " + str2
print(result)
# Resultat: "Hej världen


#Längd på en sträng

str1 = "Hej"
str2 = "världen"
result = str1 + " " + str2
print("Längden på en sträng är: ", len(result))

#Escape sekvenser \

letters = "ABC"
i = 0
while i < len(letters):
    print(letters[i])
    i += 1

letters = "ABC"
for i in letters:
    print(i)