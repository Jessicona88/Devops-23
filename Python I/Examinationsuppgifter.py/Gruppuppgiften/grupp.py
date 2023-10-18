#import utils

def meny(bredd):
    print(f"| {'Café Python'} |".center(bredd))
    print("*"*bredd)
    toprint = ""
    for x in range(1, len(lst_varor) + 1):
        if x % 3 != 0:
            toprint += f"│{lst_varor[x - 1]}".ljust(int(bredd/3))
        else:
            toprint += f"│{lst_varor[x - 1]}│\n".rjust(int(bredd/3))
    print(toprint)
    print("*" * bredd)
    print("-" * bredd)
    print("1 | Ny order")
    print("2 | Modifiera vara")
    print("3 | Lägg till vara")
    print("4 | Ta bort vara")
    print("5 | Sök order")
    print("-" * bredd)
    print("Ange val (1, 2, 3, 4, 5)")
    return input("> ")

while True:
    os.system("clear")
    val = meny(96)
    if val == "1":
        reg_items = register_items(lst_varor)
    elif val == "2":
        print("Modifiera vara här")
    elif val == "2":
        print("Modifiera vara här")
    elif val == "3":
        print("Lägg till vara")
    elif val == "4":
        print("Ta bort vara")
    elif val == "5":
        print("Sök order")
    else:
        print("Fel inmatning")