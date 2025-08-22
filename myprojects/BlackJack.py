
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