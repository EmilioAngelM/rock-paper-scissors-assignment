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



#simulating a computer input
options = ["rock","paper", "scissors"]
computer_choice = random.choice(options)





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







exit()
#Determining who won

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")