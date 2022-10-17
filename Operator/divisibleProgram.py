#to check if the given number is divisible by a number
number = float(input("Number to check divisibility:"))
divisor = float(input("Numbert to check dividsibility by:"))
if number%divisor == 0:
    print("The number",number,"is divisible by",divisor)
else:print("The number",number,"is not divisible by",divisor)
