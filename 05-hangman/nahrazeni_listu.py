# Nahrazení pozice v listu
list = [ "h", "e", "l", "l", "o"]
list1 = ["_", "_", "_", "_", "_"]
pismeno = "l"
slovo = ""

for i in range(len(list)):
    if list[i] == pismeno:
        #print(i)
        list1[i] = pismeno

#Převod listu na string
for w in list1:
    slovo += w

#Vypsání slova velkými písmeny
print(slovo.upper())
