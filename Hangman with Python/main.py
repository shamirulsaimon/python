import random
word_list = ["aardvark","baboon","camel"]
# TO Do -1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)
# TO DO -2 Ask the user to Guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Player Guess a letter: ").lower()
# TO DO -3 Check if the letter the user guessed (guess) is one of letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
for letter in chosen_word:
 # print(letter)
 if letter == guess:
  print("Right")
 else:
  print("wrong")