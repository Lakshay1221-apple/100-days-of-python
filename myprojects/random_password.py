#RANDOM PASSOWRD  GENERATOR

import random
import string

def generate_passowrd():
    print("Welcome to the Passowrd Generator")

    try:
        # Ask user for password length and character counts
        total_length = int(input("Enter the length of password you want: "))
        num_letters = int(input("How many letters do you want? "))
        num_numbers = int(input("How many numbers do you want? "))
        num_specialcharc = int(input("How many special characters do you want? "))

    except ValueError:  
        print("Please enter valid numbers.")
        return

    # This check must be outside of the try block
    if total_length != num_letters + num_numbers + num_specialcharc:
        print("Total letters, special characters, and numbers do not match the length of the password.")
        return

    # Generate characters
    letters = random.choices(string.ascii_letters, k=num_letters)  
    numbers = random.choices(string.digits, k=num_numbers)         
    special = random.choices(string.punctuation, k=num_specialcharc)  

    # Calculate remaining characters if needed (optional based on earlier logic)
    remaining = total_length - (num_letters + num_numbers + num_specialcharc)  

    all_charc = string.ascii_letters + string.digits + string.punctuation
    filler = random.choices(all_charc, k=remaining)  

    
    password_charc = letters + numbers + special + filler  
    random.shuffle(password_charc)  
    password = ''.join(password_charc)  

    print(f"Your password has been generated: {password}")  


generate_passowrd()
