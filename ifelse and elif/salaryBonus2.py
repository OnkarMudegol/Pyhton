#Company will give bonu based on following criteria
#Time Spent in Company   Bonus
#  >10 yrs                10%
#  <=6 yrs and >=10        8%
#  <6 yrs                  5%
employeeYears=float(input("Hoe many years have you worked with the company? "))
salary=float(input("Current Salary: "))

if employeeYears > 10 and employeeYears< 100:
    bonus=salary + (salary*0.1) 
    print("Your net bonus salary is:",bonus) 
elif employeeYears >= 6 and employeeYears <= 10:
    bonus=salary + (salary*0.08)
    print("Your net bonus salary is: ",bonus)
elif employeeYears < 6:
    bonus=salary+ (salary*0.05)
    print("Your net bonus salary is: ",bonus)
else:print("Invalid Input.")
