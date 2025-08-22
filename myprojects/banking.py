import re  # Import regex module for validating card numbers and PINs

# Global dictionary to store bank data (card number as key, user info as value)
Bank_data = {}

# Regex patterns for validation
card_numpat = r"^\d{10}$"  # Card number must be exactly 10 digits
pin_pat = r"^\d{4}$"       # PIN must be exactly 4 digits


def register():
    """Handles the user registration process."""
    username = input("Enter Your User Name: ").upper()

    # --- Card Number Input and Validation ---
    card = input("Enter your 10-digit card number: ")
    # Check if card number is valid and not already in use
    if not re.match(card_numpat, card) or card in Bank_data:
        print("❌ Invalid or already used card number. Please try again.")
        return  # Exit the function if card is invalid

    # --- PIN Input and Validation ---
    pin = input("Enter your 4-digit card PIN: ")
    if not re.match(pin_pat, pin):
        print("❌ Invalid PIN format. It must be 4 digits. Please try again.")
        return  # Exit the function if PIN is invalid

    # --- Store new user data ---
    Bank_data[card] = {
        "name": username,  # Store user's name
        "pin": pin,        # Store user's PIN
        "balance": 0       # Start with ₹0 balance
    }
    print(f"✅ Account for {username} created successfully!")


def login():
    """Handles the user login process."""
    while True:
        # Prompt user for card number and PIN
        card = input("Enter your card number: ")
        pin = input("Enter your PIN: ")

        # Fetch user data from Bank_data using card number
        user = Bank_data.get(card)

        # Check if card exists and PIN matches
        if user and user["pin"] == pin:
            print(f"✅ Welcome {user['name']}!")
            banking_system(user)  # Pass user data to banking system
            break  # Exit login loop after successful login
        else:
            print("❌ Invalid card number or PIN. Please try again.")
            continue


def banking_system(user):
    """Handles the banking features for a logged-in user."""

    while True:
        # Show main banking menu
        print(f"\n--- Welcome To The Bank, {user['name']} ---")
        print("1. Balance Check")
        print("2. Transfer Funds")
        print("3. Exit")

        choice = input("Choose the feature you want to use: ")

        if choice == '1':
            # Show current balance
            print(f"💰 Your balance is ₹{user['balance']}")

        elif choice == '2':
            # Handle fund transfer
            print(f"💰 Your account balance is ₹{user['balance']}")
            trans_name = input("Enter the name of the person you want to transfer funds to: ")
            trans_card = input("Enter the card number of the person you want to transfer funds to: ")

            # Validate recipient card number format
            if not re.match(card_numpat, trans_card):
                print("❌ Invalid card number. Please enter the card number again.")
                continue  # Restart transfer process

            try:
                # Prompt for transfer amount
                trans_amount = int(input("Enter the amount you want to transfer: ₹"))

                # Check if user has enough balance
                if trans_amount > user["balance"]:
                    print("❌ Insufficient balance. Please try again.")
                    continue

                elif trans_amount <= 0:
                    print("❌ Invalid transfer amount. Please enter a positive number.")
                    continue

                else:
                    # Deduct transfer amount from user's balance
                    user["balance"] -= trans_amount

                    print(f"✅ ₹{trans_amount} has been transferred successfully to {trans_name} (Card: {trans_card})")

                    # Ask if user wants to see remaining balance
                    rem_balance = input("Do you want to see your remaining balance? (yes/no): ").strip().lower()
                    if rem_balance == 'yes':
                        print(f"💰 Your remaining balance is ₹{user['balance']}")
                    else:
                        print("✅ Transfer complete.")
                    break  # Exit transfer process

            except ValueError:
                print("❌ Invalid amount. Please enter digits only.")
                continue

        elif choice == '3':
            # Exit banking system
            print("👋 Thank you for using our service. Goodbye!")
            break

        else:
            # Handle invalid menu choice
            print("❌ Invalid choice. Please select 1, 2, or 3.")
            continue


def banking_menu():
    """Main menu for the banking application."""
    while True:
        print("\n--- Welcome To The Bank ---")
        print("1. Register a new account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register()  # Call register function
        elif choice == '2':
            login()     # Call login function
        elif choice == '3':
            print("👋 Thank you for visiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")


# Entry point for the program
if __name__ == "__main__":
    banking_menu()  # Start the banking menu


