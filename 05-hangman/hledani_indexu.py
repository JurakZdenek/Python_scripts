# Hledani v listu a vypis jeho pozice, najde to každou pozici a číslo pozice (indexu) to vloží do listu "pozice"
list = [ "h", "e", "l", "l", "o"]
pozice = []
pismeno = "l"

for i in range(len(list)):
    if list[i] == pismeno:
        print(i)