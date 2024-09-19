import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")
screen.bgcolor("lightgreen")
screen.setup(width=800, height=600)

# Draw finish line
finish_line = turtle.Turtle(visible=False)
finish_line.penup()
finish_line.goto(300, 250)
finish_line.pendown()
finish_line.goto(300, -250)

# Create turtles
colors = ["red", "blue", "green", "orange", "purple"]
turtles = []
start_x = -300  # Starting x-coordinate for all turtles
start_y = 190   # Starting y-coordinate for the first turtle
spacing_y = 100  # Vertical spacing between turtles
for i, color in enumerate(colors):
    turtles.append(turtle.Turtle(shape="turtle"))
    turtles[i].color(color)
    turtles[i].penup()
    turtles[i].goto(start_x, start_y - i * spacing_y)
    turtles[i].pendown()

# Function to prompt user for turtle selection
def prompt_user_pick():
    while True:
        user_choice = screen.textinput("Pick a Winner", "Which turtle do you think will win? (red, blue, green, orange, purple)").lower()
        if user_choice in colors:
            return user_choice
        else:
            screen.textinput("Invalid Choice", f"Please choose one of: {', '.join(colors)}")

# Function to move turtles randomly with random speeds
def move_turtles(user_choice):
    while True:
        for turtle in turtles:
            speed = random.randint(1, 10)  # Generate a random speed for each turtle
            turtle.forward(speed)
            if turtle.xcor() >= 300:
                winner_color = turtle.color()[0]
                return winner_color

# Function to announce winner and handle play again
def announce_winner(winning_color, user_choice):
    if user_choice == winning_color:
        win_message = f"Congratulations! You picked the correct turtle. The {winning_color.capitalize()} turtle wins!"
    else:
        win_message = f"You picked the wrong turtle. The {winning_color.capitalize()} turtle wins."

    play_again = screen.textinput("Winner!", f"{win_message}\n\nDo you want to play again? (yes/no)").lower()
    if play_again == "yes":
        reset_race()
    else:
        screen.bye()

# Function to reset the race
def reset_race():
    for turtle, y_position in zip(turtles, range(start_y, start_y - len(colors) * spacing_y, -spacing_y)):
        turtle.goto(start_x, y_position)
        turtle.clear()

    screen.title("Turtle Racing Game")
    start_race()

# Function to start the race
def start_race():
    user_choice = prompt_user_pick()
    winning_color = move_turtles(user_choice)
    announce_winner(winning_color, user_choice)

# Start the race initially
start_race()

# Close the window on click
turtle.done()
