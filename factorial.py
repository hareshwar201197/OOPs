"""def factorial(num):
    fact=0
    if num<0:
        print("Negative number is not valid")
    elif num>0:
        print("Your factorial is ")
        for i in range(1,num+1):
           fact=fact*i
        print(fact)
    else:
        print("The factorial of 0 is 1")
        return fact"""


"""n=int(input("Enter the Possitive number :"))

fact=1
for i in range(1,n+1):
    
    fact=fact*i
    i=i-1
    print(fact)"""
#


i=int(input("Enter the possitive number : "))
fact=1
while(i>0):
    fact=fact*i
    i=i-1
    print("Factorial is =",fact)
