# Hra Hangman neboli šibenice
import random

obrazky = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print('''
 _
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
+--------------------------------------------+
|           Vítej ve hře Hangman.            |
|   Nepožívej diakritiku - háčky čárky.      |
+--------------------------------------------+
''')

winner = '''
██     ██ ██ ███    ██ ███    ██ ███████ ██████  
██     ██ ██ ████   ██ ████   ██ ██      ██   ██ 
██  █  ██ ██ ██ ██  ██ ██ ██  ██ █████   ██████  
██ ███ ██ ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
 ███ ███  ██ ██   ████ ██   ████ ███████ ██   ██ 
                                                 
'''

gameover = '''
 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                          
                                                                          '''

slova = [
    ["hrnek", "pijeme z toho"], 
    ["dvere", "zavíráme to"],
    ["police", "jsou na tom knihy"],
    ["lampa", "svití to"],
    ["okno", "veliké a nechceš to mýt"],
    ["stul", "pokládáme na to věci"],
    ["k", "je to kurva na 1"]
]

pokusy = 0
random_list = random.choice(slova)
vybrane_slovo = random_list[0]
napoveda = random_list[1]
vybrany_list = list(vybrane_slovo)
delka_slova = len(vybrany_list)
pracovni_list = []

pismeno_sklonovane = "písmen"

if delka_slova == 1:
    pismeno_sklonovane = "písmeno"
elif delka_slova <= 4:
    pismeno_sklonovane = "písmena"

print("")
print(f"Hledané slovo je na {delka_slova} {pismeno_sklonovane} a nápověda k němu zní: {napoveda}")
print("")

#naplneni listu "_"
for i in range(delka_slova):
    pracovni_list.append("_")

while vybrany_list != pracovni_list:
    pracovni_slovo = ""
    for i in pracovni_list:
            pracovni_slovo += f"{i} "
    print(pracovni_slovo.upper())
    zadane_pismeno = input("Zadej písmeno:\n").lower()
    #vymena "_" za nalezene pismeno
    if zadane_pismeno in vybrany_list:
        for i in range(delka_slova):
            if vybrany_list[i] == zadane_pismeno:
                pracovni_list[i] = zadane_pismeno
        
    else:
        print(obrazky[pokusy])
        pokusy += 1
        if pokusy == 7:
            print(f"Hledané slovo bylo: {vybrane_slovo.upper()}")
            print(gameover)
            break
        else:
            print(f"Špatně! Zbývající pokusy:{7-pokusy}")   

if vybrany_list == pracovni_list:
    print(f"Vyhrál si, hledané slovo bylo {vybrane_slovo.upper()}")
    print(winner)