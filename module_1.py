def task2(num1,choice):
    import math
    choice=choice.lower()
    if choice=="sq":
        result=math.sqrt(num1)
    elif choice=="l":
        result=math.log(num1)
    elif choice=="s":
        result=math.sin(num1)
    else:
        result="Wrong choice"
    return(result)

num1=int(input("Enter the number to take square root:- "))
choice=input("Enter your choice(Sq- for Square root, L- For Log, S- For sign) ")
result=task2(num1,choice)
print(result)
