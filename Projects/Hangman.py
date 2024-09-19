# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Hangman Game 

# NOTE: In this game, the player will try to guess the letters of a secret word.
#       They will get a certain number of chances to guess wrong before they lose.
# ==============================================================================

import random

# List of possible words for the game
word_list = ["python", "blue", "marble", "academy", "computer", "robot", "apple"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word (with guessed letters shown)
def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "  # Show guessed letters
        else:
            display += "_ "  # Show blanks for unguessed letters
    print(display.strip())

# Function to get the player's guess
def get_guess():
    guess = input("Guess a letter: ").lower()
    while not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please guess a single letter.")
        guess = input("Guess a letter: ").lower()
    return guess

# Function to check if the player has won (guessed all letters)
def check_win(secret_word, guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True

# Main function to play the game
def play_hangman():
    print("Welcome to Hangman!")
    
    # Choose a random secret word for the game
    secret_word = choose_word()
    guessed_letters = []  # List of correctly guessed letters
    wrong_guesses = 0  # Count of wrong guesses
    max_wrong_guesses = 6  # Maximum wrong guesses before the player loses
    
    # Game loop: continue until player wins or runs out of guesses
    while wrong_guesses < max_wrong_guesses:
        display_word(secret_word, guessed_letters)
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
        
        # Get the player's guess
        guess = get_guess()
        
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1
        
        # Check if the player has won
        if check_win(secret_word, guessed_letters):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
    else:
        print(f"Out of guesses! The word was: {secret_word}")

# Start the game
play_hangman()
