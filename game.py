#game.py


import os
import random

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")


print("-------------------")
print(f"Welcome '{PLAYER_NAME}' to my Rock-Paper-Scissors game...")
print("-------------------")


#asking user for input




user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

print(user_choice)

#I prefer using the string interpolation method
print(f"You chose: {user_choice}")







options = ["rock","paper", "scissors"]


#validate the user selection
#stop the program and not try to determine a winned is the user choice is invalid


if user_choice not in options:
    print("OOPS, wrong option. Please choose a valid option!")
    exit()






#simulating a computer input

computer_choice = random.choice(options)
print(f"The computer chose: {computer_choice}")


#Determining who won
#Adapted from solution shared by William Perrone in class

if user_choice == computer_choice:
    print("It is a tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Great Job! You WON")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Oh, better luck next time. The computer won")
elif user_choice == "rock" and computer_choice == "paper":
    print("Oh, better luck next time. The computer won")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Great Job! You WON")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Great Job! You WON")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Oh, better luck next time. The computer won")







print("Thank you for playing! Please play again!")
