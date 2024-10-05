import random

stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)  # For testing purposes

placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letter = []

while not game_over:

    guess = input("Player, guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)

    # This condition checks if the guess is not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        if lives == 0:
            print("Game over. You lose!")
            game_over = True

    if "_" not in display:
        game_over = True
        print("You win the game!")

    print(stages[lives])
