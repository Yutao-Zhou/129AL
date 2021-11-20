import math

print()

def primefactors(n): 
    while n % 2 == 0: 
        print (2), 
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            print (i), 
            n = n / i 
    if n > 2: 
        print (n) 

while True:
    instr = input("Please enter an integer: ")
    try:
        interger = int(instr)
        assert interger>0
    except ValueError:
            print("Your input was not a number, try again!")
    except AssertionError:
            print("Your input was not greater than 0, try again!")
    else:
        print()
        print("The primeFactors are: ")
        primefactors(interger)
        print()
        break