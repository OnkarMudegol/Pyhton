numbers = [1,2,3,4,5,2,6]
#in the above list, find vaue 2, if it is present,
# replace it with 200, only update first occurance
numm = []
count = 0
for x in numbers:
    if x == 2 and count==0 :
        x = 200
        numm.append(x)
        count+=1
    else:numm.append(x)
print(numm)