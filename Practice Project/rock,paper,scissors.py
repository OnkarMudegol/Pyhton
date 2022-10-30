#make rock, paper, scissor game
import random
user_choise = str(input("Enter rock, paper or scissor:"))
possible_choises = ["rock", "paper", "scissor"]
computer_choise = random.choice(possible_choises)
if user_choise not in possible_choises:
    print("Invaid input")
else:
    print("User choise:{}".format(user_choise))
    print("Computer choise:{}".format(computer_choise))     

if user_choise == computer_choise:
    print("Draw")
elif user_choise == "rock" and computer_choise == "paper":
    print("Computer wins")
elif user_choise == "rock" and computer_choise == "scissor":
    print("User wins")
elif user_choise == "paper" and computer_choise == "scissor":
    print("Computer wins")
elif user_choise == "paper" and computer_choise == "rock":
    print("User wins")     
elif user_choise == "scissor" and computer_choise == "rock":
    print("Computer wins")
elif user_choise == "scissor" and computer_choise == "paper":
    print("User wins")
