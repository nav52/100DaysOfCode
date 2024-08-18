"""
Build a Hangman Game
Tasks:
    Choose a word from the list of words
    Get the user to guess the letter untill the word is completed or the lives are lost with incorrect guesses
"""
import random
from sidekick_modules.hangman_words import word_list
from sidekick_modules.hangman_art import stages, logo

# Set the lives as 6
lives = 6

# Game Initialization
print(logo)
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
entered_letters = []

# Get the user input 
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the letter was entered previously, let the user know without deducting the life
    if guess in entered_letters:
        print(f"You have already guessed {guess}")
        continue
    entered_letters.append(guess)

    display = ""

    # Check the guessed letter against the chosen word and fill the blanks
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # Deduct the life if the guessed letter is not in the word
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, it is not in the word. You lose a life")

        # Game Over if the lives becomes 0
        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The word was {chosen_word}")

    # Let the user know they have won the game when there are no more blanks
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # For hangaman art related to lives.
    print(stages[lives])
