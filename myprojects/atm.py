#-----------------
# THE ATM MACHINE
#-----------------

def atm_machine():
    # Import regex module for pattern matching
    import re

    # Welcome message and transaction limit info
    print("WELCOME TO THE APEX ATM")
    trans_limit = 10000  # Set transaction limit
    print("Your Transaction limit is up to $10,000")

    # Ask user for their name and convert it to uppercase
    name = input("Please enter your name: ").upper()

    # Regex patterns for validating card number and PIN
    card_numpat = r"^\d{10}$"  # Card number must be exactly 10 digits
    pin_pat = r"^\d{4}$"       # PIN must be exactly 4 digits

    # Loop to validate customer and card details
    while True:
        # Ask if the user is a customer of the bank
        bank_cus = input("Are you a customer of our bank? (yes/no): ").strip().lower()

        if bank_cus == "no":
            # Inform about charges for non-customers
            print("You will be charged $3 for your withdrawal.")
        else:
            # No charges for bank customers
            print("There will be no charges over your withdrawal.")

        # Prompt user for their 10-digit card number
        card_num = input("Enter your 10 digit card number: ")
        # Validate card number with regex
        if not re.match(card_numpat, card_num):
            print("Invalid Card Number, Card Number must be of 10 digits")
            continue  # Retry if invalid

        # Prompt user for their 4-digit ATM PIN
        Atm_pin = input("Enter your 4 digit ATM Pin: ")
        # Validate ATM PIN with regex
        if not re.match(pin_pat, Atm_pin):
            print("Invalid ATM Pin, Please enter your ATM Pin again:")
            continue  # Retry if invalid

        break  # Exit loop if card details are valid

    # Loop to handle amount withdrawal
    while True:
        try:
            # Prompt user to enter withdrawal amount
            amount = int(input("Please enter the amount you want to withdraw: "))

            if amount > trans_limit:
                # Reject if amount exceeds transaction limit
                print("The amount is greater than the transaction limit of 10k")
                continue  # Retry
            elif amount <= 0:
                # Reject negative or zero amounts
                print("Please enter a positive amount")
                continue  # Retry
            else:
                # Successful transaction
                print("Your Transaction is completed, Please collect your cash and card")
                break  # Exit loop
        except ValueError:
            # Handle invalid (non-numeric) input
            print("Invalid Amount, Please enter valid digits")
            continue  # Retry

# Outer loop to allow multiple transactions
while True:
    atm_machine()  # Run the ATM process

    # Ask user if they want another transaction
    second_trans = input("Do you want to make a second Transaction (yes/no): ").strip().lower()
    if second_trans == "yes":
        # Start another transaction
        continue
    else:
        # Exit if user doesn't want to continue
        print("Thanks for visiting, Have a Good Day!")
        break
