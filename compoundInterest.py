#to calculate compund interest with 
#amount, time and rate as user input
amt = float(input("Enter the loan amount: "))
time = float(input("Enter the time period of loan: "))
rate = float(input("Rate of Interest: "))
CI = amt*(1+rate/100)**time
print("The compund ineterest is: ",CI)
