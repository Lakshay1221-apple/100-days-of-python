# #In this code, we create a turtle graphics program that allows the user to control a turtle using keyboard inputs.
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# tim.speed("fastest")
# tim.color("blue")
# tim.shape("turtle")
#
# def move_up():
#     tim.setheading(90)
#     tim.forward(10)
#
#
# def move_down():
#     tim.setheading(270)
#     tim.forward(10)
#
#
# def move_left():
#     tim.setheading(180)
#     tim.forward(10)
#
#
# def move_right():
#     tim.setheading(0)
#     tim.forward(10)
#
# def draw_square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)
#
# def pen_up():
#     tim.penup()
#
# def pen_down():
#     tim.pendown()
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# def draw_circle():
#     tim.circle(50)
#
# def draw_anti_circle():
#     tim.circle(-50)
#
# screen.listen()
# screen.onkey(move_up, " Up")
# screen.onkey(move_down, "Down")
# screen.onkey(move_left, "Left")
# screen.onkey(move_right, "Right")
# screen.onkey(draw_square, "S")
# screen.onkey(pen_up, "U")
# screen.onkey(pen_down, "D")
# screen.onkey(clear_screen, "C")
# screen.onkey(draw_circle, "O")
# screen.onkey(draw_anti_circle, "A")
#
# screen.mainloop()




