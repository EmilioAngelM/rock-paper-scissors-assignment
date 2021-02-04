#game.py



import random

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")


#asking user for input




user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

print(user_choice)

#I prefer using the string interpolation method
print(f"You chose: {user_choice}")


#simulating a computer input
computer_choice = "paper"

print(f"The computer chose: {computer_choice}")




options = ["rock","paper", "scissors"]
computer_choice = random.choice(options)





#simulating a computer input







exit()
#Determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")