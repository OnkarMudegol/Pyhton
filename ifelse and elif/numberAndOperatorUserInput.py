#take user input for first and second input
#take user input for operator
num1 = float(input("Enter num 1:"))
num2 = float(input("Enter num 2:"))
op =input("Enter the operator + - * % // :")
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="%":
    print(num1%num2)
elif op=="//":
    print(num1//num2)
else:print("Invalid operator")