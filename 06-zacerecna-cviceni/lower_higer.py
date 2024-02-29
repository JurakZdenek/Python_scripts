import random
import os

data = [
    {
        'name': 'Instagram',
        'follower_count': 501,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Facebook',
        'follower_count': 4,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 436,
        'description': 'Fotbalový hráč',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 161,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Harry Potter film',
        'follower_count': 8,
        'description': 'Film',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 307,
        'description': 'Podnikatelka',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 324,
        'description': 'Fotbalista',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 158,
        'description': 'Fotbalista',
        'country': 'Brazilie'
    },
    {
        'name': 'Eminem',
        'follower_count': 40,
        'description': 'Hudebník',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 193,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 111,
        'description': 'Herečka',
        'country': 'Francie'
    }
]

#Settings
data_len = len(data)
use_indexs = []
score = 0


#Funkcions
def index(list_len):
    """Popis funkce"""
    free = "no"
    while free == "no": 
        rand_index = random.randint(0, list_len - 1)
        if rand_index not in use_indexs:
            use_indexs.append(rand_index)
            break
        else:
            free == "yes"
    return rand_index

def info(index):
    """Popis druhé funkce"""
    print(f"{data[index]["name"]} - {data[index]["description"]} - {data[index]["country"]}")
    followers = data[index]["follower_count"]
    return followers

def compare(one, two):
    """ Popis třetí funkce"""
    if one > two:
        return a
    else:
        return b

    
# Samotný program
a = index(data_len)
b = index(data_len)

while data_len != len(use_indexs):
    os.system("clear")
    print("A:")
    a_followers = info(a)
    print(f"{a_followers}\n\n")

    print("B:")
    b_followers = info(b)
    print(f"{b_followers}\n\n")

    result = compare(a_followers, b_followers)

    print(f"Tvé skóre je {score}")
    choice = input("Kdo má více followers? a/b: ")
    if choice == "a": choice = a
    else: choice = b
    if choice == result:
        score += 1
        a = result
        b = index(data_len)
    else:
        print(f"\n\nBohužel špatně. Dosažené skóre {score}\n\n")
        break

os.system("clear")
if data_len == len(use_indexs): print(f"\n\nGRATULUJI VYHRÁL SI a tvé skóre je {score}\n\n")