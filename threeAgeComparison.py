#take input of age from three people 
#dtermine the oldest and youngest
age1=float(input("Enter first person's age:"))
age2=float(input("Enter second person's age:"))
age3=float(input("Enter third person's age:"))
if age1 > age2 and age1 > age3:print("The oldest age is:", age1)
elif age2 > age1 and age2 > age3:print("The oldest age is:", age2)
elif age3 > age1 and age3 > age2:print("The oldest age is:", age3)

if age1 < age2 and age1 < age3:print("The youngest age is:", age1)
elif age2 < age1 and age2 < age3:print("The youngest age is:", age2)
elif age3 < age1 and age3 < age2:print("The youngest age is:", age3)

if age1 == age2:print("First two ages are same.")
elif age1 == age3:print("First and third age is equal.")
elif age2 == age3:print("Last two ages are equal.") 
else:print("All are of same age.")