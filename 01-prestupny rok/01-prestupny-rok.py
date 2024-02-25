print("Program pro zjištění přestupného roku")
rok = int(input("Zadejte rok:\n"))

ctyrkou = False
stovkou = False
ctyrstovkou = False

if rok % 4 == 0:
    ctyrkou = True

if rok % 100 == 0:
    stovkou = True

if rok % 400 == 0:
    ctyrstovkou = True

if (ctyrkou == True and stovkou == False) or (ctyrkou == True and stovkou == True and ctyrstovkou == True):
    print(f"Rok {rok} je přestupný")
else:
    print(f"Rok {rok} není přestupný")