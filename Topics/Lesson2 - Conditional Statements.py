# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Basic Example of Conditional statements

# NOTE: code is read from top to bottom
#
# NOTE: Indentation is important, the computer reads the code very mechanically,
#       we have to remember to take this into account when writing our codes!

# ==============================================================================
# these statements can be read in the following manner:
# 
# if the input age is less than or equal to 3,
#     then print You're so young, how are you typing these answers?
#
# otherwise, if the input age is greater than 3 and less than or equal to 12,
#     then print You're a cool kid
#
# otherwise, if the input age is greater than 12 and less than 20,
#     then print You're a cool teen, I bet

age = int(input('How old are you? (eg: 35): '))

# each conditional checks age by comparing it to specific numbers
if age <= 3: 
    print("You're so young, how are you typing these answers?")

elif age > 3 and age <= 12:
    print("You're a cool kid!")

elif age > 12 and age < 20:
    print("You're a cool teen, I bet!")

elif age >= 20 and age < 30:
    print("You're a young adult!")

# ==============================================================================
# Try to read/write the next conditional statement using the same logic

eye_color = input('Enter your eye color (eg: green): ')

# each conditional checks eye color by comparing it to specific strings
if eye_color == 'blue' and age == 22:
    print('Hey, same as the guy who wrote this code!')

elif eye_color == 'brown':
    print('brown! like coffee or chocolate!')

elif eye_color == 'blue': # this will not print if age is 22, due to an above clause
    print('blue! like the sea!' )

elif eye_color == 'green':
    print('green! like grass and leaves!')

else: # did I miss any colors? they'll all end up here!
    print(eye_color+', very cool!')

# ==============================================================================
# Practice: 
# Try to write a line of code that checks if the user is 30 or older and print a motivational or funny response!


# Try to write a new set of questions, maybe ask hair color, height etc.


# ==============================================================================
# You can also go crazy and have many ifs all together

# these statements can be read in the following manner:
# 
# if the weather is sunny,
#      if the temp is hot
#           then print Wear a t-shirt and shorts!
#      otherwise, if the temp is warm
#           then print Wear a light jacket!
# otherwise, 
#     It’s rainy. Don’t forget your umbrella!

weather = "sunny" # Test different values for weather

if weather == "sunny":
    temp = "hot"
    if temp == "hot":
        print("Wear a t-shirt and shorts!")
    elif temp == "warm":
        print("Wear a light jacket!")
else:
    print("It’s rainy. Don’t forget your umbrella!")
