#Fizz Buzz - pokud je číslo dělitelné 3 = fizz, pokud 5 = buzz, pokud 3 a 5 = FizzBuzz

for i in range(1, 101):
    if (i % 5 == 0) and (i % 3 ==0):
        print("FizzBuzz") 
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)