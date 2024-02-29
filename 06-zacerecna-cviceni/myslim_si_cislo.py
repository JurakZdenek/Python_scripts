import random
import os

os.system("clear")
hrajeme = ""

while hrajeme != "n":
    os.system("clear")
    min = 1
    max = 100
    random_number = random.randint (min, max)

    print(f"\n\nMyslím si číslo od {min} do {max}\n\n")

    pokusy = int(input("Kolik chceš pokusů na uhádnutí?\n"))
    # level = input("Obtížnost: (easy / hard)\n")
    # if level == "easy": 
    #     pokusy = 10 
    #     print(f"Zvolili jste easy, máš tedy {pokusy} pokusů")
    # else:
    #     pokusy = 5
    #     print(f"Zvolili jste hard, máš tedy {pokusy} pokusů")

    sel_num = int(input(f"\n\nZadej číslo({pokusy}):\n"))

    while sel_num != random_number:
        if sel_num < random_number:
            print("Větší")
        elif sel_num > random_number:
            print("Menší")
        pokusy -= 1
        if pokusy == 0: break
        sel_num = int(input(f"\nZadej číslo({pokusy}):\n"))
    if sel_num == random_number: print("\nGratuluji, vyhrál si!")
    else: print(f"\nGAME OVER, číslo bylo {random_number}")
    hrajeme = input("\nHraješ znovu? (a/n):\n")
