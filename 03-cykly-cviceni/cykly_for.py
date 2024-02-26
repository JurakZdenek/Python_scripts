#pouziti s listem
list = [1, "Zdenek", 3.14, False]

for i in list:
    print(i)

#se stringem
str = "Zdenek"
for ch in str:
    print(ch)

#range pocet
for i in range(5):
    print(i)

#range od do
for i in range(10, 20):
    print(i)

#range s krokem po 5ti
for i in range(20, 40 , 5):
    print(i)

#sečti sudá čísla od 1 do 100 (2+4+6.....) = 2550
sum = 0
for i in range(2, 102, 2):
    #print(i)
    sum += i

print(sum)