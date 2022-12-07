num1=int(input("Enter The First numbers :"))
operator=input("Enter the operator(+,-,*,/,%)")
num2=int(input("Enter The second Number"))

if operator=="+":
    print(num1 + num2)
elif operator=="-":
    print(num1 - num2)
elif operator=="-":
    print(num1 / num2)
elif operator=="/":
    print(num1 / num2)
elif operator=="%":
    print(num1 % num2)
else:
    print("Invalid input")
