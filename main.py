# / # / # PROJECT OF DAY 7 # / # / #

import random
import hangman_art
import hangman_words
from replit import clear

stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
display = []
guessed_letters = []
word_length = len(chosen_word)
print(f"Pssst, the solution is {chosen_word}.")
print(hangman_art.logo)

for _ in range(word_length):
    display += "_"

print(display)

incomplete_word = True
lives = 6


while incomplete_word:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in chosen_word and guess not in guessed_letters:
        guessed_letters += guess
    elif guess in chosen_word and guess in guessed_letters:
        print("You've already guessed this letter!")

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess

    print(display)

    if guess not in chosen_word:
        print(f"{guess} is not in the word!")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose!")
            incomplete_word = False

    if "_" not in display:
        print("You won!")
        incomplete_word = False
