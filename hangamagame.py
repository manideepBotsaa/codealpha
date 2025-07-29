import random

# List of predefined words
words = ["apple", "tiger", "house", "train", "green"]

# Choose a random word
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a display of underscores for the word
display_word = ["_"] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Let's begin!\n")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("Current word: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
        print("Good guess!\n")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_guesses - incorrect_guesses} guesses left.\n")

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over! The word was:", word_to_guess)
