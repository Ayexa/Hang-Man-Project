# HangMan Project --->
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Testing Code
print(f"The word is : {chosen_word}")

# Create blanks
display = []
for _ in range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # check guessed letter
    for position in range(word_lenght):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\n"
        #       f"Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    # check if there are no more "_" left in 'display'.
    # then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win!")


