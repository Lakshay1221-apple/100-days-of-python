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