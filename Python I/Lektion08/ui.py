
#Jag använder denna variabel i funktionerna och den måste sparas
# i modulen, annars funkar inte koden.
bredd = 32

#Definition av funktioner, dessa sparas som modul ui
def line(value):
  if value:
    print("*" * bredd)
  else:
    print("-" * bredd)

def header(exempel):
    print("|",exempel.center(bredd), "|")

def echo(text):
    print(text)

def prompt(val):
    print(f"| Val > {val}")