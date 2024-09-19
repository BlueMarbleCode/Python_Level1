# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Rock, Paper, Scissors Game Against the Computer 

# NOTE: In this game, the player will choose rock, paper, or scissors.
#       The computer will randomly pick one too, and then we'll see who wins!
# ==============================================================================

import random  # Importing the random module to let the computer pick randomly

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Welcome message
print("Welcome to Rock, Paper, Scissors!")

# Get player choice
player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Ensure player choice is valid
while player_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Computer randomly chooses rock, paper, or scissors
computer_choice = random.choice(choices)

# Show what the player and the computer chose
print(f"\nYou chose {player_choice}, and the computer chose {computer_choice}.")

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == "rock" and computer_choice == "scissors") or \
     (player_choice == "scissors" and computer_choice == "paper") or \
     (player_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("Computer wins!")

