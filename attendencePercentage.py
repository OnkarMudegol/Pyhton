#calculate the attendence percentage of sem and tell if eligible for exam
classesAttended = float(input("How many clases have you attended?"))
attendencePercentage= (classesAttended/125)*100
if attendencePercentage > 75:
    print("Your attendence percentage is:", attendencePercentage, ",you are eligible for exams.")

else: print("Your attendence percentage is:", attendencePercentage, ",you are not eligible for exams.")
