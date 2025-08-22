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