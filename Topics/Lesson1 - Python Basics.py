# ============================================================================== 
# The Blue Marble Academy
# Beginner Python Program
# Lesson 1: Python Basics 
# ==============================================================================
# 1. Input() and print()

# input() is used to get user input. NOTE: The user is the person interacting with the program! 
# print() is used to display output to the user.

# Example:
input("Enter your name: ")  # Python will wait for the user to enter their name.
print("Hello") # Print hello

# a) Write a program that asks for the user's favorite video or board game.
# b) Print your favourite video or board game.

# ============================================================
# 2. Data Types (Integer, String, Float, Boolean)

# Variables are names that hold values. You can use them to store information.
# To create a variable: variable_name = value

# Data types tell us what kind of value a variable holds. 
# Here are the four basic types:

# Integer: Whole numbers, e.g., 1, 2, 3, 4,
# String: Text, e.g., "Hello"
# Float: Decimal numbers, e.g., 3.14
# Boolean: True or False values

# Example:
integer_number = 10  # The variable integer_number stores the integer value 10
string_text = "Hello, World!"  # The variable string_text stores the string value Hello, World
float_number = 3.14  # The variable float_number stores the float value 3.14
boolean_value = True  # The variable boolean_value stores the boolean value True

# We can also print variables 
print(integer_number)  
print(string_text)  
print(float_number)  
print(boolean_value)

# Create variables of each of four data types and print them.

# ============================================================
# 3. Operations on Numbers

# You can use Python to perform math operations on numbers. Here are some examples:

# Example:
a = 10
b = 5

# Addition
print(a + b)  # Output: 15

# Subtraction
print(a - b)  # Output: 5

# Multiplication
c = a * b # Multiply and then store the result in variable c
print(c)  # Output: 50

# Division
print(a / b)  # Output: 2.0

# a) Write a program that takes two numbers as input and prints their sum.
# b) Calculate the area of a rectangle with length 8 and width 6 using multiplication.

# ============================================================
# 4. Concatenating and Multiplying Strings

# You can combine strings (concatenation) or repeat them (multiplication).

# Example:
string1 = "Hello"
string2 = "World"

# Concatenation
print(string1 + " " + string2)  # Output: Hello World

# Multiplication
print(string1 * 3)  # Output: HelloHelloHello

# Write a program that asks the user for their first name and last name, then prints their full name.

# ============================================================
# 5. Variable Naming Conventions

# ALl variable names should be descriptive and follow these rules:
# - Start with a letter or underscore (_)
# - Followed by letters, numbers, or underscores
# - No spaces or special characters

# Example:
valid_name = "Alice"
age_of_person = 20
is_student = True

# Invalid names (will cause errors):
# 1st_variable = 30  # Cannot start with a number
# my-variable = 40    # Hyphens are not allowed
# my variable = 50    # Spaces are not allowed

# Can you identify the valid variable names?
# variable = 1
# variable2 = 2
# variable-3 = 3
# variable 4 = 4
