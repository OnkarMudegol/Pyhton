#to figure out if input year is leap year or not
from re import I


year = float(input("Enter a year:"))
if year%100==0 and year%400==0:
    print("The year is a leap year.")
elif year%100 != 0 and year%4==0 :
    print("The year is a leap year.")
else: print("The year is not a leap year.")
