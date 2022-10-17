#A company decided to give bonus of 1000Rs to
#employee if his/her service is more than 5 years
#Ask user their salary and year of service and print
#the net bonus amount
yearsofservice=float(input("How many years of service have you provided to this company? "))
currentslary=float(input("What is your current income? "))
if yearsofservice > 5:

    print("Your net bonus salary is", currentslary+10000)

else:
    print("Your net bonus salary is", currentslary)