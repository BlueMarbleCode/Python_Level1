# ==============================================================================
# The Blue Marble Academy
# Beginner Python Program
# Working with Lists

# NOTE: Lists are like collections or groups where we can store multiple values.
#       For example, you could have a list of your favorite ice cream flavors
#
#       You can add, remove, and organize things in your list!
# ==============================================================================

# Let's start by making a list of fruits
fruits = ["apple", "banana", "cherry"]

# len() gives us the length of the list 
print(len(fruits)) 

# INDEXING
# In a list each item has its place.
# You can access items by their position (called an index).
# In Python, indexing starts at 0. So, "apple" is at position 0.
print(fruits[0])  
print(fruits[1]) 
print(fruits[2])  

# Create your own list with 5 items.

# print the fifth item


# ==============================================================================
# APPENDING
# We can use .append() to add to the list.
fruits.append("orange")  # Adding "orange" to the end of the list
print(fruits) 

# Add a new item to your list using append().

# ==============================================================================
# EXTENDING
# We can also add multiple fruits at once with .extend().
new_fruits = ["grape", "pineapple"] # We have to make a new list of more fruits
fruits.extend(new_fruits)  
print(fruits)  

# Extend your list to include 2 more items.

# ==============================================================================
# INSERTING
# We can add an item anywhere in the list with .insert().
# Let's insert "kiwi" at position 2 (before "cherry")
# Remember index starts from 0
fruits.insert(2, "kiwi")
print(fruits)  

# Insert a item at the beginning of your list.

# ==============================================================================
# REMOVING
# We can remove items from the list with .remove().
fruits.remove("banana")
print(fruits)  

# Remove an item from the list.

# ==============================================================================
# SLICING
# We can take a part of the list, called slicing.
# Let's say we only want the first three fruits.
some_fruits = fruits[0:3]  # This gives us a new list with the first 3 items
print(some_fruits)  

# Slice your list to get the first two items and print them.


# ==============================================================================
# 2D LISTS
# Lists can also have lists inside them, like a list of lists.
# This is useful for organizing things in rows and columns, like a grid!
# Here's an example of a 2D list (a list of two lists of fruits):
fruit_grid = [["apple", "banana"], ["cherry", "orange"]]

# To access items in a 2D list, we use two indexes.
# The first index is for the list (row), the second is for the item (column).
print(fruit_grid[0][1])  
print(fruit_grid[1][0]) 

# Try creating a 2D list for your favorite foods by category (candy, veggies, etc.).

