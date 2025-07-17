#SUM OF TWO DIGITS (TWP METHODS)

# ===== METHOD 1: Using Integer Division & Modulus =====
# two_digit_number = int(input("Enter a two digit number: "))  
# first_digit = two_digit_number // 10  
# second_digit = two_digit_number % 10  
# sum_of_digits = first_digit + second_digit
# print(sum_of_digits)

# # ===== METHOD 2: Using String Indexing =====
# two_digit_number = input("Enter a two digit number: ")  
# digit_one = two_digit_number[0]  
# digit_two = two_digit_number[1]  
# print(int(digit_one) + int(digit_two))  

# # BMI CALCULATOR

# print("WELCOME TO THE BMI CALCULATOR")  

# try:
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in m: "))
#     bmi = float(weight / (height ** 2))
#     print(f"Your Body Mass Index (BMI) is {bmi:.2f}")

#     if bmi <= 18.5:
#         print("You are UNDERWEIGHT")
#     elif 18.5 < bmi <= 25:
#         print("You are NORMAL")
#     elif 25 < bmi <= 30:
#         print("You are OVERWEIGHT")
#     elif 30 < bmi <= 35:
#         print("You are OBESE")
#     else:
#         print("You are CLINICALLY OBESE")

# except ValueError:
#     print("Invalid input. Please enter numeric values for weight and height.")


# # BILL SPLITTER WITH TIP

# total_bill = float(input("Enter your total bill: "))
# no_of_people = int(input("enter the number of people: "))
# each_person = total_bill / no_of_people  
# print(f"each person has to pay {each_person}")  

# tip_percentage = int(input("10%,12%,15%: "))  # Original input line (commented earlier)

# if tip_percentage == 10:
#     tip_amount = tip_percentage * each_person / 100 
#     print(f"each person should pay a tip amount of {tip_amount}")
#     total_amount = each_person + tip_amount
#     print(f"each person should pay a total amount of {total_amount}")
# elif tip_percentage == 12:
#     tip_amount = tip_percentage * each_person / 100
#     print(f"each person should pay a tip amount of {tip_amount}")
#     total_amount = each_person + tip_amount
#     print(f"each person should pay a total amount of {total_amount}")
# elif tip_percentage == 15:
#     tip_amount = tip_percentage * each_person / 100
#     print(f"each person should pay a tip amount of {tip_amount}")
#     total_amount = each_person + tip_amount
#     print(f"each person should pay a total amount of {total_amount}")
# else:
#     print("invalid tip percentage")


# # ROLLER COASTER RIDE

# print("WELCOME TO THE ROLLER COASTER")

# try:
#     age = int(input("Enter your age: "))
#     height = int(input("Enter your height in cm: "))
#     want_a_photo = input("Do you want a photo? (yes/no): ").upper()

#     total_bill = 0
#     if height >= 120:
#         if age >= 18:
#             total_bill = 15  
#         else:
#             total_bill = 7   
#         if want_a_photo == "YES":
#             total_bill += 3  
#         print(f"Your total bill is ${total_bill}")
#         print("You can ride the roller coaster")
#     else:
#         print("You cannot ride the roller coaster")

# except ValueError:
#     print("Invalid input. Please enter numeric values for age and height.")


# # LEAP YEAR FINDER

# try:
#     year = int(input("Enter a year: "))
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f"{year} is a leap year")
#             else:
#                 print(f"{year} is not a leap year")
#         else:
#             print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# except ValueError:
#     print("Invalid year. Please enter a valid number.")


 #PIZZA BILL SYSTEM


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
#     elif size == "M":
#         total_bill = 20
#         if add_pepperoni == "Y":
#             total_bill += 3
#         if extra_cheese == "Y":
#             total_bill += 1
#         print(f"Your total bill is ${total_bill}")
#     elif size == "L":
#         total_bill = 25
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
# name1 = input("Enter your name: ").lower()
# name2 = input("Enter their name: ").lower()
# combined_names = name1 + name2

# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# true_score = t + r + u + e

# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e2 = combined_names.count("e")
# love_score = l + o + v + e2

# final_score = int(str(true_score) + str(love_score))

# if final_score < 10 or final_score > 90:
    # print(f"Your score is {final_score}, you go together like coke and mentos ❤️.")
# elif 40 <= final_score <= 50:
#     print(f"Your score is {final_score}, you are alright together 💛.")
# else:
#     print(f"Your score is {final_score}.")


# TREASURE ISLAND GAME


# def treasure_island_game():
#     print("Welcome to Treasure Island!")
#     print("Your mission is to find the treasure.")

#     play_again = True
#     while play_again:
#         choice1 = input("Left or right? ").lower()
#         if choice1 == "right":
#             print("You fell into a hole. Game Over.")
#         elif choice1 != "left":
#             print("Invalid input. Game Over.")
#         else:
#             choice2 = input("Swim or wait? ").lower()
#             if choice2 == "swim":
#                 print("You were attacked by trout. Game Over.")
#             elif choice2 != "wait":
#                 print("Invalid input. Game Over.")
#             else:
#                 choice3 = input("Which door? Red, Blue, or Yellow? ").lower()
#                 if choice3 == "red":
#                     print("You were burned by fire. Game Over.")
#                 elif choice3 == "blue":
#                     print("You were eaten by beasts. Game Over.")
#                 elif choice3 == "yellow":
#                     print("You found the treasure! You Win!")
#                 else:
#                     print("Game Over.")
        
#         play_again_input = input("Play again? (yes/no): ").lower()
#         if play_again_input != "yes":
#             play_again = False
#             print("Thanks for playing!")

# treasure_island_game()


# Stone-Paper-Scissors Game


# try:
#     import random

#     play_again = True
#     your_point = 0
#     computer_point = 0

#     while play_again:
#         choices = ["stone", "paper", "scissor"]
#         your_choice = input("Enter your choice (stone/paper/scissor): ").lower()
#         computer_choice = random.choice(choices)
#         print("Computer choice: ", computer_choice)

#         if your_choice == computer_choice:
#             print("It's a tie!")
#             your_point += 1
#             computer_point += 1
#         elif your_choice == "stone" and computer_choice == "scissor":
#             print("You win!")
#             your_point += 1
#         elif your_choice == "paper" and computer_choice == "stone":
#             print("You win!")
#             your_point += 1
#         elif your_choice == "scissor" and computer_choice == "paper":
#             print("You win!")
#             your_point += 1
#         else:
#             print("You lose!")
#             computer_point += 1

#         print("Your point: ", your_point)
#         print("Computer point: ", computer_point)

#         play_again_input = input("Play again? (yes/no): ").lower()
#         if play_again_input != "yes":
#             play_again = False
#             print("Thanks for playing!")

# except ValueError:
#     print("Invalid input. Please enter a valid choice (stone/paper/scissor).")


# # HEADS OR TAILS

    
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


#FINDING THE MAX MARKS OF THE STUDENTS


# print("Max student Score")
# student_score = [78, 65, 89, 86, 55, ]
# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score  = score
# print(f"The highest score in the class is: {max_score}")



# #ADDING UP DIGITS FROM 1 TO 100


# print("Adding up digits from 1 to 100")
# total = 0
# for number in range(1, 101):
#     total += number
#     print(f"Adding {number} gives {total}")
# print(f"The total is of all the numbers from 1 to 100 is {total}")


# FizzBuzz Game


# print("Welcome to the Fizz Buzz Game 🥤🐝")

# total_BUZZ = 0
# total_FIZZ = 0
# total_FIZZBUZZ = 0
# no_FIZZBUZZ = 0

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"{number} FIZZBUZZ")
#         total_FIZZBUZZ += 1

#     elif number % 3 == 0:
#         print(f"{number} FIZZ")
#         total_FIZZ += 1

#     elif number % 5 == 0:
#         print(f"{number} BUZZ")
#         total_BUZZ += 1

#     else:
#         print(f"{number} is neither FIZZ nor BUZZ — no FIZZBUZZ in your luck! 😂")
#         no_FIZZBUZZ += 1  

# print("\n🎯 Game Summary:")
# print(f"Total FIZZ: {total_FIZZ}")
# print(f"Total BUZZ: {total_BUZZ}")
# print(f"Total no FIZZBUZZ: {no_FIZZBUZZ}")
# print(f"Total FIZZBUZZ: {total_FIZZBUZZ}")


# # PASSWORD GENERATOR

# import random
# import string

# def generate_passowrd():
#     print("Welcome to the Password Generator")

#     try:
#         # Ask user to specify password details
#         total_length = int(input("Enter the length of password you want: "))
#         num_letters = int(input("How many letters do you want? "))
#         num_numbers = int(input("How many numbers do you want? "))
#         num_specialcharc = int(input("How many special characters do you want? "))

#     except ValueError:
#         print("Please enter valid numbers.")
#         return

#     # Validate if the total components add up to the requested password length
#     if total_length != num_letters + num_numbers + num_specialcharc:
#         print("Total letters, special characters, and numbers do not match the length of the password.")
#         return

#     # Generate random letters, digits, and special characters based on user input
#     letters = random.choices(string.ascii_letters, k=num_letters)
#     numbers = random.choices(string.digits, k=num_numbers)
#     special = random.choices(string.punctuation, k=num_specialcharc)

#     # Calculate remaining characters to fill (only if needed — optional based on logic)
#     remaining = total_length - (num_letters + num_numbers + num_specialcharc)
#     all_charc = string.ascii_letters + string.digits + string.punctuation
#     filler = random.choices(all_charc, k=remaining)

#     # Combine all selected characters into one list
#     password_charc = letters + numbers + special + filler

#     # Shuffle the combined characters to randomize their order
#     random.shuffle(password_charc)

#     # Convert the list into a single string as the final password
#     password = ''.join(password_charc)

#     print(f"Your password has been generated: {password}")

# generate_passowrd()


# THE HANGMAN PROJECT 

# HANGMAN 1 ( WORD GUESSING GAME )


# import random

# print("Welcome to the Hangman Game!")

# # FOR GETTING A WORD-LIST OF INFINITE WORDS

# # Download a word list (e.g., from https://www.mit.edu/~ecprice/wordlist.10000)

# # Save it as words.txt in the same directory.

# # import random

# # def load_words():
# #     with open("words.txt", "r") as file:
# #         words = file.read().splitlines()
# #     return [word.lower() for word in words if len(word) >= 4]  # Filter short words if needed

# def hangman():
#     life = 3
#     word_list = ["python", "java", "javascript", "ruby", "swift"]
#     program_word = random.choice(word_list)

#     print(f"The word has {len(program_word)} letters.")
#     revealed_indices = [1, 2, 5]

#     marked_word = ""
#     for i in range(len(program_word)):
#         if i in revealed_indices and i < len(program_word):
#             marked_word += program_word[i] + " "
#         else:
#             marked_word += "_ "

#     print("Your word (some letters revealed):")
#     print(marked_word.strip())

#     while life > 0:
#         user_word = input("Enter your full word guess: ").lower()

#         if user_word == program_word:
#             print("🎉 Correct! You guessed the word!")
#             return
#         else:
#             life -= 1
#             print("❌ Wrong guess!")
#             print(f"Lives remaining: {life}")

#     print(f"💀 You lost! The correct word was '{program_word}'.")

# # Main game loop
# while True:
#     hangman()
#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again != "yes":
#         print("Thanks for playing! Good day!")
#         break



# HANGMAN 2 ( LETTER GUESSING GAME )


# import random

# def load_words():
#     return ["python", "java", "javascript", "ruby", "swift"]

# def hangman():
#     life = 3
#     word_list = load_words()
#     program_word = random.choice(word_list)
#     word_length = len(program_word)

#     # Reveal some letters at random
#     num_to_reveal = max(1, word_length // 3)
#     revealed_indices = random.sample(range(word_length), num_to_reveal)

#     word_display = []
#     revealed_letters = set()
#     player_guessed_letters = set()

#     for i in range(word_length):
#         if i in revealed_indices:
#             word_display.append(program_word[i])
#             revealed_letters.add(program_word[i])
#         else:
#             word_display.append("_")

#     print("\n🎮 Welcome to the Hangman Game!")
#     print(f"The word has {word_length} letters.")
#     print("Some letters are already revealed to help you!")
#     print("Word:", " ".join(word_display))

#     while life > 0 and "_" in word_display:
#         guess = input("Guess a letter: ").lower()

#         if not guess.isalpha() or len(guess) != 1:
#             print("⚠️ Please enter a single valid letter.")
#             continue

#         if guess in player_guessed_letters:
#             print("⏳ You've already guessed that letter.")
#             continue

#         player_guessed_letters.add(guess)

#         if guess in program_word:
#             print("✅ Correct guess!")
#             for idx, char in enumerate(program_word):
#                 if char == guess:
#                     word_display[idx] = guess
#         else:
#             life -= 1
#             print(f"❌ Wrong guess! Lives remaining: {life}")

#         print("Word:", " ".join(word_display))
#         print("Guessed letters:", ", ".join(sorted(player_guessed_letters)))

#     if "_" not in word_display:
#         print(f"\n🎉 You won! The word was: {program_word}")
#     else:
#         print(f"\n💀 You lost! The word was: {program_word}")

# # Main game loop
# while True:
#     hangman()
#     play_again = input("\nDo you want to play again? (yes/no): ").lower()
#     if play_again != "yes":
#         print("Thanks for playing! Goodbye!")
#         break


# PAINT THE WALL 
# import math

# def paint_the_wall():


#     print("Welcome to the Paint the Wall program!")
#     print("This program will help you to the calculate the amount of paint can needed to paint the wall taking into account that one can of paint covers 10 square meters of the wall assuming that one can of paint  containe 5 liters of paint.")

#     height = float(input("Enter the lenght of the wall in meters: "))
#     width = float(input("Enter the width of the wall in meters: "))

#     area = height * width
#     print(f"The area of the wall is {area} square meters.")

#     No_of_cans_needed = area // 10
#     total_cans = math.ceil(No_of_cans_needed)
#     print(f"You will need {total_cans} cans of paint to paint the wall.")


# paint_the_wall()


# PRIME NUMBER CHECKER 

# import math

# def prime_number_checker():
#     print("Welcome to the Prime Number Checker!\nThis program will help you determine if a number is prime or not.")

#     while True:
#         try:
#             Entered_number = int(input("Enter a number to check if it is prime: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")
#             continue  # Let user try again without quitting

#         if Entered_number < 2:
#             print(f"{Entered_number} is not a prime number.")
#         else:
#             for i in range(2, int(math.sqrt(Entered_number)) + 1):
#                 if Entered_number % i == 0:
#                     print(f"{Entered_number} is not a prime number.")
#                     break
#             else:
#                 print(f"{Entered_number} is a prime number.")

#         # Ask user if they want to check another number
#         run_again = input("Do you want to check another number? (yes/no): ").strip().lower()
#         if run_again != "yes":
#             print("Thanks for using the Prime Number Checker! Goodbye!")
#             break

# prime_number_checker()

# THE CAESAR CIPHER CODE 

# Logo Display (Caesar Cipher)

# import string

# import pyfiglet

# logo = pyfiglet.figlet_format("Caesar Cipher", font="starwars")
# print(logo)

# def Caesar_cipher():

#     while True:
#         print("\nWelcome to the Caesar Cipher Program!")
#         print("This program will help you to encrypt or decrypt a message using the Caesar cipher technique.")

#         alphabets = list(string.ascii_lowercase)
#         numbers = list(string.digits)

#         try:
#             direction = input("Type 'encode' to encrypt your message or 'decode' to decrypt your message: ").lower()
#             if direction not in ['encode', 'decode']:
#                 print("Invalid input. Please enter 'encode' or 'decode'.")
#                 continue

#             text = input("Enter your message: ").lower()
#             shift = int(input("Enter the shift number: "))

#             if shift < 0:
#                 print("Shift number cannot be negative. Please enter a positive shift number.")
#                 continue 

#             shift_alpha = shift % 26  # Normalize shift
#             shift_digit = shift % 10  # Normalize shift for digits

#             Cipher_text = ""

#             for char in text:
#                                                                #EXMAPLE                                                            
#                 if char in alphabets:                          #char = 'y', index = 24, shift = 3
#                                                                #Encoding:  (24 + 3) % 26 = 1 → 'b'
#                     index = alphabets.index(char)              #Decoding: (24 - 3) % 26 = 21 → 'v'          
#                     new_index = (index + shift_alpha) % 26 if direction == 'encode' else (index - shift_alpha) % 26
#                     Cipher_text += alphabets[new_index]               
                    

#                 elif char in numbers:
#                     index = numbers.index(char)
#                     new_index = (index + shift_digit) % 10 if direction == 'encode' else (index - shift_digit) % 10
#                     Cipher_text += numbers[new_index]

#                 else:
#                     Cipher_text += char
                

#             print(f"The {direction}d message is: {Cipher_text}")

#         except ValueError:
#             print("Invalid input. Please enter a valid shift number.")
#             continue

#         run_again = input("Do you want to run the program again? (yes/no): ").strip().lower()
#         if run_again != "yes":
#             print("Thanks for using the Caesar Cipher Program! Goodbye!")
#             break


# Caesar_cipher()


# Day 9 - Dictionaries , Nesting and The Secrete Auction Program

# The Secret Auction Program

# def secret_auction():

#     print("Welcome to the Secret Auction Program!")
#     print("This program will help you to conduct a secret auction.")

#     bids = {}

#     while True:
#         name = input("Enter the name of the bidder: ")

#         if name in bids:
#              print("This name has already been used. Please enter a different name.")
#              continue

#         try:
          
#           bid_amount = float(input("Enter the bid amount: $")) 
#         except ValueError:

#             print("Invalid input. Please enter a valid number for the bid amount.")
#             continue 

#         bids[name] = bid_amount 

#         another_bidder = input("Is there another bidder? (yes/no): ").strip().lower()
#         if another_bidder != "yes":
#             print("No more bidders. Ending the auction.")
#             break                      

#     if bids:
#         highest_bidder = max(bids, key=bids.get)
#         highest_bid = bids[highest_bidder]
#         print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid:.2f}.")

# while True:
#     secret_auction()

#     run_again = input("Do you want to run the program again? (yes/no): ").strip().lower()
#     if run_again != "yes":
#           print("Thanks for using the Secret Auction Program! Goodbye!")
#           break


# loops in dictionaries


# programming_languages = {
#     "python": "A language that lets you work quickly and integrate systems more effectively.",
#     "Java": "A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.",
#     "JavaScript": "A programming language that conforms to the ECMAScript specification, primarily",
#     "loops": ["While Loop", "For Loop", "Do While Loop"],
# } 
# for key in programming_languages:
#     print(key)         
#     print(programming_languages[key])



#  The Grading Criteria Program

# def grading_criteria():
#     print("Welcome to the grading criteria!")
#     print("This program will help you determine the grade based on the marks entered.")

#     students = {}

#     # Input phase
#     while True:
#         name = input("\nEnter the name of the student: ").strip()

#         if name in students:
#             print("This name has already been used. Please enter a different name.")
#             continue

#         try:
#             grade = int(input("Enter the marks of the student (0-100): "))
#             if not (0 <= grade <= 100):
#                 print("Invalid marks. Please enter a value between 0 and 100.")
#                 continue
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#             continue

#         students[name] = grade

#         # Strict validation for yes/no
#         while True:
#             another = input("Do you want to enter another student? (yes/no): ").strip().lower()
#             if another in ("yes", "no"):
#                 break
#             print("Invalid input. Please enter 'yes' or 'no'.")

#         if another == "no":
#             break

#     # Grade assignment
#     print("\n--- Grade Results ---")
#     for student, grade in students.items():
#         if grade >= 90:
#             letter = 'A'
#         elif grade >= 80:
#             letter = 'B'
#         elif grade >= 70:
#             letter = 'C'
#         elif grade >= 60:
#             letter = 'D'
#         elif grade >= 50:
#             letter = 'E'
#         else:
#             letter = 'F'

#         print(f"{student} has received grade {letter}.")

#     # Optional: Personal check
#     while True:
#         check = input("\nDo you want to check the marks of a specific student? (yes/no): ").strip().lower()

#         if check != 'yes' and check != "no":
#             print("Invalid input. Please enter 'yes' or 'no'.")
#             continue

#         if check == "no":
#             break

#         name_to_check = input("Enter the name of the student to check: ").strip()
#         if name_to_check in students:
#             print(f"{name_to_check} scored {students[name_to_check]} marks.")
#         else:
#             print("No such student found.")

# # Loop to run program multiple times
# while True:
#     grading_criteria()
#     again = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
#     if again != "yes":
#         print("Thanks for using the grading criteria program! Goodbye!")
#         break


# -------------------------------
# 📝 DIFFERENT METHODS OF NESTING DICTIONARIES
# -------------------------------

# ✅ 1. Simple Dictionary

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# ✅ 2. Nesting a List in a Dictionary

# travel_log_simple = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# ✅ 3. Nesting a Dictionary in a Dictionary

# travel_log_nested_dict = {
#     "Countries": {
#         "France": ["Paris", {"Friends": "India"}, {"Enemy": "Pakistan"}, "Lille", "Dijon"],
#         "Germany": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# }

# Adding a new country (Italy) to the nested dictionary

# travel_log_nested_dict["Countries"]["Italy"] = ["Rome", "Milan", "Venice"]

# Updating Germany's entry to include more details

# travel_log_nested_dict["Countries"]["Germany"] = {
#     "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "Friends": ["India"]
# }

# Counting the number of cities visited in Italy

# visit_count = len(travel_log_nested_dict["Countries"]["Italy"])

# Adding visit count to Italy's entry

# travel_log_nested_dict["Countries"]["Italy"] = {
#     "city_visited": travel_log_nested_dict["Countries"]["Italy"],
#     "visit_count": visit_count
# }

# Accessing and modifying France's entry

# cities_in_france = travel_log_nested_dict["Countries"]["France"]
# travel_log_nested_dict["Countries"]["France"] = {
#     "city_visited": cities_in_france
# }

#  ✅ Printing Nested Dictionary

# print("\n🌍 Travel Log (Nested Dictionary):")
# print(travel_log_nested_dict)


# -------------------------------
# ✅ 4. Mutating a Dictionary Using a Function
# -------------------------------

# List of dictionaries

# travels = [
#     {
#         "Country": "France",
#         "visits": 12,
#         "Cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "Country": "Germany",
#         "visits": 5,
#         "Cities": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]

# # Function to add a new country

# def add_new_country(country_visited, times_visited, cities_visited):
#     """
#     Adds a new country to the travels list.

#     Parameters:
#     country_visited (str): Name of the country.
#     times_visited (int): Number of times the country was visited.
#     cities_visited (list): List of cities visited in the country.
#     """
#     new_country = {
#         "Country": country_visited,
#         "visits": times_visited,
#         "Cities": cities_visited
#     }
#     travels.append(new_country)

# # Adding Italy
# add_new_country("Italy", 3, ["Rome", "Milan", "Venice"])

# # ✅ Printing Updated Travels List
# print("\n🗺️ Updated Travels List:")
# for country in travels:
#     print(country)

#---------------
# THE CALCULATOR
#---------------
# def calculator():
#     """A simple command-line calculator with previous result support."""
#     print("Welcome to the Calculator")
#     print("This program helps you perform basic arithmetic operations.")

#     operations = {
#         "1": ("Addition", "+"),
#         "2": ("Subtraction", "-"),
#         "3": ("Multiplication", "*"),
#         "4": ("Division", "/"),
#         "5": ("Remainder", "%"),
#         "6": ("Power of", "**"),
#         "7": ("Exit", None)
#     }

#     previous_result = None  # To store result of previous operation

#     while True:
#         print("\nAvailable operations:")
#         for key, (name, _) in operations.items():
#             print(f"{key}. {name}")

#         choice = input("Enter the choice (1-7) for the operation you want to use: ")

#         if choice == '7':
#             print("Thank you for using the calculator. Goodbye!")
#             break

#         if choice not in operations:
#             print("❌ Invalid choice. Please enter a number between 1 and 7.")
#             continue

#         try:
#             # Ask if user wants to use previous result or enter new inputs
#             if previous_result is not None:
#                 reuse = input("Do you want to use the previous result? (yes/no): ").strip().lower()
#                 if reuse == "yes":
#                     num1 = previous_result
#                     print(f"First number is set to previous result: {num1}")
#                 else:
#                     num1 = float(input("Enter the first number: "))
#             else:
#                 num1 = float(input("Enter the first number: "))

#             num2 = float(input("Enter the second number: "))

#         except ValueError:
#             print("❌ Invalid input. Please enter numeric values.")
#             continue

#         op_name, op_symbol = operations[choice]

#         try:
#             if choice == '1':
#                 result = num1 + num2
#             elif choice == '2':
#                 result = num1 - num2
#             elif choice == '3':
#                 result = num1 * num2
#             elif choice == '4':
#                 if num2 == 0:
#                     raise ZeroDivisionError("division by zero")
#                 result = num1 / num2
#             elif choice == '5':
#                 if num2 == 0:
#                     raise ZeroDivisionError("modulo by zero")
#                 result = num1 % num2
#             elif choice == '6':
#                 result = num1 ** num2

#             print(f"✅ Result: {num1} {op_symbol} {num2} = {result}")

#             # Save result for possible reuse
#             previous_result = result

#             another_oper = input("\nDo you want to perform another operation7? (yes/no): ").strip().lower()
#             if another_oper != "yes":
#                 print("Thank you for using the calculator. Goodbye!")
#                 break

#         except ZeroDivisionError as e:
#             print(f"❌ Error: Cannot perform {op_name.lower()} ({e}).")
#             continue


# # Run the calculator
# calculator()


#-------------
# Title Function
#-------------


# name = "lakshay raj"
# print(name.title())
        

# def format_name(f_name, l_name):
#     #This type of strings are called dockstrings they are multiline strings and all are integrated in one line.
#     """Format the first and last name to title case."""    
#     if f_name == "" or l_name == "":
#         return "You didnt provide valid inputs"
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"     

# print(format_name("lakshay", "raj"))



#-------------
# Scope and Number Guessing Game
#-------------



#----------Scope--------

# enemies = 1   # This enemy variable is outside the increase enemy function, thus called  a #Global Variable

# def increase_enemies():
#     enemies = 2     # This enemy variable is inside the increase enemy function, thus it is different from the enemy variable outside. It is a #Local Variable
#     print(f"enemies inside function: {enemies}")   #This is only considere the enemy variable which is part of the function

# increase_enemies()
# print(f"enemies outside function: {enemies}")  #This will call the enemy variable which is outside the function cause the other is already called with the function

# Name space = Anything you give name to is called name space


#------Modifying Global Variable


# enemies = 1  # global variable

# def increase_enemies():
#     # global enemies  # pass as parameter
#     # enemies += 2  # modify the local copy
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1 # return the new value

# # call the function and assign the result back to global enemies
# enemies = increase_enemies#(enemies)

# print(f"enemies outside function: {enemies}")





#----------Local Scope--------

# def drink_portion():
#     portion_strenth = 2
#     print(f"The portion strenth is {portion_strenth}")

# drink_portion()
# print(f"The portion strenth is {portion_strenth}") #this will give an error because ther is no seperate portion_strenght variable
          
                        
#----------Global Scope--------

# player_health = 10  # This is a global variable

# def game():       
#     def drink_portion():
#         portion_strength = 2
#         print(f"The portion strength is {portion_strength}")

#     # drink_portion()  # Call drink_portion() inside game

# game()  # Call the outer function
# drink_portion()
# print(f"The player health is {player_health}")


#--------There is no Block Scope-------


# game_level = 3

# def horror_game():
#        enemies = ["Skeleton", "Zombie", "Alien"]
#        if game_level < 5:
#               new_enemy = enemies[0] # the value is assigned to the new_enemy variable but it wont give output because we'll have to call new_enemy with in the def 
            #   print(new_enemy)
       

# print(new_enemy) # As this print statement is outside the def it will show an error 
# horror_game() #This will give the final correct output 


#-----THE NUMBER GUESSING GAME

# import random

# def number_guessing_game():
#     print("Welcome to the Number Guessing Game!")

#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#     if difficulty == 'easy':
#         attempts = 10
#     else:
#         attempts = 3
    
#     print(f"As you choosed difficulty = {difficulty}, You have {attempts} attempts to guess the number.")
    
#     computer = random.randint(1, 100)
#     print("🎉 Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     print(f"You have {attempts} attempts to guess the number.")

#     while attempts > 0:
#         try:
#             user = int(input("Make a guess: "))         
#         except ValueError:                                 
#             print("❌ Invalid input. Please enter a valid integer.")
#             continue  # Ask again instead of breaking

#         if user < computer:
#             print("🔼 Too low.")
#         elif user > computer:
#             print("🔽 Too high.")
#         else:
#             print(f"✅ Correct! You guessed the number in {10 - attempts + 1} attempts.")
#             break

#         attempts -= 1
#         if attempts > 0:
#             print(f"🔄 You have {attempts} attempts remaining.")
#         else:
#             print(f"❌ You've run out of attempts. The number was {computer}.")

# while True:
#     number_guessing_game()
#     play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#     if play_again != 'yes':
#         print("👋 Thanks for playing! Goodbye!")
#         break



#---- Debugging and error handling-----


# def my_function():
#     for i in range(1, 20): #to get the print change 20 to 21.
#         if i == 20:
#             print("You got it")



# my_function()


# Whenever a function is not working and neither giving any bug then use the print satatement

# pages = 0
# word_per_page = 0
# pages = int(input("Enter the number of pages: "))
# word_per_page = int(input("Enter the number of words per page: "))
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)

# def mutable_list(a_list):
#     b_list = []
#     for item in a_list:
#         newitem= item * 2
#         b_list.append(newitem)
#     print(b_list)

    
# mutable_list([1, 2, 3, 4, 5])


# def check_odd_even(number):
#     """Check if a number is odd or even."""
#     return "Even" if number % 2 == 0 else "Odd"

# # Example usage
# try:
#     user_input = int(input("Enter a number: "))
#     print(f"The number {user_input} is {check_odd_even(user_input)}")
# except ValueError:
    # print("❌ Please enter a valid integer.")


#The Higher Lower Game
# score = 0

# def high_low(score):

#     print("Welcome to the Higher Lower Game!")
#     while True:
#      question = print("The first question: Which one of the following celebrities has the highest netowrth 'RONALDO' or 'virat kholi'?\nanswer in A or B")
#      answer = input("Enter your answer")
#      if answer != "A":
#          print("you loose\ngame over")
#          break
#      else:
#         print("You won")
#         score += 1
#         print(f"print your score is {score}")
#         return score

# while True:
#    score = high_low(score)
#    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#    if play_again != "yes":
#       print("Thanks for playing! Goodbye!")
#       break


#--------
# THE HIGHER LOWER GAME
#-------

# import random

# score = 0

# # List of questions as dictionaries
# questions = [
#     {
#         "question": "Which one of the following celebrities has the highest net worth?",
#         "options": {"A": "RONALDO", "B": "Virat Kohli"},
#         "correct": "A"
#     },
#     {
#         "question": "Which company is older?",
#         "options": {"A": "Microsoft", "B": "Google"},
#         "correct": "A"
#     },
#     {
#         "question": "Which country has the larger population?",
#         "options": {"A": "India", "B": "USA"},
#         "correct": "A"
#     },
#     {
#         "question": "Which planet is closer to the Sun?",
#         "options": {"A": "Venus", "B": "Mars"},
#         "correct": "A"
#     },
#     {
#         "question": "Who has won more Grand Slam titles?",
#         "options": {"A": "Roger Federer", "B": "Rafael Nadal"},
#         "correct": "B"
#     }
# ]

# def high_low(score):
#     print("Welcome to the Higher Lower Game!")
#     while True:
#         # Pick a random question
#         q = random.choice(questions)

#         print("\n" + q["question"])
#         for key, value in q["options"].items():
#             print(f"{key}: {value}")

#         answer = input("Enter your answer (A or B): ").strip().upper()

#         if answer != q["correct"]:
#             print("❌ You lose!\nGame over.")
#             break
#         else:
#             print("✅ You won!")
#             score += 1
#             print(f"🎯 Your current score is {score}")
#             return score  # Return updated score

# while True:
#     score = high_low(score)  # Update the score
#     play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
#     if play_again != "yes":
#         print("\nThanks for playing! 👋 Goodbye!")
#         break

    


    



    


    


    

    





        



    


   
    

    
        






    
                   
