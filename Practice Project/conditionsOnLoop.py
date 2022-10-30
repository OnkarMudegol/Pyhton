#write a program to display only those numbers from a list that satisfy following condition
#Number must be dicisible by 5
#If the nuber is graeter than 150, then skip it and mve to next number
#If the number is greater than 500, stop the loop
# numbers=[12, 75, 150, 180, 145]
numbers=["12","75","150","180","145"]
for i in numbers: 
    n = int(i)
    if n > 150:
        continue
    elif n > 500:
        break
    elif n%5==0:
        print(i)

