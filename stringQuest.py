#take a user input
#if the length of the string is more than 3 characters, add ing then return output
string = str(input("Enter a word:"))
a=len(string)
b=("ing")
if a>3:print(string+b)
else:print(string)