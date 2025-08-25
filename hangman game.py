import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "challenge", "computer"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    word_display = ["_"] * len(word)

    print("Welcome to Hangman!")
    print("Guess the word:")

    while attempts > 0 and "_" in word_display:
        print("\nWord:", " ".join(word_display))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    word_display[idx] = guess
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in word_display:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
