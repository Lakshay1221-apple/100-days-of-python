# THE HANGMAN PROJECT 

# HANGMAN 1 ( WORD GUESSING GAME )


import random

print("Welcome to the Hangman Game!")

# FOR GETTING A WORD-LIST OF INFINITE WORDS

# Download a word list (e.g., from https://www.mit.edu/~ecprice/wordlist.10000)

# Save it as words.txt in the same directory.

import random

def load_words():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return [word.lower() for word in words if len(word) >= 4]  # Filter short words if needed

def hangman():
    life = 3
    word_list = ["python", "java", "javascript", "ruby", "swift"]
    program_word = random.choice(word_list)

    print(f"The word has {len(program_word)} letters.")
    revealed_indices = [1, 2, 5]

    marked_word = ""
    for i in range(len(program_word)):
        if i in revealed_indices and i < len(program_word):
            marked_word += program_word[i] + " "
        else:
            marked_word += "_ "

    print("Your word (some letters revealed):")
    print(marked_word.strip())

    while life > 0:
        user_word = input("Enter your full word guess: ").lower()

        if user_word == program_word:
            print("🎉 Correct! You guessed the word!")
            return
        else:
            life -= 1
            print("❌ Wrong guess!")
            print(f"Lives remaining: {life}")

    print(f"💀 You lost! The correct word was '{program_word}'.")

# Main game loop
while True:
    hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Good day!")
        break



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
