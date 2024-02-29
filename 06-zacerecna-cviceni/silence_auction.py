import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''

offers = {}
while_condition = 0
os.system("clear")
top_price = 0
winner = ""
stop_key = "stop" 

#print(logo)
print("Nabídněte cenu za obraz")

while while_condition == 0:
    print(logo)
    name = input("Vaše jméno\n")
    if name == stop_key:
        break
    offer = int(input("Vaše nabídka\n"))
    offers[name] = offer
    os.system("clear")

for key in offers:
    if offers[key] > top_price:
        top_price = offers[key]
        winner = key

print(f"Vítězem je {winner} s nabídkou {top_price} Kč")