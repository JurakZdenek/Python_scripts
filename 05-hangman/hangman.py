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
    ["stul", "pokládáme na to věci"]
]

pokusy = 0
random_list = random.choice(slova)
vybrane_slovo = random_list[0]
napoveda = random_list[1]
vybrany_list = list(vybrane_slovo)
delka_slova = len(vybrany_list)
pracovni_list = []

print("")
print(f"Nápověda k hledanému slovu zní: {napoveda}")
print("")

#naplneni listu "_"
for i in range(delka_slova):
    pracovni_list.append("_")

while vybrany_list != pracovni_list:
    zadane_pismeno = input("Zadej písmeno:\n").lower()
    pracovni_slovo = ""
    #vymena "_" za nalezene pismeno
    if zadane_pismeno in vybrany_list:
        for i in range(delka_slova):
            if vybrany_list[i] == zadane_pismeno:
                pracovni_list[i] = zadane_pismeno
        for i in pracovni_list:
            pracovni_slovo += i
        print(pracovni_slovo.upper())
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