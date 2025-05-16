def factorial(num1):
    n=1
    if num1<2:
        return 1
    else:
        return num1*factorial(num1-1)
    
    
num1=int(input("Enter the number:- "))
val=factorial(num1)

print(val)
    
