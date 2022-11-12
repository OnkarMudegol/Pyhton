add = lambda a,b: a+b
sub = lambda a,b: a-b
prod = lambda a,b: a*b
quotient = lambda a,b: a/b 
remainder = lambda a,b: a%b
num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))
op = input("Enter a operator from the following list: +, -, /, %, *:")
op_list = ["+","-","/","*","%"]
if op in op_list:
    if op == "+":print("The sum is:",add(num1,num2))
    elif op == "-":print("The difference is:",sub(num1,num2))
    elif op == "*":print("The product is:",prod(num1,num2))
    elif op == "/":print("The quotient is:",quotient(num1,num2))
    elif op == "%":print("The remainder is:",remainder(num1,num2))
else:print("Invalid input. Please check input and try again.")