# NUMBER GUESSING GAME
# This is a simple number guessing game where the computer tries to guess a number the user is thinking of.

# def play_game():
#     low = 1          # Starting lower bound
#     high = 100       # Starting upper bound

#     print("Think of a number between", low, "and", high)
#     input("Press Enter when you're ready...")

#     guess_count = 0  # Initialize guess counter

#     while True:
#         guess = (low + high) // 2  # Guess the middle of the range
#         guess_count += 1  # Increment the guess count with each guess
#         print("Is your number", guess, "?")
        
#         feedback = input("Enter 'low' if your number is higher, 'high' if it's lower, or 'correct': ")

#         if feedback == "low":
#             low = guess + 1  # If the number is higher, adjust the lower bound
#         elif feedback == "high":
#             high = guess - 1  # If the number is lower, adjust the upper bound
#         elif feedback == "correct":
#             print(f"Hooray! I guessed it in {guess_count} guesses!")  # Success message with guess count
#             break  # End the loop when the number is guessed correctly
#         else:
#             print("Invalid input. Please enter 'low', 'high', or 'correct'.")

# # Main loop to ask if the user wants to play again
# while True:
#     play_game()  # Start a new game
    
#     play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask if they want to play again
#     if play_again != "yes":
#         print("Thanks for playing! Goodbye!")  # End the game
#         break


# Atm pin

# import re

# print("WELCOME TO THE APEX ATM")

# name = input("Enter your name: ").upper()

# pattern = r"^\d{10}$"
# pin_pat = r"^\d{4}$"

# print("Your withdraw limit is up to 10K")

# while True:
#     answer = input("Are you a customer of this bank? (yes/no): ").strip().lower()

#     if answer == "no":
#         print("You will be charged $20.")
#     elif answer == "yes":
#         print("Thank you for being our customer!")
#     else:
#         print("Please answer with 'yes' or 'no'.")
#         continue  # Ask the question again

#     card_num = input("Enter your card number (10 digits): ")
#     if not re.match(pattern, card_num):
#         print("Invalid card number: must be exactly 10 digits.")
#         continue

#     while True:
#         pin = input("Enter your 4-digit ATM PIN: ")
#         if not re.match(pin_pat, pin):
#             print("Invalid PIN. Please enter exactly 4 digits.")
#             continue
#         break
#     while True:
#         try:
#             cash = int(input("Enter the amount you want to withdraw (max $10000): "))
#             if cash > 10000:
#                 print("You can only withdraw up to $10,000.")
#                 continue
#             elif cash <= 0:
#                 print("Please enter a positive amount.")
#                 continue
#             break
#         except ValueError:
#             print("Invalid input. Please enter a numeric amount.")
#             continue

#     print("Transaction successful!")
#     print("You can collect your card.")
    # print("Thank you for visiting,", name)
    # break


#complete Banking system:

# import re

# Bank_data = {}

# pattern = r"^\d{10}$"
# pin_pat = r"^\d{4}$"

# def register():
#     username = input("Enter your name: ").upper()
#     card = input("Enter your 10-digit card number: ")
#     if not re.match(pattern, card) or card in Bank_data:
#         print("Invalid or already used card number.")
#         return

#     pin = input("Enter your 4-digit PIN: ")
#     if not re.match(pin_pat, pin):
#         print("Invalid PIN format.")
#         return

#     Bank_data[card] = {
#         "name": username,
#         "pin": pin,
#         "balance": 0
#     }

#     print(f"Account created successfully for {username}.")

# def login():
#     card = input("Enter your card number: ")
#     pin = input("Enter your PIN: ")

#     user = Bank_data.get(card)
#     if user and user["pin"] == pin:
#         print(f"Welcome {user['name']}!")
#         banking_menu(card)
#     else:
#         print("Invalid card number or PIN.")

# def banking_menu(card):
#     user = Bank_data[card]
#     while True:
#         print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
#         choice = input("Choose an option: ")

#         if choice == "1":
#             print(f"Your balance is ₹{user['balance']}")
#         elif choice == "2":
#             try:
#                 amt = int(input("Enter the amount you want to deposit: "))
#                 if amt <= 0:
#                     print("Please enter a positive amount.")
#                 else:
#                     user["balance"] += amt
#                     print(f"Amount deposited successfully. Your current balance is ₹{user['balance']}")
#             except ValueError:
#                 print("Please enter a valid number.")
#         elif choice == "3":
#             try:
#                 amt = int(input("Enter amount to withdraw (Limit: ₹10,000): "))
#                 if amt <= 0:
#                     print("Enter a valid amount.")
#                 elif amt > 10000:
#                     print("Limit exceeded.")
#                 elif amt > user["balance"]:
#                     print("Insufficient balance.")
#                 else:
#                     user["balance"] -= amt
#                     print(f"Withdrawal successful. Remaining balance: ₹{user['balance']}")
#             except ValueError:
#                 print("Please enter a valid number.")
#         elif choice == "4":
#             print("Logged out.")
#             break
#         else:
#             print("Invalid choice.")

# # Main program
# while True:
#     print("\n--- Welcome To Apex Bank ---")
#     print("1. Registration\n2. Login\n3. Exit")
#     option = input("Choose an option: ")

#     if option == "1":
#         register()
#     elif option == "2":
#         login()
#     elif option == "3":
#         print("Thank you for visiting Apex Bank!")
#         break
#     else:
#         print("Invalid choice.")



# TO  DO  LIST 

# WORKPLACE = {
#     "Work": [],
#     "School": [{"Task": "HOMEWORK", "done": False}],
#     "Home": [],
#     "Groceries": [],
# }

# def display_tasks(tasks):
#     """Display tasks in a user-friendly format"""
#     if not tasks:
#         print("No tasks found.")
#         return
#     for i, task in enumerate(tasks, 1):
#         status = "✓" if task["done"] else "✗"
#         print(f"{i}. {task['Task']} [{status}]")

# def addtask():
#     """Add a new task to a workplace"""
#     print("\nSelect Workplace:")
#     print("1 for Work")
#     print("2 for School")
#     print("3 for Home")
#     print("4 for Groceries")
    
#     try:
#         work_place = int(input("Select your WORKPLACE between [1-4]: "))
#     except ValueError:
#         print("Please enter a number between 1-4")
#         return

#     workplace_map = {
#         1: "Work",
#         2: "School",
#         3: "Home",
#         4: "Groceries"
#     }

#     if work_place not in workplace_map:
#         print("Invalid choice.")
#         return

#     workplace = workplace_map[work_place]
#     task = input("Enter the task you want to add: ").strip().upper()
    
#     if not task:
#         print("Task cannot be empty!")
#         return

#     WORKPLACE[workplace].append({"Task": task, "done": False})
#     print(f"\nTask '{task}' added to {workplace}!")
#     print(f"Updated {workplace} tasks:")
#     display_tasks(WORKPLACE[workplace])

# def deletetask():
#     """Delete a task from a workplace"""
#     print("\nSelect Workplace:")
#     print("1 for Work")
#     print("2 for School")
#     print("3 for Home")
#     print("4 for Groceries")

#     try:
#         work_place = int(input("Select your WORKPLACE between [1-4]: "))
#     except ValueError:
#         print("Invalid input. Please enter a number.")
#         return

#     workplace_map = {
#         1: "Work",
#         2: "School",
#         3: "Home",
#         4: "Groceries"
#     }

#     if work_place not in workplace_map:
#         print("Invalid choice.")
#         return

#     workplace = workplace_map[work_place]
#     tasks = WORKPLACE[workplace]
    
#     print(f"\nCurrent {workplace} tasks:")
#     display_tasks(tasks)
    
#     if not tasks:
#         return

#     task_to_delete = input("Enter the exact task name you want to delete: ").strip().upper()
    
#     deleted = False
#     for task in tasks[:]:  # Create a copy to iterate over
#         if task["Task"] == task_to_delete:
#             tasks.remove(task)
#             deleted = True
#             break
    
#     if deleted:
#         print(f"\nTask '{task_to_delete}' removed successfully!")
#     else:
#         print(f"\nTask '{task_to_delete}' not found. Please check the exact name.")
    
#     print(f"Updated {workplace} tasks:")
#     display_tasks(tasks)

# def viewtask():
#     """View tasks in a workplace"""
#     print("\nSelect Workplace:")
#     print("1 for Work")
#     print("2 for School")
#     print("3 for Home")
#     print("4 for Groceries")

#     try:
#         work_place = int(input("Select workplace to view [1-4]: "))
#     except ValueError:
#         print("Please enter a number between 1-4")
#         return

#     workplace_map = {
#         1: "Work",
#         2: "School",
#         3: "Home",
#         4: "Groceries"
#     }

#     if work_place not in workplace_map:
#         print("Invalid choice.")
#         return

#     workplace = workplace_map[work_place]
#     print(f"\nTasks in {workplace}:")
#     display_tasks(WORKPLACE[workplace])

# def markas_complete():
#     """Mark a task as complete"""
#     print("\nSelect Workplace:")
#     print("1 for Work")
#     print("2 for School")
#     print("3 for Home")
#     print("4 for Groceries")

#     try:
#         work_place = int(input("Select workplace [1-4]: "))
#     except ValueError:
#         print("Please enter a number between 1-4")
#         return

#     workplace_map = {
#         1: "Work",
#         2: "School",
#         3: "Home",
#         4: "Groceries"
#     }

#     if work_place not in workplace_map:
#         print("Invalid choice.")
#         return

#     workplace = workplace_map[work_place]
#     tasks = WORKPLACE[workplace]
    
#     print(f"\nCurrent {workplace} tasks:")
#     display_tasks(tasks)
    
#     if not tasks:
#         return

#     try:
#         task_num = int(input("Enter the task number to mark complete: "))
#         if task_num < 1 or task_num > len(tasks):
#             print("Invalid task number!")
#             return
#     except ValueError:
#         print("Please enter a valid number.")
#         return

#     tasks[task_num-1]["done"] = True
#     print(f"\nTask '{tasks[task_num-1]['Task']}' marked as complete!")
#     print(f"Updated {workplace} tasks:")
#     display_tasks(tasks)

# def main():
#     """Main program loop"""
#     print("WELCOME TO TO-DO-LIST MANAGER")
    
#     while True:
#         print("\nMAIN MENU:")
#         print("1. ADD TASK")
#         print("2. DELETE TASK")
#         print("3. VIEW TASKS")
#         print("4. MARK TASK AS COMPLETE")
#         print("5. EXIT")

#         try:
#             choice = int(input("Select option [1-5]: "))
#         except ValueError:
#             print("Please enter a number between 1-5")
#             continue

#         if choice == 1:
#             addtask()
#         elif choice == 2:
#             deletetask()
#         elif choice == 3:
#             viewtask()
#         elif choice == 4:
#             markas_complete()
#         elif choice == 5:
#             print("\nThank you for using To-Do List Manager. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please select 1-5")

# if __name__ == "__main__":
#     main()



#RANDOM PASSOWRD  GENERATOR

# import random
# import string

# def generate_passowrd():
#     print("Welcome to the Passowrd Generator")

#     try:
#         # Ask user for password length and character counts
#         total_length = int(input("Enter the length of password you want: "))
#         num_letters = int(input("How many letters do you want? "))
#         num_numbers = int(input("How many numbers do you want? "))
#         num_specialcharc = int(input("How many special characters do you want? "))

#     except ValueError:  
#         print("Please enter valid numbers.")
#         return

#     # This check must be outside of the try block
#     if total_length != num_letters + num_numbers + num_specialcharc:
#         print("Total letters, special characters, and numbers do not match the length of the password.")
#         return

#     # Generate characters
#     letters = random.choices(string.ascii_letters, k=num_letters)  
#     numbers = random.choices(string.digits, k=num_numbers)         
#     special = random.choices(string.punctuation, k=num_specialcharc)  

#     # Calculate remaining characters if needed (optional based on earlier logic)
#     remaining = total_length - (num_letters + num_numbers + num_specialcharc)  

#     all_charc = string.ascii_letters + string.digits + string.punctuation
#     filler = random.choices(all_charc, k=remaining)  

    
#     password_charc = letters + numbers + special + filler  
#     random.shuffle(password_charc)  
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


import random

def load_words():
    return ["python", "java", "javascript", "ruby", "swift"]

def hangman():
    life = 3
    word_list = load_words()
    program_word = random.choice(word_list)
    word_length = len(program_word)

    # Reveal some letters at random
    num_to_reveal = max(1, word_length // 3)
    revealed_indices = random.sample(range(word_length), num_to_reveal)

    word_display = []
    revealed_letters = set()
    player_guessed_letters = set()

    for i in range(word_length):
        if i in revealed_indices:
            word_display.append(program_word[i])
            revealed_letters.add(program_word[i])
        else:
            word_display.append("_")

    print("\n🎮 Welcome to the Hangman Game!")
    print(f"The word has {word_length} letters.")
    print("Some letters are already revealed to help you!")
    print("Word:", " ".join(word_display))

    while life > 0 and "_" in word_display:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue

        if guess in player_guessed_letters:
            print("⏳ You've already guessed that letter.")
            continue

        player_guessed_letters.add(guess)

        if guess in program_word:
            print("✅ Correct guess!")
            for idx, char in enumerate(program_word):
                if char == guess:
                    word_display[idx] = guess
        else:
            life -= 1
            print(f"❌ Wrong guess! Lives remaining: {life}")

        print("Word:", " ".join(word_display))
        print("Guessed letters:", ", ".join(sorted(player_guessed_letters)))

    if "_" not in word_display:
        print(f"\n🎉 You won! The word was: {program_word}")
    else:
        print(f"\n💀 You lost! The word was: {program_word}")

# Main game loop
while True:
    hangman()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break


# THE CAESAR CIPHER PROJECT
 
import string
import pyfiglet

# Show ASCII logo
logo = pyfiglet.figlet_format("Caesar Cipher", font="starwars")
print(logo)

def Caesar_cipher():
    while True:
        print("\nWelcome to the Caesar Cipher Program!")
        print("This program will help you to encrypt or decrypt a message using the Caesar cipher technique.")

        alphabets = list(string.ascii_lowercase)
        numbers = list(string.digits)

        try:
            direction = input("Type 'encode' to encrypt your message or 'decode' to decrypt your message: ").lower()
            if direction not in ['encode', 'decode']:
                print("Invalid input. Please enter 'encode' or 'decode'.")
                continue

            text = input("Enter your message: ").lower()
            shift = int(input("Enter the shift number: "))

            if shift < 0:
                print("Shift number cannot be negative. Please enter a positive shift number.")
                continue 

            shift_alpha = shift % 26
            shift_digit = shift % 10
            Cipher_text = ""

            for char in text:
                if char in alphabets:
                    index = alphabets.index(char)
                    new_index = (index + shift_alpha) % 26 if direction == 'encode' else (index - shift_alpha) % 26
                    Cipher_text += alphabets[new_index]

                elif char in numbers:
                    index = numbers.index(char)
                    new_index = (index + shift_digit) % 10 if direction == 'encode' else (index - shift_digit) % 10
                    Cipher_text += numbers[new_index]

                else:
                    Cipher_text += char  # Leave punctuation and symbols unchanged

            print(f"\nThe {direction}d message is: {Cipher_text}")

        except ValueError:
            print("Invalid input. Please enter a valid shift number.")
            continue

        run_again = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
        if run_again != "yes":
            print("Thanks for using the Caesar Cipher Program! Goodbye!")
            break

Caesar_cipher()


# The Secret Auction Project

def secret_auction():
    
    print("Welcome to the Secret Auction Program!")
    print("This program will help you to conduct a secret auction.")

    bids = {}

    while True:
        name = input("Enter the name of the bidder: ")

        if name in bids:
            print("This name has already been used. Please enter a different name.")
            continue

        try:
            bid_amount = float(input("Enter the bid amount: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number for the bid amount.")
            continue

        bids[name] = bid_amount

        another_bidder = input("Is there another bidder? (yes/no): ").strip().lower()
        if another_bidder != "yes":
            break

    # Determine the highest bidder
    if bids:
        highest_bidder = max(bids, key=bids.get)
        highest_bid = bids[highest_bidder]
        print(f"\nThe highest bidder is {highest_bidder} with a bid of ${highest_bid:.2f}.")

# Run the program and optionally allow re-running
while True:
    secret_auction()
    run_again = input("\nDo you want to run the Secret Auction Program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        print("Thanks for using the Secret Auction Program! Goodbye!")
        break

# The Grading Criteria Project

def grading_criteria():
    print("Welcome to the grading criteria!")
    print("This program will help you determine the grade based on the marks entered.")

    students = {}

    # Input phase
    while True:
        name = input("\nEnter the name of the student: ").strip()

        if name in students:
            print("This name has already been used. Please enter a different name.")
            continue

        try:
            grade = int(input("Enter the marks of the student (0-100): "))
            if not (0 <= grade <= 100):
                print("Invalid marks. Please enter a value between 0 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        students[name] = grade

        # Strict validation for yes/no
        while True:
            another = input("Do you want to enter another student? (yes/no): ").strip().lower()
            if another in ("yes", "no"):
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if another == "no":
            break

    # Grade assignment
    print("\n--- Grade Results ---")
    for student, grade in students.items():
        if grade >= 90:
            letter = 'A'
        elif grade >= 80:
            letter = 'B'
        elif grade >= 70:
            letter = 'C'
        elif grade >= 60:
            letter = 'D'
        elif grade >= 50:
            letter = 'E'
        else:
            letter = 'F'

        print(f"{student} has received grade {letter}.")

    # Optional: Personal check
    while True:
        check = input("\nDo you want to check the marks of a specific student? (yes/no): ").strip().lower()

        if check != 'yes' and check != "no":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        if check == "no":
            break

        name_to_check = input("Enter the name of the student to check: ").strip()
        if name_to_check in students:
            print(f"{name_to_check} scored {students[name_to_check]} marks.")
        else:
            print("No such student found.")

# Loop to run program multiple times
while True:
    grading_criteria()
    again = input("\nDo you want to run the program again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for using the grading criteria program! Goodbye!")
        break


#-----------------
# THE CALCULATOR PROJECT
#-----------------


def calculator():
    """A simple command-line calculator with previous result support."""
    print("Welcome to the Calculator")
    print("This program helps you perform basic arithmetic operations.")

    operations = {
        "1": ("Addition", "+"),
        "2": ("Subtraction", "-"),
        "3": ("Multiplication", "*"),
        "4": ("Division", "/"),
        "5": ("Remainder", "%"),
        "6": ("Power of", "**"),
        "7": ("Exit", None)
    }

    previous_result = None  # To store result of previous operation

    while True:
        print("\nAvailable operations:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter the choice (1-7) for the operation you want to use: ")

        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in operations:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")
            continue

        try:
            # Ask if user wants to use previous result or enter new inputs
            if previous_result is not None:
                reuse = input("Do you want to use the previous result? (yes/no): ").strip().lower()
                if reuse == "yes":
                    num1 = previous_result
                    print(f"First number is set to previous result: {num1}")
                else:
                    num1 = float(input("Enter the first number: "))
            else:
                num1 = float(input("Enter the first number: "))

            num2 = float(input("Enter the second number: "))

        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
            continue

        op_name, op_symbol = operations[choice]

        try:
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError("division by zero")
                result = num1 / num2
            elif choice == '5':
                if num2 == 0:
                    raise ZeroDivisionError("modulo by zero")
                result = num1 % num2
            elif choice == '6':
                result = num1 ** num2

            print(f"✅ Result: {num1} {op_symbol} {num2} = {result}")

            # Save result for possible reuse
            previous_result = result

            another_oper = input("\nDo you want to perform another operation7? (yes/no): ").strip().lower()
            if another_oper != "yes":
                print("Thank you for using the calculator. Goodbye!")
                break

        except ZeroDivisionError as e:
            print(f"❌ Error: Cannot perform {op_name.lower()} ({e}).")
            continue


# Run the calculator
calculator()

#--------------
# THE BLACK JACK 21 PROJECT
#--------------

import random

player_balance = 1500  # Global balance

def black_jack_21(balance):
    print("\n🎲 Welcome to the Black Jack 21 Game!")
    print(f"Your current balance: 💰 {balance}")

    print("\n♠️ Blackjack Rules:\n")
    print("1️⃣ Get as close to 21 as possible without going over.")
    print("2️⃣ Face cards = 10, Ace = 1 or 11.")
    print("3️⃣ Dealer draws until total reaches at least 17.\n")

    cards = {
        "Number cards": [2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Face cards": [10, 10, 10],  # King, Queen, Jack
        "Ace": [11]
    }

    deck = cards["Number cards"] + cards["Face cards"] + cards["Ace"]

    # Place a bet
    while True:
        try:
            bet = int(input(f"Place your bet (Available: {balance}): "))
            if bet > balance or bet <= 0:
                print("❌ Invalid bet. Try again.")
            else:
                break
        except ValueError:
            print("❌ Please enter a valid number.")

    print(f"Your balance after bet is {balance - bet}")

    # Deal initial cards
    player_cards = [random.choice(deck), random.choice(deck)]
    dealer_cards = [random.choice(deck), random.choice(deck)]

    def calculate_score(hand):
        """Adjust Ace from 11 to 1 if total > 21"""
        score = sum(hand)
        while score > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
            score = sum(hand)
        return score

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"\nYour cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    # Player's turn
    while True:
        choice = input("Type 'hit' to draw another card or 'stand' to pass: ").lower()
        if choice == "hit":
            player_cards.append(random.choice(deck))
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")

            if player_score > 21:
                print("💥 You went over 21! Dealer wins.")
                balance -= bet
                print(f"Your balance is now: 💰 {balance}")
                return balance
            elif player_score == 21:
                print("🎉 You hit 21!")
                break
        elif choice == "stand":
            break
        else:
            print("❌ Invalid choice. Please type 'hit' or 'stand'.")

    # Dealer's turn
    print(f"\nDealer's cards: {dealer_cards}, current score: {dealer_score}")
    while dealer_score < 17:
        dealer_cards.append(random.choice(deck))
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer drew: {dealer_cards[-1]}, total score: {dealer_score}")

    # Final results
    print("\n--- Final Scores ---")
    print(f"Your hand: {player_cards}, score: {player_score}")
    print(f"Dealer's hand: {dealer_cards}, score: {dealer_score}")

    if dealer_score > 21:
        print("🎉 Dealer went over 21! You win!")
        balance += bet
    elif dealer_score == player_score:
        print("🤝 It's a draw. Your balance remains unchanged.")
    elif dealer_score > player_score:
        print("😞 Dealer wins!")
        balance -= bet
    else:
        print("🎉 You win!")
        balance += bet

    print(f"Your balance is now: 💰 {balance}")
    return balance

# Main game loop
while True:
    if player_balance <= 0:
        print("\n💸 You have no more money! Game over.")
        break

    player_balance = black_jack_21(player_balance)

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print(f"\nThanks for playing! You walk away with 💰 {player_balance}")
        break
