#sum of digits of a two digit number

# two_digit_number = int(input("Enter a two digit number: ")) # ask for the input of 2 digit number 

# first_digit = two_digit_number // 10 # get the first digit by dividing by 10 and taking the integer value
# second_digit = two_digit_number % 10 # get the second digit by taking the remainder divided by 10

# sum_of_digits = first_digit + second_digit
# print(sum_of_digits)

# or

# two_digit_number = input("Enter a two digit number: ") # ask for the input of 2 digit number 

# digit_one = two_digit_number[0] # get the first digit by taking the first character of the string
# digit_two = two_digit_number[1] # get the second digit by taking the second character of the string

# print(int(digit_one) + int(digit_two)) # convert the string to integer and add them

# BMI CALCULATOR
# print("WELCOME TO THE BMI CALCULATOR")  # Print the welcome message

# try:
#     # Take input from the user and convert it to float
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in m: "))

#     # Calculate BMI using the formula: weight / (height^2)
#     bmi = float(weight / (height ** 2))

#     # Print the calculated BMI with two decimal places
#     print(f"Your Body Mass Index (BMI) is {bmi:.2f}")

#     # Classify the BMI according to standard ranges
#     if bmi <= 18.5:
#         print("You are UNDERWEIGHT")
#     elif 18.5 < bmi <= 25:
#         print("You are NORMAL")
#     elif 25 < bmi <= 30:
#         print("You are OVERWEIGHT")
#     elif 30 < bmi <= 35:
#         print("You are OBESE")
#     else:  # bmi > 35
#         print("You are CLINICALLY OBESE")

# except ValueError:
#     # Handle non-numeric input error
#     print("Invalid input. Please enter numeric values for weight and height.")

# total_bill  = float(input("Enter your total bill: "))
 
# no_of_people= int(input("enter the number of people: "))
# each_person = total_bill / no_of_people # calculate the amount each person has to pay
# print(f"each person has to pay {each_person}") # print the amount each person has to pay

# # tip_percentage = int(input("10%,12%,15%: "))

# if tip_percentage == 10:
#     tip_amount = tip_percentage * each_person / 100 
#     print(f"each person should pay a  tip amount of {tip_amount}")
#     total_amount = each_person + tip_amount
#     print(f"each person should pay a total amount of {total_amount}")

# elif tip_percentage == 12:
#     tip_amount = tip_percentage * each_person / 100
#     print(f"each person should pay a  tip amount of {tip_amount}")
#     total_amount = each_person + tip_amount
#     print(f"each person should pay a total amount of {total_amount}")

# elif tip_percentage == 15:
#     tip_amount = tip_percentage * each_person / 100
#     print(f"each person should pay a  tip amount of {tip_amount}")
#     total_amount = each_person + tip_amount
#     print(f"each person should pay a total amount of {total_amount}")

# else:
#     print("invalid tip percentage")
# print("WELCOME TO THE ROLLER COASTER")


# try:
#     # Ask the user to enter their age and convert it to an integer
#     age = int(input("Enter your age: "))
    
#     # Ask the user to enter their height and convert it to an integer
#     height = int(input("Enter your height in cm: "))
    
#     # Ask the user if they want a photo, and convert the response to uppercase
#     want_a_photo = input("Do you want a photo? (yes/no): ").upper()

#     # Initialize the total bill
#     total_bill = 0

#     # Check if the height is enough to ride the roller coaster
#     if height >= 120:
#         # Set ticket price based on age
#         if age >= 18:
#             total_bill = 15  # Adult ticket price
#         else:
#             total_bill = 7   # Child ticket price
        
#         # Add photo cost if user wants a photo
#         if want_a_photo == "YES":
#             total_bill += 3  # Extra cost for photo

#         # Display total bill
#         print(f"Your total bill is ${total_bill}")
        
#         # Confirm they can ride
#         print("You can ride the roller coaster")
#     else:
#         # If height is not enough
#         print("You cannot ride the roller coaster")

# # Handle the case when the user inputs a non-numeric value
# except ValueError:
#     print("Invalid input. Please enter numeric values for age and height.")

    
# LEAP YEAR FINDER
# try:
#     # Take input from the user and convert it to an integer
#     year = int(input("Enter a year: "))

#     # Check if the year is a leap year
#     if year % 4 == 0:
#         # If divisible by 4, check if it's a century year
#         if year % 100 == 0:
#             # If it's a century year, it must also be divisible by 400 to be a leap year
#             if year % 400 == 0:
#                 print(f"{year} is a leap year")
#             else:
#                 print(f"{year} is not a leap year")
#         else:
#             # Not a century year, but divisible by 4 — it's a leap year
#             print(f"{year} is a leap year")
#     else:
#         # Not divisible by 4 — not a leap year
#         print(f"{year} is not a leap year")

# except ValueError:
#     # Handle non-numeric input error
#     print("Invalid year. Please enter a valid number.")


 #PIZZA BILL SYSTEM

# print("WELCOME TO THE PIZZA BILL SYSTEM")

# print("MENU\nSmall pizza = $15\nMEdium pizza = $20\nLarge Pizza = $25 \nPepperoni for small pizza = $2\nPepperoni for medium and large pizza = $3\nExtra cheese for all pizzas = $1")

# print("WELCOME TO THE PIZZA BILL SYSTEM")

# print("MENU\nSmall pizza = $15\nMedium pizza = $20\nLarge Pizza = $25\nPepperoni for small pizza = $2\nPepperoni for medium and large pizza = $3\nExtra cheese for all pizzas = $1")

# print("WELCOME TO THE PIZZA BILL SYSTEM")

# print("MENU\nSmall pizza = $15\nMedium pizza = $20\nLarge Pizza = $25\nPepperoni for small pizza = $2\nPepperoni for medium and large pizza = $3\nExtra cheese for all pizzas = $1")

# try:
#     size = input("Enter the size of pizza you wish to order (S/M/L): ").upper()
#     add_pepperoni = input("Do you want to add pepperoni? (Y/N): ").upper()
#     extra_cheese = input("Do you want to add extra cheese? (Y/N): ").upper()

#     total_bill = 0

#     if size == "S":
#         total_bill = 15
#         if add_pepperoni == "Y":
#             total_bill += 2
#         if extra_cheese == "Y":
#             total_bill += 1
#         print(f"Your total bill is ${total_bill}")

#     elif size == "M" or size == "L":
#         if size == "M":
#             total_bill = 20
#         else:
#             total_bill = 25

#         if add_pepperoni == "Y":
#             total_bill += 3
#         if extra_cheese == "Y":
#             total_bill += 1

#         print(f"Your total bill is ${total_bill}")

#     else:
#         print("Invalid size. Please enter S, M, or L.")

# except ValueError:
#     print("Invalid input. Please enter a valid size (S/M/L) and Y/N for options.")


# LOVE CALCULATOR

# print("Welcome to the Love Calculator!")

# # Get input names
# name1 = input("Enter your name: ").lower()
# name2 = input("Enter their name: ").lower()

# # Combine names
# combined_names = name1 + name2

# # Count letters in "TRUE"
# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# true_score = t + r + u + e

# # Count letters in "LOVE"
# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e2 = combined_names.count("e")
# love_score = l + o + v + e2

# # Combine to make final score
# final_score = int(str(true_score) + str(love_score))

# # Output result
# if final_score < 10 or final_score > 90:
#     print(f"Your score is {final_score}, you go together like coke and mentos ❤️.")
# elif 40 <= final_score <= 50:
#     print(f"Your score is {final_score}, you are alright together 💛.")
# else:
#     print(f"Your score is {final_score}.")


# def treasure_island_game():
#     """
#     This function implements the Treasure Island game based on a flowchart.
#     The game guides the player through a series of choices, and the outcome
#     depends on the path they choose.  The game ends in either success
#     (finding the treasure) or failure (game over).
#     The function now includes a loop that allows the player to try again.
#     """
#     play_again = True  # Initialize the play_again variable
#     while play_again:
#         print("Welcome to Treasure Island!")
#         print("Your mission is to find the treasure.")

#         # First choice: left or right
#         choice1 = input("You are at a crossroads. Do you want to go left or right? ").lower()
#         if choice1 == "right":
#             print("You fell into a hole. Game Over.")
#         elif choice1 != "left":
#             print("Invalid input. Game Over.")
#         else:
#             # Second choice: swim or wait
#             choice2 = input("You've come to a lake. Do you want to swim or wait for a boat? ").lower()
#             if choice2 == "swim":
#                 print("You were attacked by trout. Game Over.")
#             elif choice2 != "wait":
#                 print("Invalid input. Game Over.")
#             else:
#                 # Third choice: which door
#                 choice3 = input(
#                     "You arrive at three doors. Which door do you choose? Red, Blue, or Yellow? "
#                 ).lower()
#                 if choice3 == "red":
#                     print("You were burned by fire. Game Over.")
#                 elif choice3 == "blue":
#                     print("You were eaten by beasts. Game Over.")
#                 elif choice3 == "yellow":
#                     print("You found the treasure! You Win!")
#                 else:
#                     print("Game Over.")
                    
#         # Ask the player if they want to play again
#         play_again_input = input("Do you want to play again? (yes/no) ").lower()
#         if play_again_input != "yes":
#             play_again = False  # Set play_again to False to exit the loop
#             print("Thanks for playing!")

# if __name__ == "__main__":
#     treasure_island_game()  # Start the game

#STONE PAPER SIZZER
# print("WELCOME TO THE STONE PAPER SCISSOR GAME")

# try:
#     import random  # Importing random module

#     play_again = True  # Boolean flag to control the loop

#     your_point = 0  # Initialize user points
#     computer_point = 0  # Initialize computer points

#     while play_again:

#         # Define the valid choices
#         choices = ["stone", "paper", "scissor"]

#         # Take user's choice
#         your_choice = input("Enter your choice (stone/paper/scissor): ").lower()

#         # Generate computer's choice randomly
#         computer_choice = random.choice(choices)
#         print("Computer choice: ", computer_choice)

#         # Check for tie
#         if your_choice == computer_choice:
#             print("It's a tie!")
#             your_point += 1
#             computer_point += 1

#         # Check all winning conditions for the user
#         elif your_choice == "stone" and computer_choice == "scissor":
#             print("You win!")
#             your_point += 1

#         elif your_choice == "paper" and computer_choice == "stone":
#             print("You win!")
#             your_point += 1

#         elif your_choice == "scissor" and computer_choice == "paper":
#             print("You win!")
#             your_point += 1

#         # If none of the above, user loses
#         else:
#             print("You lose!")
#             computer_point += 1

#         # Show current points
#         print("Your point: ", your_point)
#         print("Computer point: ", computer_point)

#         # Ask user if they want to play again
#         play_again_input = input("Do you want to play again? (yes/no): ").lower()

#         if play_again_input != "yes":
#             play_again = False  # Exit the loop
#             print("Thanks for playing!")

# # Handle invalid input error
# except ValueError:
#     print("Invalid input. Please enter a valid choice (stone/paper/scissor).")


    
# import random
# c = ("heads" , "tails")
# v = random.choice(c)
# print(v)

# which number is greatest

# nums = input("Enter two 2-digit numbers separated by a space: ")
# num1_str, num2_str = nums.split()

# num1 = int(num1_str)
# num2 = int(num2_str)

# if num1 > num2:
#     print("First number is greater")
# elif num2 > num1:
#     print("Second number is greater")
# else:
#     print("Both numbers are equal")