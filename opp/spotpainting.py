import  turtle
import random
import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
    # print(rgb_colors)



# Create screen and turtle
screen = turtle.Screen()
screen.colormode(255)  # Use RGB color mode

tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# # Define a function to generate random RGB colors
# def random_color():
#     r = random.randint(0, 255)  # Random Red value
#     g = random.randint(0, 255)  # Random Green value
#     b = random.randint(0, 255)  # Random Blue value
#     return r, g, b
#
# # Set starting position
tim.setheading(225)  # Point diagonally down-left
tim.forward(300)
tim.setheading(0)    # Face right
#
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors)) # Draw a dot with random color
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)  # Turn upwards
        tim.forward(50)
        tim.setheading(180)  # Turn left
        tim.forward(500)
        tim.setheading(0)    # Face right again

screen.exitonclick()
