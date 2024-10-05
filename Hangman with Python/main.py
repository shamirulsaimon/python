import random
word_list = ["aardvark","baboon","camel"]


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

word_lenght = len(chosen_word)
for position in range(word_lenght):
 placeholder += "_"

print(placeholder)

game_over = False
correct_letter = []

while not game_over:

 guess = input("Player Guess a letter: ").lower()

 display = ""

 for letter in chosen_word:
  if letter == guess:
   display += letter
   correct_letter.append(letter)
  elif letter in correct_letter:
   display+=letter
  else:
   display += "_"

 print(display)

 if "_" not in display:
  game_over = True
  print("You Win the game")