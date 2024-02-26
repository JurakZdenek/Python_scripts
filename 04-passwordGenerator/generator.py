import random

#použité znaky
uppers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specials = ["!", "*", "(", ")", "@"]

#délka hesla
pass_length = int(input("Zadej požadovanou délku hesla (5-2048):\n"))
#nebudeme generovat heslo menší než 5 znaků a větší než 2048
if pass_length < 5: pass_length = 5
if pass_length > 2048: pass_length = 2048
#počet velkých písmen
count_uppers = round(pass_length * 0.19)
#počet čísel
count_numbers = round(pass_length * 0.19)
#počet speciálních znaků
count_specials = round(pass_length * 0.1)
#zbytek jsou malá písmena
count_lowers = pass_length - count_uppers - count_numbers - count_specials

#Generování náhodného hesla postupně dle krytérií výše
password = ""
for i in range(count_uppers):
    password += random.choice(uppers)

for i in range(count_numbers):
    password += random.choice(numbers)

for i in range(count_specials):
    password += random.choice(specials)

for i in range(count_lowers):
    password += random.choice(lowers)

#převedení stringu na list
password_list = list(password)
#náhodné rozházení pořadí položek v listu - čili pořadí znaků v hesle
password_list = random.sample(password_list, pass_length)

#převedení listu na string
final_password = ""
for i in password_list:
    final_password += i



print("")
print("--------------------------- YOUR PASSWORD ---------------------------")
print(final_password)
print("---------------------------------------------------------------------")    
print("")