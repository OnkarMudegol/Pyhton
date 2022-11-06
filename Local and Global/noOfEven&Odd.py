# you have a static list of 10 elements 
# (32,21,64,100,13)
# create a function to return no of odd and even numbers
list_numbers = [32,21,64,100,13]
def count(list_numbers):
    even_count=0
    odd_count=0
    for i in list_numbers:
        if i%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
    print("Total no. of even numbers:",even_count)
    print("Total no. of odd numbers:",odd_count)
count(list_numbers)