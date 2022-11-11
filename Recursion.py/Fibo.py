#fibonaci with recurrsion
num1 = 0
num2 = 1
series = [0,1]
n = 10
while n!=0:
    nxt_num = num1 + num2
    num1 = num2
    num2 = nxt_num
    n = n-1
    series.append(nxt_num)
print(series)