import json

heltal_minne = []
#skapa textfil som ska öppnas varje gång
f = open("heltal.json.txt", "r")
heltal_minne = json.dumps(heltal_minne)
f.write(heltal_minne)



#no se puede leer algo q no esta, primero hay que crearlo con write
f = open("heltal.json.txt", "a")
heltal_minne = json.loads(heltal_minne)
f.read()
print(heltal_minne)
for i in heltal_minne:
    print(i)

f.close()




