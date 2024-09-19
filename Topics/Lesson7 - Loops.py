# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Working with For Loops and While Loops

# NOTE: Loops let us repeat something again and again. They are super useful
#       when we want to do the same thing multiple times, like counting, or going
#       through a list of items one by one.

# ==============================================================================
# FOR LOOPS
# A for loop is used to repeat something for each item in a list or a sequence.
# It loops through each item and does something with it.

for number in range(1, 6):
    print(number)  
    
# The range(1, 6) creates numbers from 1 to 5. The loop goes through each number
# one at a time and prints it.


# Example: Looping through a list of animals
animals = ["cat", "dog", "rabbit", "parrot"]

for animal in animals:
    print(animal)  # This will print each animal name in the list.

# The loop goes through each item in the animals list and prints it.

# Example: Looping through each letter in a word
word = "BlueMarble"

for letter in word:
    print(letter)  # This will print each letter in "BlueMarble" one by one.

# 1. Write a for loop that prints the numbers from 10 to 15.
# 2. Write a for loop that prints each fruit in a list: ["apple", "banana", "cherry"].
# 3. Create a for loop that prints every letter in the word "Python".

# ==============================================================================
# WHILE LOOPS
# A while loop keeps repeating as long as a condition is true.
# Be careful! You need to make sure the condition will eventually become false,
# otherwise, the loop will run forever!

# Example: Counting from 1 to 5 using a while loop
count = 1

while count <= 5:
    print(count)
    count += 1  # This makes the count go up by 1 each time the loop runs.

# The loop keeps running while count is less than or equal to 5. After each loop,
# the count gets bigger by 1, until it reaches 5.


# Example: Asking the user for input until they say "stop"
user_input = ""

while user_input != "stop":
    user_input = input("Type 'stop' to end the loop: ")

print("You ended the loop!")

# The loop keeps running until the user types "stop".


# 1. Write a while loop that counts from 1 to 10.
# 2. Write a while loop that keeps asking the user to guess a secret number until they get it right.
# 3. Create a while loop that keeps printing "Hello!" until a counter reaches 5.

# ==============================================================================
# Combine a for loop and a while loop in one program. Example: Use a while loop to ask the user
# how many times they want to print something, then use a for loop to print it that many times.