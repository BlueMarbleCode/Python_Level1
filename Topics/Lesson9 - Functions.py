# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Functions

# NOTE: most things written as functions can be written as normal lines of code
# but are much more clunky and disorganized

# ==============================================================================
# Creating a Function
# We use the 'def' keyword to define (create) a function. A function can have a
# name and can take input (called parameters). It can also return a result.

# Example: A simple function that says hello

def say_hello():
    print("Hello!")
    
# To use (or call) the function, we just write the function name:
say_hello()  

# ==============================================================================
# Function with Parameters
# Functions can take input, so we can use that input inside the function.

# Example: A function that takes a name and says hello to that person.

def greet(name):
    print(f"Hello, {name}!")

# Calling the function with a specific name
greet("Alice") 
greet("Bob")   

def greet2(name="Pam"): # default value
    print(f"Hello, {name}!")

def repeat_word(word, times):
    for i in range(times):
        print(word)

# Call the function to print "Python" 5 times
repeat_word("Python", 5)

# ==============================================================================
# Function with Return Value
# Sometimes we want the function to give back (return) a result.

# Example: A function that adds two numbers together and returns the result.

def add_numbers(a, b):
    return a + b  # This adds 'a' and 'b' and returns the result

# We can store the result of the function in a variable
sum_result = add_numbers(3, 5)
print(f"The sum is: {sum_result}")  


# ==============================================================================
# Write a function called 'double_number' that takes a number as input,
#    doubles it, and returns the result.


# Write a function called 'greet_person' that takes a name and a greeting word
#    (like "Hello" or "Hi") and prints the greeting followed by the person's name.

# Write a function called 'count_down' that takes a number and prints a
#    countdown from that number to 1.
