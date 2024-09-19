# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Working with Dictionaries, Sets

# NOTE: These are different types of collections in Python, each used in its own way.
#
# 1. Dictionaries are like a real dictionary: words and their meanings.
# 2. Sets are like a collection of unique things with no order.

# ==============================================================================
# DICTIONARIES
# A dictionary is made up of key-value pairs. It's like having a list where each
# item has a name (key) and a description (value).

favorite_animals = {
    "Alice": "Cat",
    "Bob": "Dog",
    "Charlie": "Parrot"
}

# Accessing a value by its key:
print(favorite_animals["Alice"])  

# Adding a new key-value pair:
favorite_animals["David"] = "Horse"
print(favorite_animals)  # This will print the updated dictionary with David's favorite animal.

# Changing a value:
favorite_animals["Bob"] = "Rabbit"
print(favorite_animals)  # Bob's favorite animal is now Rabbit instead of Dog.

# Removing a key-value pair:
del favorite_animals["Charlie"]
print(favorite_animals)  

# Practice: Create your own dictionary 


# ==============================================================================
# SETS
# A set is like a collection of unique things. There are no duplicates, and the items
# don’t follow any order. Sets are useful when we only care about having each thing once.

favorite_colors = {"red", "blue", "green", "blue"}  # Notice "blue" is repeated.

# Even though "blue" is listed twice, it only appears once in the set!
print(favorite_colors)  # This will print: {'red', 'blue', 'green'}

# Adding an item to the set:
favorite_colors.add("yellow")
print(favorite_colors)  # This will print: {'red', 'blue', 'green', 'yellow'}

# Removing an item from the set:
favorite_colors.remove("green")
print(favorite_colors)  # This will print: {'red', 'blue', 'yellow'}

# Practice: Create your own set 

# ==============================================================================
# Checking if an item is in the set:
if "blue" in favorite_colors:   # You can also write a similar if for lists
    print("Blue is a favorite color!")
else:
    print("Blue is not a favorite color!")

# Create a list of 10 numbers and check if 55 is in the list