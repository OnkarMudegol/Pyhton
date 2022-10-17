#elif is short for elseif
#Marks       #Grades
#A           100-90
#B           90-80
#C           80-70
#D           >70

marks = float(input("Enter your marks:"))
if marks > 90 and marks <= 100:print("Your grade is A.")
elif marks > 80 and marks <=90:print("Your grade is B")
elif marks >70 and marks <=80:print("Your grade is C")
elif marks <70:print("Your grade is D")
else:print("Not a valid score.Enter a number between 0-100.")