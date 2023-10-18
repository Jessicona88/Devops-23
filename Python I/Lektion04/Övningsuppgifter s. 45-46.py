#8.2 Övningsuppgifter

#8.2
todos = [
'Städa',
'Handla',
'Plugga',
'Ge␣blod'
]
'''
# 8.1
print(todos[0])
print(todos[2])
print(todos[1])

#8.2
print(todos)
attGöra = input("Lägga till ny aktivitet: ")
todos.append(attGöra)
print(todos)

# 8.3
print(todos)
gjort = int(input("Ta bort aktivitet via index: "))
del todos[gjort]
print(todos)

# 8.4
print(todos)
gjort = input("Ta bort aktivitet via värde: ")
todos.remove(gjort)
print(todos)

# 8.5
print(todos)
attGöra = input("Lägga till ny aktivitet: ")
todos.append(attGöra)
todos.sort()
print(todos)
'''
# 8.6
print(todos)
göra = input("Aktivitet: ")
if göra in todos:
    print("Aktiviteten finns redan på listan.")
else:
    add = input("Vill du lägga till den? J/N: ")
    if add == "ja" or "Ja" or "J" or "j":
        todos.append(göra)
        print("Aktivitet tillagd!")
        print(todos)


