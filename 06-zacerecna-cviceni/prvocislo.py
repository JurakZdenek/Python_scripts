#Funkce pro zjištění zda je zadané číslo (int) prvočíslem - vrací True/False
def prime_number(number):
    result = True

    if number == 1:
        result = False
    else:
        for i in range(2, number):
            if number % i == 0:
                result = False
    return(result)