score = [12, 78457, 4689, 23673, 8645, 8965340, 24539, 53, 9873, 89]
#print(min(score))
#print(max(score))

maximum = 0
minimum = maximum

for max in score:
    if max > maximum:
        maximum = max

minimum = maximum
#pokud neznám maximální číslo v rozsahu, tak do minimum dosadím nějaké velké číslo jako 999999999999999 které bude určitě větší než hledané nejmenší číslo.

for min in score:
    if min < minimum:
        minimum = min

print(maximum)
print(minimum)
