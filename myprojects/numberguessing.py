#--------------
# THE NUMBER GUESSING GAME
#--------------

def play_game():
    # Define the range of numbers the user is thinking of
    low = 1
    high = 100

    print("Think of a number between 1 to 100")  # Prompt user to think of a number
    input("Press Enter when you're ready...")    # Wait for the user to get ready

    guess_count = 0  # Initialize the count of guesses

    # Start guessing loop
    while True:
        guess = (low + high) // 2  # Computer guesses the middle of the current range
        guess_count += 1  # Increment guess counter
        print(f"Is your number {guess}?")  # Ask user if this is their number

        # Get feedback from the user about the guess
        feedback = input(
            "Enter 'low' if your number is higher, 'high' if your number is lower, "
            "or 'correct' if the guess is right: "
        ).strip().lower()

        # Adjust range based on feedback
        if feedback == "low":
            low = guess + 1  # Move the lower bound up since number is higher

        elif feedback == "high":
            high = guess - 1  # Move the upper bound down since number is lower

        elif feedback == "correct":
            # Computer guessed correctly
            print(f"Hooray! I guessed it in {guess_count} guesses!")
            break  # Exit the loop

        else:
            # Handle invalid input
            print("Invalid input, please enter 'low', 'high', or 'correct'.")

# Loop to allow multiple games
while True:
    play_game()  # Start the game
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")  # Exit message
        break  # Exit the loop if user doesn't want to play again
