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
