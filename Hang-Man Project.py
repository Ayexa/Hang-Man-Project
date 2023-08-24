# HangMan Project --->
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6

from hangman_art import logo, stages
print(logo)

# Create blanks
display = []
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    # check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(display)

    # check if there are no more "_" left in 'display'.
    # then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])

