#to calculate simple interest with
#amount, interest rate and time as user input
amount = float(input("Enter the loan amount: "))
rate = float(input("Enter the annual interst rate: "))
time = float(input("Enter the time period(in yrs): "))
SI = (amount*rate*time)/100
print("The simple interest is: ",SI)