import numpy as np
while True:
    de=(input ("Choose enter an angle in degrees: "))
    
    try:
        d=int(de)
       
    except ValueError:
            print("Your input was not a number, try again!")
    else:
        r=(d*3.14/180)
        break 

ne=input("Choose number of terms to sum: ")
while True:
    try:
        n=int(ne)
        assert n<=25      
    except ValueError:
        ne=input("Your input was not a number, try again: ")
    except AssertionError:
        ne=input("Your input is larger than 25, try again: ")
    else:
        break

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
f=2*n+1
fa=factorial(f)
def sind(d):
    sum=0
    for i in range(0,n+1):
        sum=sum+((-1)**(i))*((r**(2*i+1))/factorial(2*i+1))
    return sum    
print()
print("The sin from tayler series: ",sind(d))
print("The sin from sin function",np.sin(np.deg2rad(d)))
ratio=sind(d)/np.sin(np.deg2rad(d))
difference=abs(sind(d)-np.sin(np.deg2rad(d)))
print("The ratio is: ",ratio)
print("The absolute difference is: ", difference)